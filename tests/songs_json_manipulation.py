from sys import path
from pathlib import Path
from os.path import join
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

    add_songs.set_short_cut('0', 'Ctrl+1')
    song_short_cut = add_songs.get_short_cut('0')
    assert song_short_cut == 'Ctrl+1'

if __name__ == '__main__':
    test_answer()