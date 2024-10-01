import email
from abc import ABC, abstractmethod
from typing import Dict


class RequestInterface(ABC):

    @abstractmethod
    def method(self):
        raise NotImplementedError

    @abstractmethod
    def set_method(self, value: str):
        raise NotImplementedError

    @abstractmethod
    def host(self):
        raise NotImplementedError

    @abstractmethod
    def set_host(self, value: str):
        raise NotImplementedError

    @abstractmethod
    def headers(self):
        raise NotImplementedError

    @abstractmethod
    def set_headers(self, values: email.message.Message):
        raise NotImplementedError

    @abstractmethod
    def header(self, key: str):
        raise NotImplementedError

    @abstractmethod
    def set_header(self, key: str, value: str):
        raise NotImplementedError

    @abstractmethod
    def path(self):
        raise NotImplementedError

    @abstractmethod
    def set_path(self, value: str):
        raise NotImplementedError
