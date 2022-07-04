from threading import Thread
from os.path import exists, join
from typing import Type

from playsound import playsound

from .interfaces import SongsConfigureInterface
from ..songs_json_manipulation.interfaces import SongsJsonManipulationInterface

class SongsConfigure(SongsConfigureInterface):
    def __init__(
        self, 
        absolute_path: str, 
        songs_json_manipulation: \
            Type[SongsJsonManipulationInterface]) -> None:

        self.__absolute_path = absolute_path
        self.__songs_json_manipulation = \
            songs_json_manipulation(absolute_path=absolute_path)
        self.__main_thread : Thread = Thread()

    def play_song(self, id: int, loop: bool) -> None:
        if not exists(join(self.__absolute_path, 'songs.json')):
            raise FileNotFoundError()

        song = self.__songs_json_manipulation.get_song(id)

        self.__main_thread = Thread(target=playsound, args=(song,))
        self.__main_thread.start()

    def stop_song(self) -> None:
        self.__main_thread.join()
        self.__main_thread = Thread()