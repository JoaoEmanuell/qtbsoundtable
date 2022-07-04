from abc import ABC, abstractmethod
from typing import Type

from ...songs_json_manipulation.interfaces import SongsJsonManipulationInterface

class SongsConfigureInterface(ABC):
    """Songs configure, get all songs from json, play song."""    
    @abstractmethod
    def __init__(
        self, 
        absolute_path: str, 
        songs_json_manipulation : Type[SongsJsonManipulationInterface]
        ) -> None:
        """Init

        Args:
            absolute_path (str): Absolute path to app.py, to locate a songs.json

        """        
        raise NotImplementedError()

    @abstractmethod
    def play_song(self, id: int, loop: bool) -> None:
        """Play a song

        Args:
            id (int): Id locate in songs.json
            loop (bool): If true this song will be looped

        Raises:
            FileNotFoundError: Case the song does not exist
        """        
        raise NotImplementedError()
        raise FileNotFoundError()

    @abstractmethod
    def stop_song(self) -> None:
        """Stop a song"""        
        raise NotImplementedError()