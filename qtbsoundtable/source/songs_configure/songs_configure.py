from os.path import exists, join
from typing import Type

from pydub import AudioSegment
from pydub.playback import play

from .interfaces import SongsConfigureInterface
from ..songs_json_manipulation.interfaces import SongsJsonManipulationInterface
from ..multi_thread import MultiThreadInterface

class SongsConfigure(SongsConfigureInterface):
    def __init__(
        self, 
        absolute_path: str, 
        songs_json_manipulation: \
            Type[SongsJsonManipulationInterface],
        thread_manipulation : Type[MultiThreadInterface]) -> None:

        self.__absolute_path = absolute_path
        self.__songs_json_manipulation = songs_json_manipulation
        self.__multi_thread : MultiThreadInterface = thread_manipulation

    def play_song(self, id: int=0, loop: bool=False) -> int:
        if not exists(join(self.__absolute_path, 'songs.json')):
            raise FileNotFoundError()

        song : str = self.__songs_json_manipulation.get_song(id)

        song_to_play = AudioSegment.from_file(song)

        thread_id = self.__multi_thread.create_thread(
            target=play, 
            args=(song_to_play,)
        )

        print(f"Playing song: {song}")
        return thread_id

    def stop_song(self, thread_id: int=0) -> None:
        self.__multi_thread.delete_thread(thread_id)