from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse  # For parsing query strings
import json  # For parsing JSON data in POST requests
import application
from application import Application


# Define a request handler class
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def _handle_request(self):
        Application.run(self)

    # Override do_* methods to point to _handle_request
    def do_GET(self):
        self._handle_request()

    def do_POST(self):
        self._handle_request()

    def do_PUT(self):
        self._handle_request()

    def do_PATCH(self):
        self._handle_request()

    def do_DELETE(self):
        self._handle_request()

# Define server details
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}')
    httpd.serve_forever()

# Run the server
if __name__ == "__main__":
    run()