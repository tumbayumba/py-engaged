from core.controller.BaseController import BaseController


class ErrorController(BaseController):
    
    def error(self, message, http_status_code):
        self.app.response.set_status_code(http_status_code)
        return self.app.response.error(str(message))
            

