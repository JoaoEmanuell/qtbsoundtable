from json import load
from sys import path
from pathlib import Path
from os.path import join
from typing import List
path.append('../')
from qtbsoundtable.source import Factory
from qtbsoundtable.source.songs_json_manipulation.interfaces \
    import SongsJsonManipulationInterface

def test_answer():
    fac = Factory()
    absolute_path = Path().absolute()
    add_songs : SongsJsonManipulationInterface = fac.get_representative(SongsJsonManipulationInterface)(
        [join(absolute_path, 'tmp.mp3')], 
        absolute_path
    )
    add_songs.add_songs()
    
    json = add_songs.get_songs()
    assert type(json) == list
    assert json[0][0] == 0