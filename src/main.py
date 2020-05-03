import os
import sys

from PySide2.QtGui import QFontDatabase
from PySide2.QtWidgets import QApplication, QStyleFactory

from src.main_window import MainWindow

def run():
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))

    fontDB = QFontDatabase()
    for root, dirs, files in os.walk(os.path.join(os.getcwd(), 'resources\\fonts')):
        for filename in files:
            fontDB.addApplicationFont(os.path.join(root, filename))

    window = MainWindow()
    window.show()
    app.exec_()