"""
Moduł rozruchowy. Zawiera funkcję uruchamiającą główne okno
"""
import os
import sys

from PySide2.QtCore import QTranslator, QLocale, QLibraryInfo
from PySide2.QtGui import QFontDatabase
from PySide2.QtWidgets import QApplication, QStyleFactory

from check_state import update, donate
from src.main_window import MainWindow


def run():
    """
    Uruchamia główne okno aplikacji QT, ustawia styl na Fusion oraz wczytuje wszystkie czcionki z folderu fonts
    """
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    update()

    # Dodawanie czcionek
    fontDB = QFontDatabase()
    for root, dirs, files in os.walk(os.path.join(os.getcwd(), '.\\resources\\fonts')):
        for filename in files:
            fontDB.addApplicationFont(os.path.join(root, filename))

    # Tłumaczenie
    qt_translator = QTranslator()
    qt_translator.load("qt_" + QLocale.system().name(),
                       QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    app.installTranslator(qt_translator)

    window = MainWindow()
    window.setMinimumSize(1280, 720)
    window.show()

    donate()
    app.exec_()
