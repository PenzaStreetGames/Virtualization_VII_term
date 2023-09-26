from abc import ABC, abstractmethod
from typing import Optional


class DatabasePort(ABC):
    @abstractmethod
    def _connect(self):
        raise NotImplementedError

    @abstractmethod
    def _disconnect(self):
        raise NotImplementedError

    @abstractmethod
    def find_all(self, table_name):
        raise NotImplementedError

    # @abstractmethod
    # def find_by_id(self, table_name, id):
    #     raise NotImplementedError
    #
    # @abstractmethod
    # def find_by_param(self, table_name, param, value):
    #     raise NotImplementedError

    @abstractmethod
    def create(self, table_name, data):
        raise NotImplementedError

    # @abstractmethod
    # def update(self, table_name, id, data):
    #     raise NotImplementedError
    #
    # @abstractmethod
    # def delete(self, table_name, id):
    #     raise NotImplementedError
