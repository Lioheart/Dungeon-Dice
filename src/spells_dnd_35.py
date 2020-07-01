"""Lista zaklęć"""
import os
import sys
from os.path import normpath, join

from PySide2.QtWidgets import QWidget, QHBoxLayout, QTextBrowser, QVBoxLayout, QListView, QLineEdit, QPushButton, \
    QSpacerItem, QSizePolicy, QApplication


class ListSpells(QWidget):
    def __init__(self):
        super().__init__()
        self.txt_browser = QTextBrowser()
        self.hbox_main = QHBoxLayout()
        self.initUI()

    def initUI(self):
        """
        Inicjuje wygląd
        """
        # Layouty
        vbox_left = QVBoxLayout()
        vbox_child = QVBoxLayout()
        vbox_right = QVBoxLayout()
        hbox = QHBoxLayout()

        # Widżety
        list_spells = QListView()
        search = QLineEdit()
        btn_subback = QPushButton('Cofnij')
        btn_add = QPushButton('Dodaj')
        btn_edit = QPushButton('Edytuj')
        btn_remove = QPushButton('Usuń')
        h_spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Ustawienia widgetów
        btn_subback.setFixedWidth(280)
        size_policy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(search.sizePolicy().hasHeightForWidth())
        search.setSizePolicy(size_policy)
        size_policy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        size_policy.setHeightForWidth(list_spells.sizePolicy().hasHeightForWidth())
        list_spells.setSizePolicy(size_policy)

        # Ustawienia widoków
        vbox_left.setSpacing(10)
        vbox_right.setSpacing(10)
        vbox_child.addWidget(search)
        vbox_child.addWidget(list_spells)
        vbox_left.addLayout(vbox_child)
        hbox.setSpacing(15)
        hbox.addItem(h_spacer)
        hbox.addWidget(btn_add)
        hbox.addWidget(btn_edit)
        hbox.addWidget(btn_remove)
        vbox_right.addWidget(self.txt_browser)
        vbox_right.addLayout(hbox)

        self.hbox_main.addLayout(vbox_left)
        self.hbox_main.addLayout(vbox_right)
        self.setLayout(self.hbox_main)

        self.show()


if __name__ == '__main__':
    os.chdir(normpath(join(os.getcwd(), '..\\')))
    app = QApplication(sys.argv)
    ex = ListSpells()
    sys.exit(app.exec_())
