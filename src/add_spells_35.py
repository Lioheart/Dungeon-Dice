"""Moduł odpowiedzialny za wygląd oraz funkcje dodawania nowych czarów z edycji 3.5 do bazy danych."""
import os
import sys
from os.path import normpath, join

from PySide2.QtCore import QSize
from PySide2.QtGui import QFont, QIcon
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QPlainTextEdit, QDialogButtonBox, \
    QFormLayout, QLineEdit, QSizePolicy

from src.ui import Button, DialogButton, ComboBox


class LevelClass(QWidget):
    """Odpowiada za klasę i poziom"""

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        Inicjuje wygląd
        """
        # Widgety
        lvl = ComboBox()
        class_lvl = ComboBox()
        btn_add = Button('Dodaj')

        # Layouty
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        # Ustawienia widgetów
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(btn_add.sizePolicy().hasHeightForWidth())
        btn_add.setSizePolicy(sizePolicy)
        class_lvl.addItem('Barbarzyńca')
        class_lvl.addItem('Bard')
        class_lvl.addItem('Czarodziej')
        class_lvl.addItem('Druid')
        class_lvl.addItem('Kapłan')
        class_lvl.addItem('Łotrzyk')
        class_lvl.addItem('Mnich')
        class_lvl.addItem('Paladyn')
        class_lvl.addItem('Tropiciel')
        class_lvl.addItem('Wojownik')
        class_lvl.addItem('Zaklinacz')
        for i in range(1, 10):
            lvl.addItem(str(i))

        # Ustawienia widoków
        vbox.setContentsMargins(0, 0, 0, 0)
        hbox.setSpacing(10)
        hbox.addWidget(class_lvl)
        hbox.addWidget(lvl)
        vbox.addLayout(hbox)
        vbox.addWidget(btn_add)
        self.setLayout(vbox)


class AddSpells(QWidget):
    """
    Klasa odpowiedzialna za Widget dodawania nowych zaklęć do edycji 3.5
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dodaj nowe zaklęcie')
        self.initUI()

    def initUI(self):
        """
        Inicjuje wygląd
        """
        # Wygląd
        font = QFont()
        icon = QIcon()

        # Ustawienia
        font.setFamily('Baloo 2')
        font.setPointSize(12)
        icon.addFile('./resources/icons/dice.svg', QSize(), QIcon.Normal, QIcon.Off)
        self.setFont(font)
        self.setWindowIcon(icon)

        # Widzety
        lbl_description = QLabel('Opis długi:')
        plain_text_edit = QPlainTextEdit()
        btn_import = Button('Importuj z pliku')
        button_box = DialogButton()

        form_left = QFormLayout()
        form_right = QFormLayout()
        name = QLineEdit()
        source_book = QLineEdit()
        source_page = QLineEdit()
        school = QLineEdit()
        sub_school = QLineEdit()
        descriptor = QLineEdit()
        lvl_class = LevelClass()
        components = QLineEdit()
        casting_time = QLineEdit()
        scope = QLineEdit()
        magic_targeting = QLineEdit()
        duration = QLineEdit()
        saving_throw = QLineEdit()
        resistance = QLineEdit()
        focus = QLineEdit()
        descriptor_short = QLineEdit()

        # Layouty
        form_layout = QVBoxLayout()
        hbox_up = QHBoxLayout()
        vbox_down = QVBoxLayout()
        hbox_btn = QHBoxLayout()

        # Ustawianie widgetów
        button_box.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        form_left.addRow(QLabel('Nazwa:'), name)
        form_left.addRow(QLabel('Podręcznik:'), source_book)
        form_left.addRow(QLabel('Strona:'), source_page)
        form_left.addRow(QLabel('Szkoła magii:'), school)
        form_left.addRow(QLabel('Podszkoła:'), sub_school)
        form_left.addRow(QLabel('Określnik:'), descriptor)
        form_left.addRow(QLabel('Poziom i klasa:'), lvl_class)
        form_right.addRow(QLabel('Komponenty:'), components)
        form_right.addRow(QLabel('Czas rzucania:'), casting_time)
        form_right.addRow(QLabel('Zasięg:'), scope)
        form_right.addRow(QLabel('Cel:'), magic_targeting)
        form_right.addRow(QLabel('Czas działania:'), duration)
        form_right.addRow(QLabel('Rzut obronny:'), saving_throw)
        form_right.addRow(QLabel('Odporność na czary:'), resistance)
        form_right.addRow(QLabel('Koncentrator:'), focus)
        form_right.addRow(QLabel('Opis krótki:'), descriptor_short)

        # Ustawianie widoków
        hbox_up.addLayout(form_left)
        hbox_up.addLayout(form_right)
        hbox_btn.addWidget(btn_import)
        hbox_btn.addWidget(button_box)
        vbox_down.addWidget(lbl_description)
        vbox_down.addWidget(plain_text_edit)
        vbox_down.addLayout(hbox_btn)
        form_layout.addLayout(hbox_up)
        form_layout.addLayout(vbox_down)
        self.setLayout(form_layout)

        # Ustawianie Slotów i sygnałów


if __name__ == '__main__':
    os.chdir(normpath(join(os.getcwd(), '..\\')))
    app = QApplication(sys.argv)
    add_spell = AddSpells()
    add_spell.show()
    sys.exit(app.exec_())
