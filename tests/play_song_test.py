from sys import path
from pathlib import Path
from os.path import join
from time import sleep
from threading import Thread
from typing import Type
path.append('../')

from qtbsoundtable.source import Factory
from qtbsoundtable.source.songs_json_manipulation.interfaces import (
    SongsJsonManipulationInterface
)
from qtbsoundtable.source.songs_configure.interfaces import (
    SongsConfigureInterface
)

def test_answer():
    fac = Factory()
    absolute_path = join(Path().absolute(), '')
    
    songs_json_manipulation : SongsJsonManipulationInterface = \
        fac.get_representative(SongsJsonManipulationInterface)(
            absolute_path = absolute_path
        )

    songs_configure_class : SongsConfigureInterface = \
        fac.get_representative(SongsConfigureInterface)(
            absolute_path = absolute_path,
            songs_json_manipulation = songs_json_manipulation
        )

    Thread(target=stop_song, args=(songs_configure_class, 3)).start()

    songs_configure_class.play_song(id=0, loop=False)

def stop_song(songs_configure : Type[SongsConfigureInterface], time : int = 5):
    sleep(time)
    print("Stope song thread!")
    songs_configure.stop_song()
    print("Stop song!")

if __name__ == '__main__':
    test_answer()