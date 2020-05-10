"""
Moduł rozruchowy. Zawiera funkcję uruchamiającą główne okno
"""
import os
import sys

from PySide2.QtGui import QFontDatabase
from PySide2.QtWidgets import QApplication, QStyleFactory

from src.main_window import MainWindow


def run():
    """
    Uruchamia główne okno aplikacji QT, ustawia styl na Fusion oraz wczytuje wszystkie czcionki z folderu fonts
    """
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))

    fontDB = QFontDatabase()
    for root, dirs, files in os.walk(os.path.join(os.getcwd(), '..\\resources\\fonts')):
        for filename in files:
            fontDB.addApplicationFont(os.path.join(root, filename))

    window = MainWindow()
    window.setMinimumSize(1280, 720)
    window.show()
    app.exec_()
