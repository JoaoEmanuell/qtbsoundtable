from typing import List, Union, Dict
from shutil import copy
from os import mkdir
from os.path import exists, join
from json import load, dumps
from json.decoder import JSONDecodeError

from .interfaces import SongsJsonManipulationInterface

class SongsJsonManipulation(SongsJsonManipulationInterface):
    def __init__(self, paths: List[str]=[], absolute_path: str='') -> None:
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
        
        id = self.private__get_last_id_json(json_path) + 1

        for song in self.__paths:
            copy(song, path)
            songs_to_add.append(
                [
                    id, # Id
                    song.split('/')[-1], # Name
                    '', # Shortcut
                    False # Loop
                ]
            )
            id += 1

        self.private__write_json(json_path, songs_to_add)

    def private__write_json(
        self, 
        json_path : str, 
        songs_to_add : List[List[str]]) -> None:

        with open(json_path, 'r') as f:
            try:
                original_json : dict = load(f)
            except JSONDecodeError:
                original_json = {'songs': []}

        with open(json_path, 'w') as f:

            original_songs : List[
                List[str]
            ] = original_json['songs']

            for song in songs_to_add:

                original_songs.append(song)

            new_json = {
                'songs': original_songs
            }

            f.write('')

            f.write(dumps(new_json))

    def private__get_last_id_json(self, json_path: str) -> int:
        # Get last id to add id in json
        with open(json_path, 'r') as f:
            try:
                original_json : dict = load(f)
            except JSONDecodeError:
                return -1

            return len(original_json["songs"]) - 1

    def get_songs(self) -> List[List[Union[int, str, bool]]]:
        songs_path = join(self.__absolute_path, 'songs.json')

        if not exists(songs_path):
            raise FileNotFoundError("songs.json not found")

        with open(songs_path, 'r') as file:
            json : Dict[str, List] = load(file)
            return json['songs']

    def get_song(self, id: str) -> str:
        songs = self.get_songs()

        for song in songs:

            if song[0] == int(id):
                song_path = str(join(self.__absolute_path, 'songs', song[1]))

                if not exists(song_path):
                    raise FileNotFoundError("Song not found")

                return song_path