import email
import urllib.parse
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

    def __init__(self, request_handler: SimpleHTTPRequestHandler):
        # Set the HTTP method (e.g., GET, POST, etc.)
        self.set_method(request_handler.command)
        # Get headers from the request
        headers = request_handler.headers
        self.set_headers(headers)
        # Set the Host header
        self.set_host(headers.get('Host'))
        # Parse and set the requested URL
        self.set_url(urllib.parse.urlparse(request_handler.path))

        # Parse the request body content if 'Content-Length' is present
        content_length = headers.get('Content-Length')
        if content_length:
            try:
                content_length = int(content_length)
                body = request_handler.rfile.read(content_length)
                content = body.decode('utf-8')
                self.set_body(content)
            except (ValueError, TypeError) as e:
                # Handle cases where Content-Length is invalid or parsing fails
                print(f"Error reading body content: {e}")
                self.set_body("")
        else:
            # Set empty body if Content-Length is not provided
            self.set_body("")

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

