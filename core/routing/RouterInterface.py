from abc import ABC, abstractmethod
from typing import Dict

from core.request.RequestInterface import RequestInterface


class RouterInterface(ABC):

    @abstractmethod
    def parse(self, request: RequestInterface):
        raise NotImplementedError

    @abstractmethod
    def dispatch(self):
        raise NotImplementedError

    @abstractmethod
    def routes(self):
        raise NotImplementedError

    @abstractmethod
    def set_routes(self, routes: Dict[str, Dict[str, str]]):
        raise NotImplementedError
