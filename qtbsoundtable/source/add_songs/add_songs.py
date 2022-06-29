from typing import List
from shutil import copy
from os import mkdir
from os.path import exists, join
from json import load, dumps
from json.decoder import JSONDecodeError

from .interfaces import AddSongsInterface

class AddSongs(AddSongsInterface):
    def __init__(self, paths: List[str], absolute_path: str) -> None:
        self.__paths = (*paths, )
        self.__absolute_path = absolute_path

    def add_songs(self) -> None:

        path = join(self.__absolute_path, 'songs', '')
        json_path = join(self.__absolute_path, 'songs.json')

        if not exists(path):
            mkdir(path)

        if not exists(json_path):
            open(json_path, 'w').close()

        songs_to_add : List[List[str]] = []
        
        for song in self.__paths:
            copy(song, path)
            songs_to_add.append(
                [
                    song.split('/')[-1], # Name
                    '', # Shortcut
                    False # Loop
                ]
            )

        self.private__write_json(json_path, songs_to_add)

    def private__write_json(
        self, 
        json_path : str, 
        songs_to_add : List[List[str]]) -> None:

        with open(json_path, 'r') as f:
            try :
                original_json : dict = load(f)
            except JSONDecodeError:
                original_json = {'songs': []}

        with open(json_path, 'w') as f:

            original_songs : List[
                List[str, str, bool]
            ] = original_json['songs']

            for song in songs_to_add:

                original_songs.append(song)

            new_json = {
                'songs': original_songs
            }

            f.write('')

            f.write(dumps(new_json))
