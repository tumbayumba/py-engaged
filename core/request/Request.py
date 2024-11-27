from core.helpers.json import Json
from urllib.parse import urlparse, parse_qs
from email.message import Message
from http.server import SimpleHTTPRequestHandler
from typing import Dict, Type
from urllib.parse import ParseResult
from core.request.RequestInterface import RequestInterface


class Request(RequestInterface):

    _method: str
    _headers: Message
    _host: str
    _url: ParseResult
    _body: str
    _query_params: Dict

    def __init__(self, request_handler):
        # Set the HTTP method (e.g., GET, POST, etc.)
        self.set_method(request_handler["method"])
        # Get headers from the request
        headers = request_handler['headers']
        self.set_headers(headers)
        # Set the Host header
        host_header = next((value.decode() for key, value in headers if key == b'host'), None)
        self.set_host(host_header)
        # Parse and set the requested URL
        self.set_url(urlparse(request_handler["path"]))
        self.set_params(parse_qs(request_handler["query_string"]))
        self.set_body(request_handler["request_body"])

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

    def set_headers(self, values: Message):
        self._headers = values

    def header(self, key: str):
        key_bytes = key.encode('utf-8')  # Convert key to bytes
        for header_key, header_value in self.headers():
            if header_key == key_bytes:
                return header_value.decode('utf-8')  # Convert bytes to string
        return None  # Return None if the key is not found

    def set_header(self, key: str, value: str):
        self._headers[key] = value

    def url(self):
        return self._url

    def set_url(self, value: ParseResult):
        self._url = value

    def body(self):
        return Json.decode(self._body)

    def set_body(self, value: str):
        self._body = value

    def params(self):
        return self._query_params
    
    def param(self, name: str):
        try:
            return self._query_params.get(name)
        except TypeError as e: 
            return None

    def set_params(self, data: Dict):
        params = {key.decode(): value[0].decode() for key, value in data.items()}
        self._query_params = params

    def add_param(self, key: str, value: str):
        self._query_params.set(key, value)

