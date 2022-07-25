from typing import Type, List
from pathlib import Path
from os.path import join, exists
from json import load
from json.decoder import JSONDecodeError

from PySide6.QtWidgets import (QApplication, QWidget, QFileDialog, 
QHBoxLayout, QScrollArea, QPushButton)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from pydub import AudioSegment
from pydub.playback import play

from source import Factory

from source.factory import FactoryInterface
from source.songs_json_manipulation import SongsJsonManipulationInterface
from source.card_song import CardSongInterface
from source.songs_configure import SongsConfigureInterface
from source.multi_thread import MultiThreadInterface

class App():
    def __init__(self, factory: Type[FactoryInterface]) -> None:
        
        self.__app = QApplication([])
        self.__factory = factory()
        self.__absolute_path = Path().absolute()

        # Add form

        self.__add_form = self.load_ui('add_songs.ui')
        self.__add_form.addSongsButton.clicked.connect(self.__add_songs)

        # Main form

        self.__main_form = self.load_ui('main.ui')
        self.__main_form.playSongsButton.clicked.connect(
            lambda: self.play_song_button(self.__main_form.playSongsButton)
        )
        self.__main_form.actionAddSounds.triggered.connect(self.__add_songs)

        # Class

        # Multi Thread

        self.__multi_thread : MultiThreadInterface = \
            self.__factory.get_representative(MultiThreadInterface)

        # Get songs

        self.__get_songs_class : SongsJsonManipulationInterface = \
            self.__factory.get_representative(SongsJsonManipulationInterface)(
                [], 
                self.__absolute_path
            )

        # Play song

        self.__play_song_class : SongsConfigureInterface = \
            self.__factory.get_representative(SongsConfigureInterface)(
                self.__absolute_path,
                self.__get_songs_class,
                self.__multi_thread
            )

        # Variables
        self.__play_songs_thread_id : int = self.__multi_thread.create_thread(
            self.__play_songs,
            (self.__get_songs_class, ),
            automatic_start=False
        )

        if not self.__verify_songs_json():
            self.__add_form.show()
        else:
            self.load_songs_in_screen()
        
        self.__app.exec()

    def load_ui(self, ui_file : str) -> Type[QWidget]:
        path = join(self.__absolute_path, "layouts", "")
        ui_file = QFile(f'{path}{ui_file}')
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        ui = loader.load(ui_file)
        return ui

    def __add_songs(self) -> None:
        paths : List[str] = QFileDialog.getOpenFileNames(
            filter = "Music Files (*.mp3 *.wav)",
        )[0]

        add_songs_class : SongsJsonManipulationInterface = self.__factory.get_representative(
            SongsJsonManipulationInterface
        )(paths, self.__absolute_path)

        add_songs_class.add_songs()

        self.__add_form.close()

        self.load_songs_in_screen()

    def load_songs_in_screen(self) -> None:
        self.__main_form.show()

        scroll_area : QScrollArea = self.__main_form.scrollArea

        scroll_area_widget = scroll_area.widget()

        box_layout = scroll_area_widget.layout()

        horizontal_layout = QHBoxLayout()

        songs = (*self.__get_songs_class.get_songs(), )

        for i, song in enumerate(songs):

            card_song_class : CardSongInterface = \
                self.__factory.get_representative(CardSongInterface)(
                    id = song[0], 
                    song_name = song[1],
                    short_cuts = ['1', '2', '3', '4', '5'],
                    window = scroll_area_widget,
                    play_song = self.__play_song_class
                )

            card = card_song_class.create_card_song()

            horizontal_layout.addWidget(card)

            if ((i + 1) % 3) == 0: # 3 cards per row

                box_layout.addWidget(self.__add_layout(horizontal_layout))
                horizontal_layout = QHBoxLayout()

        box_layout.addWidget(self.__add_layout(horizontal_layout))

    def __add_layout(self, horizontal_layout : Type[QHBoxLayout]) \
        -> Type[QWidget]:
        # Return : QWidget is a widget containing the horizontal layout
        
        horizontal_layout_widget = QWidget()
        horizontal_layout_widget.setLayout(horizontal_layout)
        return horizontal_layout_widget

    def play_song_button(self, button: Type[QPushButton]) -> None:
        button_text = button.text()

        if button_text == 'Tocar sons':

            self.__multi_thread.start_thread(self.__play_songs_thread_id)

            button.setText('Parar sons')

        else:

            self.__multi_thread.stop_thread(self.__play_songs_thread_id)

            button.setText('Tocar sons')

    def __play_songs(self, songs_json: Type[SongsJsonManipulationInterface]) \
        -> None:
        # Play all songs in songs.json
        songs = songs_json.get_songs()
        for song in songs:
            file = AudioSegment.from_file(
                songs_json.get_song(song[0]) # Get the absolute path
            )
            play(file)

    def __verify_songs_json(self) -> bool:
        # Verify songs json integrity
        # If integrity return True, else return False
        songs_json_path = join(self.__absolute_path, 'songs.json')

        if exists(songs_json_path):
            try:
                with open(songs_json_path, 'r') as file:
                    json = load(file)
                    json['songs']
                    return True
            except (JSONDecodeError, KeyError):
                return False
        else:
            return False

if __name__ == '__main__':
    App(Factory)