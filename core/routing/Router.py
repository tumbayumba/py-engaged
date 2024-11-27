import importlib
from core.errors.MethodNotAllowedException import MethodNotAllowedException
from core.errors.RouterException import RouterException
from core.request.RequestInterface import RequestInterface
from core.routing.RouterInterface import RouterInterface
from typing import Dict, Optional

class Router(RouterInterface):

    __routes: Dict[str, Dict[str, str]]
    __current_route: Dict
    __endpoint: str
    __module_name: str
    __controller_name: str
    __action_name: str
    __action_args: Dict
    __middlewares: list = []

    def __init__(self, routes: Optional[Dict[str, Dict[str, str]]] = None):
        self.set_routes(routes if routes is not None else {})
        self.set_action_args({})
        self.set_middlewares([])

    def routes(self):
        return self.__routes

    def set_routes(self, routes: Dict[str, Dict[str, str]]):
        self.__routes = routes

    def current_route(self):
        return self.__current_route

    def set_current_route(self, route: Dict):
        self.__current_route = route

    def endpoint(self):
        return self.__endpoint

    def set_endpoint(self, value: str):
        self.__endpoint = value

    def module_name(self):
        return self.__module_name

    def set_module_name(self, value: str):
        self.__module_name = value

    def controller_name(self):
        return self.__controller_name

    def set_controller_name(self, value: str):
        self.__controller_name = value

    def action_name(self):
        return self.__action_name

    def set_action_name(self, value: str):
        self.__action_name = value

    def action_args(self): 
        return self.__action_args

    def set_action_args(self, arguments: Dict):
        self.__action_args = arguments

    def middlewares(self): 
        return self.__middlewares

    def set_middlewares(self, values: list):
        self.__middlewares = values

    def add_middleware(self, value: Dict):
        self.__middlewares.append(value)
        

    def parse(self, request: RequestInterface):
        url = request.url()
        method = request.method()
        self.set_endpoint(url.path)
        routes = self.routes()
        route = routes.get(self.endpoint())

        self.set_current_route(route)
        try:
            if route is None:
                raise RouterException(f'No route found for {self.endpoint()}')

            if method != route['method']:
                raise MethodNotAllowedException(f'Method `{method}` not allowed for {self.endpoint()}')
            
            # Handle middlewares if they exist
            if route.get('middlewares') is not None and isinstance(route['middlewares'], list):
                for middleware in route.get('middlewares'):
                    middleware_module_class = middleware.rsplit('.', 1)
                    self.add_middleware(dict(
                        module_name=middleware_module_class[0],
                        class_name=middleware_module_class[1],
                    ))

            module_controller_action = route['controller'].rsplit('.', 2)
            if len(module_controller_action) != 3:
                raise RouterException(f'Invalid controller action {module_controller_action}')

            self.set_module_name(module_controller_action[0])
            self.set_controller_name(module_controller_action[1])
            self.set_action_name(module_controller_action[2])
        except (RouterException, MethodNotAllowedException) as e:
            # Map the status code based on the exception type
            status_code = 405 if isinstance(e, MethodNotAllowedException) else 400
            self._set_error_handler(e, status_code)


    def _set_error_handler(self, exception, status_code):
        """Helper method to handle route errors by setting default error action."""
        self.set_module_name('core.controller.ErrorController')
        self.set_controller_name('ErrorController')
        self.set_action_name('error')
        self.set_action_args({"message": str(exception), "http_status_code": status_code})


    def dispatch(self, request: RequestInterface):
        self.parse(request)

        # disptach logic first to middlewares if they exist
        middlewares = self.middlewares()
        if len(middlewares) > 0:
            for middleware in middlewares:
                middleware_module = importlib.import_module(middleware['module_name'])
                middleware_class = getattr(middleware_module, middleware['class_name'])
                middleware_instance = middleware_class()
                handle = getattr(middleware_instance, 'handle')
                middleware_result = handle(request)
                if not isinstance(middleware_result, bool):
                    return middleware_result

        module = importlib.import_module(self.module_name())
        controller_class = getattr(module, self.controller_name())
        # Create an instance of the controller class
        controller_instance = controller_class()
        # Dynamically get the method
        method = getattr(controller_instance, self.action_name())
        # Unpacking dict into function arguments
        arguments = self.action_args()
        if arguments:
            return method(**arguments)
            
        return method()



