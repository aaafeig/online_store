from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class BaseOrder(ABC):

    @abstractmethod
    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def __str__(self):
        pass