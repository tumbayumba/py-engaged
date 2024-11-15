from core.configuration.ConfigInterface import ConfigInterface
from core.request.RequestInterface import RequestInterface
from core.response.ResponseInterface import ResponseInterface
from core.routing.RouterInterface import RouterInterface


class Application:

    STATUS_OK = 0
    STATUS_FAILED = 1

    __instance = None
    __config: ConfigInterface
    __handler = None
    __request: RequestInterface
    __router: RouterInterface
    __response: ResponseInterface

    @staticmethod
    def get_instance():
        if Application.__instance is None:
            Application.__instance = Application()
        return Application.__instance

    def run(self):
        return self.router.dispatch(self.request)

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

    @property
    def response(self):
        return self.__response

    def set_response(self, value: ResponseInterface):
        if not isinstance(value, ResponseInterface):
            raise ValueError("`response` must be an instance of ResponseInterface")
        self.__response = value
