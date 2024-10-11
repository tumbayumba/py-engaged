from core.controller.Controller import Controller
from core.request.RequestInterface import RequestInterface
from core.routing.RouterInterface import RouterInterface
from typing import Dict, Optional

class Router(RouterInterface):

    __routes: Dict[str, Dict[str, str]]
    __current_route: Dict
    __endpoint: str
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
        if route is None:
            raise ValueError(f'No route found for {self.endpoint()}')

        if method != route['method']:
            raise ValueError(f'Method {method} does not match route {self.endpoint()}')

        controller_action = route['controller'].split('.')
        if len(controller_action) != 2:
            raise ValueError(f'Invalid controller action {controller_action}')

        self.set_controller_name(controller_action[0])
        self.set_action_name(controller_action[1])


    def dispatch(self, request: RequestInterface):
        self.parse(request)


