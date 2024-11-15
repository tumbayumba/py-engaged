from http.server import SimpleHTTPRequestHandler
import json
from typing import Dict
from core.Application import Application
from core.response.ResponseInterface import ResponseInterface
from core.decorators.response import sender


class Response(ResponseInterface):

    _handler: SimpleHTTPRequestHandler
    _status_code: int
    _headers: Dict
    _content: str

    def __init__(self, request_handler: SimpleHTTPRequestHandler):
        self.set_handler(request_handler)
        self.set_status_code(200)
        self.set_headers({})
        self.set_header('content-type', 'application/json')

    @property
    def handler(self):
        return self._handler
    
    def set_handler(self, value):
        self._handler = value

    def status_code(self):
        return self._status_code

    def set_status_code(self, value: int):
        self._status_code = value

    def headers(self):
        return self._headers

    def set_headers(self, values: Dict):
        self._headers = values

    def header(self, key: str):
        return self._headers.get(key)

    def set_header(self, key: str, value: str):
        self._headers[key] = value

    def content(self):
        return self._content

    def set_content(self, value: str):
        self._content = value

    def send(self, content):
        return json.dumps(content)

    @sender
    def error(self, message):
        return dict({
            "status": Application.STATUS_FAILED,
            "message": message
        })
        