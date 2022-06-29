from typing import Type
from pathlib import Path
from os.path import join

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

from source import Factory
from source.factory.interfaces import FactoryInterface

class App():
    def __init__(self, factory : Type[FactoryInterface]) -> None:
        self.__app = QApplication([])
        self.__factory = factory()

        # Add form

        self.__add_form = self.load_ui('add_songs.ui')
        self.__add_form.addSongsButton.clicked.connect(self.add_songs)

        self.__add_form.show()

        self.__app.exec()

    def load_ui(self, ui_file : str) -> Type[QWidget]:
        path = Path().absolute()
        path = join(path, "layouts", "")
        ui_file = QFile(f'{path}{ui_file}')
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        ui = loader.load(ui_file)
        return ui

    def add_songs(self) -> None:
        print("Add songs")

if __name__ == '__main__':
    App(Factory)