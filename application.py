from http.server import BaseHTTPRequestHandler
import urllib.parse

class Application:

    @staticmethod
    def run(handler: BaseHTTPRequestHandler):
        method = handler.command
        path = handler.path
        request_version = handler.request_version
        parsed_path = urllib.parse.urlparse(path)
        query_params = urllib.parse.parse_qs(parsed_path.query)
        headers = handler.headers

        print(f'Method: {method}')
        print(f'Path: {path}')
        print(f'Request Version: {request_version}')
        print(f'Parsed Path: {parsed_path}')
        print(f'Query Params: {query_params}')
        # print(f'Headers:\n {headers}')

        # Send common response headers
        handler.send_response(200)
        handler.send_header('Content-type', 'application/json')
        handler.end_headers()

        # Handle different methods
        match method:
            case 'GET':
                handler.wfile.write(b'Handled GET request')
            case 'POST':
                handler.wfile.write(b'Handled POST request')
            case 'PUT':
                handler.wfile.write(b'Handled PUT request')
            case 'PATCH':
                handler.wfile.write(b'Handled PATCH request')
            case 'DELETE':
                handler.wfile.write(b'Handled DELETE request')
            case _:
                handler.wfile.write(b'Unhandled HTTP method')
