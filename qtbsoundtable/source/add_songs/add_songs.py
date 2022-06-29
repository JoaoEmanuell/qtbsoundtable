from typing import List
from shutil import copy
from os import mkdir
from os.path import exists, join

from .interfaces import AddSongsInterface

class AddSongs(AddSongsInterface):
    def __init__(self, paths: List[str], absolute_path: str) -> None:
        self.__paths = (*paths, )
        self.__absolute_path = absolute_path

    def add_songs(self) -> None:

        path = join(self.__absolute_path, 'songs', '')

        if not exists(path):
            mkdir(path)
        
        for song in self.__paths:
            copy(song, path)