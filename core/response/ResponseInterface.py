from abc import ABC, abstractmethod
from typing import Dict


class ResponseInterface(ABC):

    @abstractmethod
    def handler(self):
        raise NotImplementedError

    @abstractmethod
    def set_handler(self, value):
        raise NotImplementedError
    
    @abstractmethod
    def status_code(self):
        raise NotImplementedError

    @abstractmethod
    def set_status_code(self, value: int):
        raise NotImplementedError

    @abstractmethod
    def headers(self):
        raise NotImplementedError

    @abstractmethod
    def set_headers(self, values: Dict):
        raise NotImplementedError
    
    @abstractmethod
    def header(self, key: str):
        raise NotImplementedError

    @abstractmethod
    def set_header(self, key: str, value: str):
        raise NotImplementedError
    
    @abstractmethod
    def content(self):
        raise NotImplementedError

    @abstractmethod
    def set_content(self, value: str):
        raise NotImplementedError

    @abstractmethod
    def send(self, content):
        raise NotImplementedError