from core.Application import Application
from core.configuration.Config import Config
from core.request.Request import Request
from core.response.Response import Response
from core.routing.Router import Router


async def app(scope, receive, send):
    """
    Echo the method and path back in an HTTP response.
    """
    assert scope['type'] == 'http'

    body_text = ""
    if scope["type"] == "http":
        # Initialize an empty body
        request_body = b""

        # Continuously receive the body in chunks
        while True:
            message = await receive()
            if message["type"] == "http.request":
                request_body += message.get("body", b"")
                if not message.get("more_body"):
                    break

        # Decode the body if it's text or JSON
        body_text = request_body.decode("utf-8")
    scope["request_body"] = body_text

    app = Application.get_instance()
    app.set_config(Config())
    app.set_handler(scope)
    app.set_request(Request(scope))
    app.set_router(Router(app.config.get('routes')))
    app.set_response(Response(scope))
    body = app.run()

    await send({
        'type': 'http.response.start',
        'status': app.response.status_code(),
        'headers': [
            [b'content-type', app.response.header('content-type')],
        ]
    })
    await send({
        'type': 'http.response.body',
        'body': body.encode('utf-8'),
    })