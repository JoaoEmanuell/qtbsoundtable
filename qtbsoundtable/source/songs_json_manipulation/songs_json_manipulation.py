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
        self.__json_path = join(self.__absolute_path, 'songs.json')

    def add_songs(self) -> None:
        path = join(self.__absolute_path, 'songs', '')

        if not exists(path):
            mkdir(path)

        if not exists(self.__json_path):
            open(self.__json_path, 'w').close()

        songs_to_add : List[List[str]] = []
        
        id = self.private__get_last_id_json() + 1

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

        self.private__write_json(songs_to_add)

    def private__write_json(self, songs_to_add : List[List[str]]) -> None:

        with open(self.__json_path, 'r') as f:
            try:
                original_json : dict = load(f)
            except JSONDecodeError:
                original_json = {'songs': []}

        with open(self.__json_path, 'w') as f:

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

    def private__get_last_id_json(self) -> int:
        # Get last id to add id in json
        with open(self.__json_path, 'r') as f:
            try:
                original_json : dict = load(f)
            except JSONDecodeError:
                return -1

            return len(original_json["songs"]) - 1

    def get_songs(self) -> List[List[Union[int, str, bool]]]:
        if not exists(self.__json_path):
            raise FileNotFoundError("songs.json not found")

        with open(self.__json_path, 'r') as file:
            json : Dict[str, List] = load(file)
            return json['songs']

    def get_song(self, id: str) -> str:
        songs = self.get_songs()
        print(songs)

        for song in songs:
            print(song)

            if song[0] == int(id):
                song_path = str(join(self.__absolute_path, 'songs', song[1]))
                print(song_path)

                if not exists(song_path):
                    raise FileNotFoundError("Song not found")

                return song_path

    def set_short_cut(self, id: str, short_cut: str) -> None:
        songs = self.get_songs()
        
        for pos, song in enumerate(songs):
            if song[0] == int(id):
                song[2] = short_cut
                songs[pos] = song
                self.private__write_short_cut_on_json(songs)
                break

    def private__write_short_cut_on_json(
        self, songs: List[List[Union[int, str, bool]]]) -> None:
        # Write the shortcut in json, use with set_short_cut
        
        with open(self.__json_path, 'w') as file:
            json = {
                'songs': songs
            }
            file.write(dumps(json))
    
    def get_short_cut(self, id: str) -> str:
        songs = self.get_songs()
        
        for song in songs:
            if song[0] == int(id):
                return song[2]