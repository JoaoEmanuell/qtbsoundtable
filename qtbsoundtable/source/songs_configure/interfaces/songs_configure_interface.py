from abc import ABC, abstractmethod
from typing import Type

from ...songs_json_manipulation.interfaces import SongsJsonManipulationInterface
from ...multi_thread import MultiThreadInterface

class SongsConfigureInterface(ABC):
    """Songs configure, play song."""    
    @abstractmethod
    def __init__(
        self, 
        absolute_path: str, 
        songs_json_manipulation : Type[SongsJsonManipulationInterface],
        thread_manipulation : Type[MultiThreadInterface]
        ) -> None:
        """Init

        Args:
            absolute_path (str): Absolute path to app.py, to locate a songs.json
            songs_json_manipulation(Type[SongsJsonManipulationInterface]): Songs json manipulation
            thread_manipulation(Type[MultiThreadInterface]): Thread manipulation

        """        
        raise NotImplementedError()

    @abstractmethod
    def play_song(self, id: int=0, loop: bool=False) -> int:
        """Play a song

        Args:
            id (int): Id locate in songs.json
            loop (bool): If true this song will be looped

        Raises:
            FileNotFoundError: Case the song does not exist

        Returns:
            int: Thread Id, provide by MultiThread
        """            
        raise NotImplementedError()
        raise FileNotFoundError()

    @abstractmethod
    def stop_song(self, thread_id: int=0) -> None:
        """Stop a song

        Args:
            thread_id (int): Thread id provide by play_song

        """        
        raise NotImplementedError()