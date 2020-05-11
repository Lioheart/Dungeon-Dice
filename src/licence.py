"""Licencja Otwartej Gry"""
import os
import queue
import threading
from os.path import normpath, join

from PySide2.QtCore import QSize
from PySide2.QtGui import QFont, QIcon
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout, QTextBrowser

from compress_txt import gzip_read


class Licence(QWidget):
    """
    Klasa Licence - wyświetla Licencję Otwartej Gry
    """

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        Inicjuje UI wyglądu menu głównego. Zawiera przyciski z ikonami
        """
        # Widgety
        font = QFont()
        icon = QIcon()
        vbox = QVBoxLayout(self)
        txt_browser = QTextBrowser(self)

        # Ustawienie Widgetów
        font.setFamily('Baloo 2')
        font.setPointSize(12)
        icon.addFile('./resources/icons/dice.svg', QSize(), QIcon.Normal, QIcon.Off)
        self.setFont(font)
        txt_browser.setFont(font)
        que = queue.Queue()
        x = threading.Thread(target=gzip_read, args=(que, './resources/descriptions/licence.txt.gz'))
        x.start()  # Rozpoczyna wątek
        x.join()  # Kończy wątek. Aby sprawdzić wystarczy x.is_alive()
        text = que.get()
        txt_browser.setHtml(text)

        # Ustawienie widoków
        self.setWindowIcon(icon)
        self.setFixedSize(840, 1188)
        vbox.addWidget(txt_browser)


if __name__ == '__main__':
    os.chdir(normpath(join(os.getcwd(), '..\\')))

    import sys

    app = QApplication(sys.argv)
    licence = Licence()
    licence.show()
    sys.exit(app.exec_())
