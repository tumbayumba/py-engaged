from core.Application import Application
from core.controller.Controller import Controller


class BaseController(Controller):
    
    @property
    def app(self): 
        return Application.get_instance();



