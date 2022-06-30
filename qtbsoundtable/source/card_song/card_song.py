from typing import List, Type
from PySide6.QtWidgets import QWidget, QGridLayout, \
    QLabel, QPushButton, QComboBox, QMainWindow
from PySide6.QtCore import QRect

from .interfaces import CardSongInterface

class CardSong(CardSongInterface):
    def __init__(self, id: int, song_name: str, \
        short_cuts: List[str], window: Type[QMainWindow]) -> None:

        self.__id = str(id)
        self.__song_name = song_name
        self.__short_cuts = (*short_cuts, )
        self.__window = window

    def create_card_song(self) -> Type[QGridLayout]:
        gridLayoutWidget = QWidget(self.__window)
        gridLayoutWidget.setObjectName(r"gridLayoutWidget")
        gridLayoutWidget.setGeometry(QRect(130, 50, 299, 219))

        gridLayout = QGridLayout(gridLayoutWidget)
        gridLayout.setObjectName(r"gridLayout")
        gridLayout.setContentsMargins(0, 0, 0, 0)

        # Combo Box | Short cuts

        comboBox = QComboBox(gridLayoutWidget)
        comboBox.setObjectName(r"shortCuts")
        comboBox.addItems([*self.__short_cuts])

        # Song name

        song_name = QLabel(gridLayoutWidget)
        song_name.setText(self.__song_name)

        # Shortcut label

        short_cut_label = QLabel(gridLayoutWidget)
        short_cut_label.setText(r"Atalho : ")

        # Play button

        play_button = QPushButton(gridLayoutWidget)
        play_button.setText(r"Play")
        play_button.setObjectName(self.__id)

        # Add in grid
        
        gridLayout.addWidget(comboBox, 2, 1, 1, 1)
        gridLayout.addWidget(song_name, 1, 0, 1, 2)
        gridLayout.addWidget(short_cut_label, 2, 0, 1, 1)
        gridLayout.addWidget(play_button, 3, 0, 1, 2)

        print(f"Card Created + {gridLayout}")

        return gridLayout