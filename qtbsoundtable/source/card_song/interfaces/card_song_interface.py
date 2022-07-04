from abc import ABC, abstractmethod
from typing import Type, List
from PySide6.QtWidgets import QFrame, QMainWindow

from ...songs_configure.interfaces import SongsConfigureInterface
from ...songs_json_manipulation.interfaces import SongsJsonManipulationInterface

class CardSongInterface(ABC):
    @abstractmethod
    def __init__(self, id : int, song_name : str, \
        short_cuts : List[str], window : Type[QMainWindow],
        absolute_path: str,
        play_song: Type[SongsConfigureInterface],
        songs_json_manipulation: Type[SongsJsonManipulationInterface]
        ) -> None:
        """Init

        """        
        raise NotImplementedError()

    @abstractmethod
    def create_card_song(self) -> Type[QFrame]:
        """Create card song

        Returns:
            Type[QGridLayout]: Grind Layout contain a card song
        """        
        raise NotImplementedError()