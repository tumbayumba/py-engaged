from abc import ABC, abstractmethod
from typing import Dict

from core.request.RequestInterface import RequestInterface


class RouterInterface(ABC):

    @abstractmethod
    def parse(self, request: RequestInterface):
        raise NotImplementedError

    @abstractmethod
    def dispatch(self, request: RequestInterface):
        raise NotImplementedError

    @abstractmethod
    def routes(self):
        raise NotImplementedError

    @abstractmethod
    def set_routes(self, routes: Dict[str, Dict[str, str]]):
        raise NotImplementedError

    @abstractmethod
    def current_route(self):
        raise NotImplementedError

    @abstractmethod
    def set_current_route(self, route: Dict):
        raise NotImplementedError

    @abstractmethod
    def endpoint(self):
        raise NotImplementedError

    @abstractmethod
    def set_endpoint(self, value: str):
        raise NotImplementedError

    @abstractmethod
    def controller_name(self):
        raise NotImplementedError

    @abstractmethod
    def set_controller_name(self, value: str):
        raise NotImplementedError

    @abstractmethod
    def action_name(self):
        raise NotImplementedError

    @abstractmethod
    def set_action_name(self, value: str):
        raise NotImplementedError
