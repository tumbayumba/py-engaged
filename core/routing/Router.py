from core.controller.Controller import Controller
from core.request.RequestInterface import RequestInterface
from core.routing.RouterInterface import RouterInterface
from typing import Dict

class Router(RouterInterface):

    __routes: Dict[str, Dict[str, str]]
    __controller: Controller

    def __init__(self):
        self.__routes = {}
        self.__controller = None

    def routes(self):
        return self.__routes

    def set_routes(self, routes: Dict[str, Dict[str, str]]):
        self.__routes = routes

    def parse(self, request: RequestInterface):
        pass

    def dispatch(self):
        pass


