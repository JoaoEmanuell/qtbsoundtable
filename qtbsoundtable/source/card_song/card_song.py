from typing import List, Type
from PySide6.QtWidgets import (QWidget, QGridLayout, QLabel, QPushButton, 
QComboBox, QMainWindow, QFrame)
from PySide6.QtCore import QRect
from PySide6.QtGui import QKeySequence

from .interfaces import CardSongInterface
from ..songs_configure.interfaces import SongsConfigureInterface
from ..songs_json_manipulation.interfaces import SongsJsonManipulationInterface

class CardSong(CardSongInterface):
    def __init__(self, id: int, song_name: str, \
        short_cuts: List[str], window: Type[QMainWindow],
        play_song: Type[SongsConfigureInterface],
        json_manipulation: Type[SongsJsonManipulationInterface]
        ) -> None:

        self.__id = str(id)
        self.__song_name = song_name
        self.__short_cuts = (*short_cuts, )
        self.__window = window
        self.__play_song = play_song
        self.__json_manipulation = json_manipulation

    def create_card_song(self) -> Type[QFrame]:
        gridLayoutWidget = QWidget(self.__window)
        gridLayoutWidget.setObjectName(r"gridLayoutWidget")
        gridLayoutWidget.setGeometry(QRect(130, 50, 299, 219))

        gridFrame = QFrame(gridLayoutWidget)
        gridFrame.setStyleSheet(self.private__get_style_sheet())
        gridFrame.setContentsMargins(0, 0, 0, 0)

        gridLayout = QGridLayout(gridFrame)
        gridLayout.setObjectName(r"gridLayout")

        # Combo Box | Short cuts

        comboBox = QComboBox(gridFrame)
        comboBox.setObjectName(r"shortCuts")
        comboBox.addItems([*self.__short_cuts])

        # Song name

        song_name = QLabel(gridFrame)
        song_name.setText(self.__song_name)

        # Shortcut label

        short_cut_label = QLabel(gridFrame)
        short_cut_label.setText(r"Atalho : ")

        # Play button

        play_button = QPushButton(gridFrame)
        play_button.setText(r"Play")
        play_button.clicked.connect(
            lambda: self.play_sound_event_button(self.__id, play_button, comboBox) 
            # Pass parameters for play_song
        )
        self.get_saved_shortcut_and_set_in_button(
            play_button, comboBox, self.__id
        )
        comboBox.currentIndexChanged.connect(
            lambda: self.set_shortcut_in_button(
                play_button, comboBox, self.__id
            )
        )

        # Add in grid
        
        gridLayout.addWidget(comboBox, 2, 1, 1, 1)
        gridLayout.addWidget(song_name, 1, 0, 1, 2)
        gridLayout.addWidget(short_cut_label, 2, 0, 1, 1)
        gridLayout.addWidget(play_button, 3, 0, 1, 2)

        return gridFrame

    def private__get_style_sheet(self) -> str:
        qss = (u"QFrame {\n"
                "border-width: 1;\n"
                "border-radius: 5;\n"
                "border-style: solid;\n"
                "border-color: rgb(10, 10, 10)\n"
                "}\n"
                "\n"
                "QLabel {\n"
                "border-width: 0;\n"
                "}")
        return qss

    def play_sound_event_button(self, id: str, 
        button: Type[QPushButton], 
        combo_box: Type[QComboBox]) -> None:

        button_text = button.text()

        print(f'Play Song card : {id}')
        if button_text == 'Play':
            thread_id = self.__play_song.play_song(id)
            button.setAccessibleName(str(thread_id))
            button.setText('Stop')
        else:
            self.__play_song.stop_song(int(button.accessibleName()))
            button.setText('Play')

    def set_shortcut_in_button(self, button: Type[QPushButton], \
        combo_box: Type[QComboBox], id: str) -> None:

            short_cut_text = combo_box.currentText()

            if short_cut_text != '':
                button.setShortcut(QKeySequence(short_cut_text))
                self.__json_manipulation.set_short_cut(id, short_cut_text)

    def get_saved_shortcut_and_set_in_button(self, button: Type[QPushButton], \
        combo_box: Type[QComboBox], id: str):

        shortcut: str = self.__json_manipulation.get_short_cut(id)
        if shortcut != '':
            combo_box.setCurrentText(shortcut)
            button.setShortcut(QKeySequence(shortcut))