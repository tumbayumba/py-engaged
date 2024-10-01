import urllib
from cgitb import handler
from http.server import BaseHTTPRequestHandler
import urllib.parse

from core.request.Request import Request
from core.request.RequestInterface import RequestInterface


class Application:

    __handler: BaseHTTPRequestHandler
    __request: RequestInterface

    def __init__(self, request_handler: BaseHTTPRequestHandler):
        self.set_request(Request(request_handler))
        self.set_handler(request_handler)

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

    def run(self):
        self.request.set_header('Host', 'google.com')
        print(f'Request method: {self.request.header('Host')}')
        path = self.handler.path
        parsed_path = urllib.parse.urlparse(path)
        query_params = urllib.parse.parse_qs(parsed_path.query)
        request_version = self.handler.request_version

        # content_length = int(headers['Content-Length'])
        # body = self.handler.rfile.read(content_length)
        # content = body.decode('utf-8')

        print(f'Path: {path}')
        print(f'Request Version: {request_version}')
        print(f'Parsed Path: {parsed_path}')
        print(f'Query Params: {query_params}')
        # print(f'Content: {content}')

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
