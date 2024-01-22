from abc import ABCMeta
from abc import abstractmethod


class Shape:
    __metaclass__ = ABCMeta

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
