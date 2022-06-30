from abc import ABC, abstractmethod
from typing import Type, List
from PySide6.QtWidgets import QGridLayout

class CardSongInterface(ABC):
    @abstractmethod
    def __init__(self, id : int, song_name : str, short_cuts : List[str]) \
        -> None:
        """Init

        """        
        raise NotImplementedError()

    @abstractmethod
    def create_card_song(self) -> Type[QGridLayout]:
        """Create card song

        Returns:
            Type[QGridLayout]: Grind Layout contain a card song
        """        
        raise NotImplementedError()