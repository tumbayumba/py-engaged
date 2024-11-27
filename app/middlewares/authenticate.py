from core.middlewares.middleware import Middleware
from core.request.RequestInterface import RequestInterface


class Authenticate(Middleware):
    
    def handle(self, request: RequestInterface):
        # print(f'auth token: {request.header("authorization-token")}')

        """
        Uncomment the code below for negative result
        """
        # self.app.response.set_status_code(401)
        # return self.app.response.error("Unauthorized")

        return True
        