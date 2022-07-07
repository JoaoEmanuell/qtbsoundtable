from abc import ABC, abstractmethod

class MultiThreadErrorInterface(ABC):
    """Muti Thread Error is a class responsible for issuing erros related of the MultiThreadError class

    """    
    @abstractmethod
    def __init__(self, message:str='Multi Thread Error') -> None:
        """Init

        Args:
            message (str, optional): Error message. Defaults to 'Multi Thread Error'.

        """        
        raise NotImplementedError()