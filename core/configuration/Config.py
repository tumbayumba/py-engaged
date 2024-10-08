from core.configuration.ConfigInterface import ConfigInterface
from app.config import config
from typing import Dict


class Config(ConfigInterface):

    __config_data: Dict[str, Dict[str, str]]

    def __init__(self):
        self.set_data(config)

    def data(self):
        return self.__config_data

    def set_data(self, value):
        self.__config_data = value

    def get(self, key: str):
        return self.__config_data.get(key) if key in self.__config_data else None

    def set(self, key: str, value):
        self.__config_data[key] = value

