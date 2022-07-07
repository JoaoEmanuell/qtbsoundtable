from typing import Tuple, Type
from abc import ABC

from .interfaces import FactoryInterface
from ..songs_json_manipulation import SongsJsonManipulation
from ..card_song import CardSong
from ..songs_configure import SongsConfigure
from ..multi_thread import MultiThreadClass

class Factory(FactoryInterface):
    def __init__(self) -> None:
        self.__representatives : Tuple[ABC] = (
            SongsJsonManipulation,
            CardSong,
            SongsConfigure,
            MultiThreadClass,
        )

    def get_representative(self, interface: Type[ABC]) -> Type[ABC]:
        for representative in self.__representatives:
            if issubclass(representative, interface):
                return representative
        raise ValueError(f"No representative found for interface: {interface}")