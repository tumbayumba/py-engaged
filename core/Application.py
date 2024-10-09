from http.server import BaseHTTPRequestHandler

from core.configuration.Config import Config
from core.configuration.ConfigInterface import ConfigInterface
from core.request.Request import Request
from core.request.RequestInterface import RequestInterface
from core.routing.Router import Router
from core.routing.RouterInterface import RouterInterface


class Application:

    __config: ConfigInterface
    __handler: BaseHTTPRequestHandler
    __request: RequestInterface
    __router: RouterInterface

    def __init__(self, request_handler: BaseHTTPRequestHandler):
        self.set_config(Config())
        self.set_handler(request_handler)
        self.set_request(Request(request_handler))
        self.set_router(Router(self.config.get('routes')))

    def run(self):
        self.router.parse(self.request)

        # Send common response headers
        self.handler.send_response(200)
        self.handler.send_header('Content-type', 'application/json')
        self.handler.end_headers()

        # Handle different methods
        match self.request.method():
            case 'GET':
                self.handler.wfile.write(b'Handled GET request')
            case 'POST':
                self.handler.wfile.write(b'Handled POST request')
                # handler.wfile.write(f"{content}".encode('utf-8'))
            case 'PUT':
                self.handler.wfile.write(b'Handled PUT request')
            case 'PATCH':
                self.handler.wfile.write(b'Handled PATCH request')
            case 'DELETE':
                self.handler.wfile.write(b'Handled DELETE request')
            case _:
                self.handler.wfile.write(b'Unhandled HTTP method')


    @property
    def config(self):
        return self.__config

    def set_config(self, value):
        if not isinstance(value, ConfigInterface):
            raise ValueError("`config` must be an instance of ConfigInterface")
        self.__config = value

    @property
    def handler(self):
        return self.__handler

    def set_handler(self, value):
        if not isinstance(value, BaseHTTPRequestHandler):
            raise ValueError("`handler` must be an instance of BaseHTTPRequestHandler")
        self.__handler = value

    @property
    def request(self):
        return self.__request

    def set_request(self, value: RequestInterface):
        if not isinstance(value, RequestInterface):
            raise ValueError("`request` must be an instance of RequestInterface")
        self.__request = value

    @property
    def router(self):
        return self.__router

    def set_router(self, value: RouterInterface):
        if not isinstance(value, RouterInterface):
            raise ValueError("`router` must be an instance of RouterInterface")
        self.__router = value
