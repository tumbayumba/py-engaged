from dataclasses import dataclass

from core.controller.Controller import Controller


class TestController(Controller):

    def index(self):
        print('index')

    def other(self):
        pass