import email
from abc import ABC, abstractmethod
from email.message import Message
from typing import Dict
from urllib.parse import ParseResult


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
    def set_headers(self, values):
        raise NotImplementedError

    @abstractmethod
    def header(self, key: str):
        raise NotImplementedError

    @abstractmethod
    def set_header(self, key: str, value: str):
        raise NotImplementedError

    @abstractmethod
    def url(self):
        raise NotImplementedError

    @abstractmethod
    def set_url(self, value: ParseResult):
        raise NotImplementedError

    @abstractmethod
    def body(self):
        raise NotImplementedError

    @abstractmethod
    def set_body(self, value: str):
        raise NotImplementedError
    
    @abstractmethod
    def params(self):
        raise NotImplementedError
    
    @abstractmethod
    def param(self, name: str):
        raise NotImplementedError

    @abstractmethod
    def set_params(self, params: Dict):
        raise NotImplementedError
    
    @abstractmethod
    def add_param(self, key: str, value: str):
        raise NotImplementedError

