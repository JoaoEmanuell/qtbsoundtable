from abc import ABC, abstractmethod
from typing import Type, List
from PySide6.QtWidgets import QFrame, QMainWindow, QPushButton, QComboBox

from ...songs_configure.interfaces import SongsConfigureInterface

class CardSongInterface(ABC):
    @abstractmethod
    def __init__(self, id : int, song_name : str, \
        short_cuts : List[str], window : Type[QMainWindow],
        play_song: Type[SongsConfigureInterface],
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

    @abstractmethod
    def play_sound_event_button(self, id:str, button:Type[QPushButton], 
        combo_box: Type[QComboBox]) \
        -> None:
        """Play sound event button
        
        Args:
            id (str): Id of song
            button (Type[QPushButton]): Button to play song
            combo_box (Type[QComboBox]): Combo box to select short cut
        """        
        raise NotImplementedError()