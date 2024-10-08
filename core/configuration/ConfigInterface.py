from abc import ABC, abstractmethod

class ConfigInterface(ABC):

    """
    Returns full list of configs
    """
    @abstractmethod
    def data(self):
        raise NotImplementedError

    @abstractmethod
    def set_data(self, value):
        raise NotImplementedError

    @abstractmethod
    def get(self, key: str):
        raise NotImplementedError

    @abstractmethod
    def set(self, key: str, value):
        raise NotImplementedError
