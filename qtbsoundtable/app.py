from typing import Type
from pathlib import Path
from os.path import join

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class App():
    def __init__(self) -> None:
        self.__app = QApplication([])

        # Add form

        self.__add_form = self.load_ui('add_songs.ui')

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

if __name__ == '__main__':
    App()