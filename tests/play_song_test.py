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
from qtbsoundtable.source.multi_thread import MultiThreadInterface

def test_answer():
    fac = Factory()
    absolute_path = join(Path().absolute(), '')
    
    songs_json_manipulation : SongsJsonManipulationInterface = \
        fac.get_representative(SongsJsonManipulationInterface)(
            absolute_path = absolute_path
        )

    multi_thread : MultiThreadInterface \
        = fac.get_representative(MultiThreadInterface)

    songs_configure_class : SongsConfigureInterface = \
        fac.get_representative(SongsConfigureInterface)(
            absolute_path = absolute_path,
            songs_json_manipulation = songs_json_manipulation,
            thread_manipulation = multi_thread
        )


    thread_id = songs_configure_class.play_song(id=0, loop=False)
    print(thread_id)
    stop_song(songs_configure_class, time=10, thread_id=thread_id)

def stop_song(songs_configure : Type[SongsConfigureInterface], time : int = 5, thread_id: int=0):
    sleep(time)
    print("Stope song thread!")
    songs_configure.stop_song(thread_id)
    print("Stop song!")

if __name__ == '__main__':
    test_answer()