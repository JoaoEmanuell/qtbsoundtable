from abc import ABC, abstractmethod
from typing import List, Union

class SongsJsonManipulationInterface(ABC):
    @abstractmethod
    def __init__(self, paths: List[str]=[], absolute_path: str='') -> None:
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

    @abstractmethod
    def get_songs(self) -> List[List[Union[int, str, bool]]]:
        """Get songs from songs.json

        Raises:
            FileNotFoundError: Case songs.json don't exist

        Returns:
            List[List[Union[int, str, bool]]]: Songs from songs.json
        """         
        raise NotImplementedError()
        raise FileNotFoundError()

    @abstractmethod
    def get_song(self, id: str) -> str:
        """Get song

        Args:
            id (str): Id from song, get this information in songs.json

        Raises:
            FileNotFoundError: Case the song not exists

        Returns:
            str: Absolute path to the song
        """        
        raise NotImplementedError()
        raise FileNotFoundError()

    @abstractmethod
    def set_short_cut(self, id: str) -> None:
        """Set shortcut the song

        Args:
            id (str): Id from song, get this information in songs.json

        Raises:
            FileNotFoundError: Case the song not exists
        """        
        raise NotImplementedError()
        raise FileNotFoundError()

    @abstractmethod
    def get_short_cut(self, id: str) -> str:
        """Get shortcut of the song

        Args:
            id (str): Id from song, get this information in songs.json

        Raises:
            FileNotFoundError: Case the song not exists

        Returns:
            str: Actual shortcut of the song
        """        
        raise NotImplementedError()
        raise FileNotFoundError()