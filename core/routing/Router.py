import importlib
from core.controller.Controller import Controller
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

    def __init__(self, routes: Optional[Dict[str, Dict[str, str]]] = None):
        self.set_routes(routes if routes is not None else {})

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

    def module(self):
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
                raise RouterException(f'Method {method} does not match route {self.endpoint()}')

            module_controller_action = route['controller'].rsplit('.', 2)
            if len(module_controller_action) != 3:
                raise RouterException(f'Invalid controller action {module_controller_action}')

            self.set_module_name(module_controller_action[0])
            self.set_controller_name(module_controller_action[1])
            self.set_action_name(module_controller_action[2])
        except RouterException as e:
            self.set_controller_name('Controller')
            self.set_action_name('not_found')


    def dispatch(self, request: RequestInterface):
        self.parse(request)

        module = importlib.import_module(self.module())
        controller_class = getattr(module, self.controller_name())
        # Create an instance of the controller class
        controller_instance = controller_class()
        # Dynamically get the method
        method = getattr(controller_instance, self.action_name())

        method()



