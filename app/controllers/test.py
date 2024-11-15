from dataclasses import dataclass
from core.controller.BaseController import BaseController


class TestController(BaseController):

    """
    GET action example
    """
    def index(self):
        try:
            # params = self.app.request.params()
            name = self.app.request.param('name')
            age = self.app.request.param('age')
            info = f'{name}: {age}'

            return self.app.response.send(dict({
                "status": self.app.STATUS_OK,
                "data": {
                    "info": info
                }
            }));
        except Exception as e:
            self.app.response.set_status_code(400)
            return self.app.response.error(str(e))
        

    """
    POST action example
    """
    def other(self):
        try:
            data  = self.app.request.body()
            phone = data.get("info").get("phone")

            return self.app.response.send(dict({
                    "status": self.app.STATUS_OK,
                    "data": {
                        "info": phone
                    }
                }))
        except Exception as e:
            self.app.response.set_status_code(400)
            return self.app.response.error(str(e))
        