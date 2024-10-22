from abc import ABC, abstractmethod

class Calculator(ABC):
    
    @abstractmethod
    def compute(self, a, b):
        pass
