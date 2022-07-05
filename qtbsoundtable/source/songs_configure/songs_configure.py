from os.path import exists, join
from typing import Type

from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio
from simpleaudio import PlayObject

from .interfaces import SongsConfigureInterface
from ..songs_json_manipulation.interfaces import SongsJsonManipulationInterface

class SongsConfigure(SongsConfigureInterface):
    def __init__(
        self, 
        absolute_path: str, 
        songs_json_manipulation: \
            Type[SongsJsonManipulationInterface]) -> None:

        self.__absolute_path = absolute_path
        self.__songs_json_manipulation = songs_json_manipulation
        self.__song_thread : PlayObject = PlayObject

    def play_song(self, id: int, loop: bool) -> None:
        if not exists(join(self.__absolute_path, 'songs.json')):
            raise FileNotFoundError()

        song : str = self.__songs_json_manipulation.get_song(id)

        song_to_play = AudioSegment.from_file(song)

        self.__song_thread = _play_with_simpleaudio(song_to_play)
        print(f"Playing song: {song}")

    def stop_song(self) -> None:
        try :
            self.__song_thread.stop()
        except RuntimeError:
            pass
        self.__song_thread = PlayObject