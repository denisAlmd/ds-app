from abc import ABC, abstractmethod

class BasePage(ABC):
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def get_name(self):
        raise NotImplementedError("Subclasses must implement name method")
    
    @abstractmethod
    def get_description(self):
        raise NotImplementedError("Subclasses must implement description method")
    
    @abstractmethod
    def render(self):
        raise NotImplementedError("Subclasses must implement render method")