from abc import ABC, abstractmethod
from typing import List

class SongsJsonManipulationInterface(ABC):
    @abstractmethod
    def __init__(self, paths : List[str], absolute_path : str) -> None:
        """Init

        Args:
            paths (List[str]): Paths to original songs
            absolute_path (str): Absolute path to application
        """        
        raise NotImplementedError()

    @abstractmethod
    def add_songs(self) -> None:
        """Copy songs to songs directory

        """        
        raise NotImplementedError()
