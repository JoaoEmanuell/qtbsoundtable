from typing import Type, List
from pathlib import Path
from os.path import join, exists

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, \
    QHBoxLayout, QScrollArea
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

from source import Factory
from source.factory.interfaces import FactoryInterface
from source.songs_json_manipulation.interfaces import SongsJsonManipulationInterface
from source.card_song.interfaces import CardSongInterface

class App():
    def __init__(self, factory : Type[FactoryInterface]) -> None:
        self.__app = QApplication([])
        self.__factory = factory()
        self.__absolute_path = Path().absolute()

        # Add form

        self.__add_form = self.load_ui('add_songs.ui')
        self.__add_form.addSongsButton.clicked.connect(self.__add_songs)

        # Main form

        self.__main_form = self.load_ui('main.ui')
        self.__main_form.playSongsButton.clicked.connect(self.play_song)
        self.__main_form.actionAddSounds.triggered.connect(self.__add_songs)

        if not exists(join(self.__absolute_path, 'songs.json')):
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

        get_songs_class : SongsJsonManipulationInterface = \
            self.__factory.get_representative(SongsJsonManipulationInterface)(
                [], 
                self.__absolute_path
            )

        songs = (*get_songs_class.get_songs(), )

        for i, song in enumerate(songs):

            card_song_class : CardSongInterface = \
                self.__factory.get_representative(CardSongInterface)(
                    id = song[0], 
                    song_name = song[1],
                    short_cuts = ['1', '2', '3', '4', '5'],
                    window = scroll_area_widget
                )

            card = card_song_class.create_card_song()

            card_widget = QWidget()

            card_widget.setLayout(card)

            horizontal_layout.addWidget(card_widget)

            if ((i + 1) % 3) == 0: # 3 cards per row

                horizontal_layout_widget = QWidget()

                horizontal_layout_widget.setLayout(horizontal_layout)

                box_layout.addWidget(horizontal_layout_widget)

                horizontal_layout = QHBoxLayout()

        horizontal_layout_widget = QWidget()

        horizontal_layout_widget.setLayout(horizontal_layout)

        box_layout.addWidget(horizontal_layout_widget)

    def play_song(self) -> None:
        pass

if __name__ == '__main__':
    App(Factory)