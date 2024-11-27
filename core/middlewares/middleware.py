from abc import ABC, abstractmethod
from core.Application import Application
from core.request.RequestInterface import RequestInterface


class Middleware(ABC):

    @abstractmethod
    def handle(self, request: RequestInterface):
        raise NotImplemented;

    @property
    def app(self): 
        return Application.get_instance();