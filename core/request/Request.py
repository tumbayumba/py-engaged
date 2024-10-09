import email
import urllib.parse
from http.server import BaseHTTPRequestHandler
from typing import Dict
from urllib.parse import ParseResult

from core.request.RequestInterface import RequestInterface


class Request(RequestInterface):

    _method: str
    _headers: email.message.Message
    _host: str
    _url: ParseResult
    _body: str

    def __init__(self, request_handler: BaseHTTPRequestHandler):
        self.set_method(request_handler.command)
        headers = request_handler.headers
        self.set_headers(headers)
        self.set_host(headers.get('Host'))
        self.set_url(urllib.parse.urlparse(request_handler.path))
        # parse body content
        content_length = int(headers['Content-Length'])
        body = request_handler.rfile.read(content_length)
        content = body.decode('utf-8')
        self.set_body(content)

    def method(self):
        return self._method

    def set_method(self, value: str):
        self._method = value

    def host(self):
        return self._host

    def set_host(self, value: str):
        self._host = value

    def headers(self):
        return self._headers

    def set_headers(self, values: email.message.Message):
        self._headers = values

    def header(self, key: str):
        return self.headers().get(key)

    def set_header(self, key: str, value: str):
        self._headers[key] = value

    def url(self):
        return self._url

    def set_url(self, value: ParseResult):
        self._url = value

    def body(self):
        return self._body

    def set_body(self, value: str):
        self._body = value

