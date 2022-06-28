from abc import ABC, abstractmethod
from typing import Type

class FactoryInterface(ABC):
    @abstractmethod
    def get_representative(self, interface : Type[ABC]) -> Type[ABC]:
        """Get Representative get a object correspondent to the interface

        Args:
            interface (Type[ABC]): Interface

        Returns:
            Type[ABC]: Class not instantiated
        """        
        raise NotImplementedError()