from core.middlewares.middleware import Middleware
from core.request.RequestInterface import RequestInterface


class My(Middleware):
    
    def handle(self, request: RequestInterface):

        return True