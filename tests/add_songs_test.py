from json import load
from sys import path
from pathlib import Path
from os.path import join
from typing import List
path.append('../')
from qtbsoundtable.source import Factory
from qtbsoundtable.source.add_songs.interfaces import AddSongsInterface

def test_answer():
    fac = Factory()
    absolute_path = Path().absolute()
    add_songs : AddSongsInterface = fac.get_representative(AddSongsInterface)(
        [join(absolute_path, 'tmp.mp3')], 
        absolute_path
    )
    add_songs.add_songs()
    with open(join(absolute_path, 'songs.json'), 'r') as f:
        json : dict = load(f)
        songs : List[List[str]] = json["songs"]

        assert type(songs[0]) == list
        assert type(songs[0][0]) == int
        assert type(songs[0][1]) == str
        assert type(songs[0][2]) == str
        assert type(songs[0][3]) == bool