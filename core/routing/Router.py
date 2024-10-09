from core.controller.Controller import Controller
from core.request.RequestInterface import RequestInterface
from core.routing.RouterInterface import RouterInterface
from typing import Dict, Optional

class Router(RouterInterface):

    __routes: Dict[str, Dict[str, str]]
    __controller_name: str
    __action_name: str

    def __init__(self, routes: Optional[Dict[str, Dict[str, str]]] = None):
        self.set_routes(routes if routes is not None else {})

    def routes(self):
        return self.__routes

    def set_routes(self, routes: Dict[str, Dict[str, str]]):
        self.__routes = routes

    def parse(self, request: RequestInterface):
        method = request.method()
        url = request.url()
        print(f'{method} {url}')



    def dispatch(self):
        pass


