from abc import ABC, abstractmethod
from typing import List

class SongsConfigureInterface(ABC):
    """Songs configure, get all songs from json, play song."""    
    @abstractmethod
    def __init__(self, absolute_path: str) -> None:
        """Init

        Args:
            absolute_path (str): Absolute path to app.py, to locate a songs.json

        """        
        raise NotImplementedError()
        
    @abstractmethod
    def get_all_songs(self) -> List[List[str]]:
        """Get all songs from songs.json

        Raises:
            FileNotFoundError: Case the songs.json file does not exist

        Returns:
            List[List[str]]: Data matrix of all songs, format : [Id, Name, Shortcut, Loop]
        """        
        raise NotImplementedError()
        raise FileNotFoundError()

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