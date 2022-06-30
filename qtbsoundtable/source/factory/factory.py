from typing import Tuple, Type
from abc import ABC

from .interfaces import FactoryInterface
from ..add_songs import AddSongs
from ..card_song import CardSong

class Factory(FactoryInterface):
    def __init__(self) -> None:
        self.__representatives : Tuple[ABC] = (
            AddSongs,
            CardSong,
        )

    def get_representative(self, interface: Type[ABC]) -> Type[ABC]:
        for representative in self.__representatives:
            if issubclass(representative, interface):
                return representative
        raise ValueError(f"No representative found for interface: {interface}")