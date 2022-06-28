from abc import ABC, abstractmethod
from typing import List

class AddSongsInterface(ABC):
    @abstractmethod
    def __init__(self, paths : List[str], absolute_path : str) -> None:
        raise NotImplementedError()

    @abstractmethod
    def add_songs(self) -> None:
        raise NotImplementedError()
