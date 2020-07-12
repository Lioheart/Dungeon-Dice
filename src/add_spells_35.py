"""Moduł odpowiedzialny za wygląd oraz funkcje dodawania nowych czarów z edycji 3.5 do bazy danych."""
import os
import sys
from os.path import normpath, join

from PySide2.QtCore import QSize, SIGNAL
from PySide2.QtGui import QFont, QIcon
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QDialogButtonBox, \
    QFormLayout, QLineEdit, QSizePolicy, QTextEdit, QMessageBox

from src.ui import Button, DialogButton, ComboBox


class LevelClass(QWidget):
    """Odpowiada za klasę i poziom"""

    def __init__(self):
        super().__init__()
        self.vbox = QVBoxLayout()
        self.btn_add = Button('Dodaj')
        self.counter = 0
        self.data = {}
        self.initUI()

    def initUI(self):
        """
        Inicjuje wygląd
        """
        # Ustawienia widgetów
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy)

        # Ustawienia widoków
        self.vbox.setContentsMargins(0, 0, 0, 0)
        self.vbox.addWidget(self.btn_add)
        self.new()
        self.setLayout(self.vbox)

        self.btn_add.clicked.connect(self.new)

    def leaveEvent(self, event):
        """
        Obsługuje sygnał wyjścia z widżetu.
        :param event: SIGNAL
        :return: dict
        """
        class_names = []
        lvl_names = []
        lvl_class = {
            'Bard': 'Brd',
            'Czarodziej': 'Cza',
            'Druid': 'Drd',
            'Kapłan': 'Kap',
            'Paladyn': 'Pal',
            'Tropiciel': 'Trp',
            'Zaklinacz': 'Zak'
        }

        for child in self.children():  # listuje wszystkie dzieci
            x = self.findChild(ComboBox, child.objectName())
            if x and 'class' in x.objectName():
                class_names.append(lvl_class[x.currentText()])
            elif x:
                lvl_names.append(x.currentText())

        zipbObj = zip(class_names, lvl_names)
        self.data = dict(zipbObj)
        return self.data

    def new(self):
        """
        Tworzy nowy layout z wyborem klasy i poziomu
        :return: None
        """
        class_lvl = ComboBox()
        lvl = ComboBox()
        class_lvl.setObjectName('classlvl_' + str(self.counter))
        lvl.setObjectName('lvl_' + str(self.counter))
        class_lvl.addItem('Bard')
        class_lvl.addItem('Czarodziej')
        class_lvl.addItem('Druid')
        class_lvl.addItem('Kapłan')
        class_lvl.addItem('Paladyn')
        class_lvl.addItem('Tropiciel')
        class_lvl.addItem('Zaklinacz')
        for i in range(1, 10):
            lvl.addItem(str(i))

        hbox = QHBoxLayout()
        hbox.setSpacing(10)
        hbox.addWidget(class_lvl)
        hbox.addWidget(lvl)
        self.vbox.removeWidget(self.btn_add)
        self.vbox.addLayout(hbox)
        self.vbox.addWidget(self.btn_add)
        self.counter += 1


class AddSpells(QWidget):
    """
    Klasa odpowiedzialna za Widget dodawania nowych zaklęć do edycji 3.5
    """

    def __init__(self, parent=None):
        super().__init__()
        self.targer = ComboBox()
        self.parent = parent
        self.plain_text_edit = QTextEdit()
        self.name = QLineEdit()
        self.source_book = QLineEdit()
        self.source_page = QLineEdit()
        self.school = QLineEdit()
        self.sub_school = QLineEdit()
        self.descriptor = QLineEdit()
        self.lvl_class = LevelClass()
        self.components = QLineEdit()
        self.casting_time = QLineEdit()
        self.scope = QLineEdit()
        self.magic_targeting = QLineEdit()
        self.duration = QLineEdit()
        self.saving_throw = QLineEdit()
        self.resistance = QLineEdit()
        self.focus = QLineEdit()
        self.descriptor_short = QLineEdit()
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
        btn_import = Button('Importuj z pliku')
        button_box = DialogButton()

        form_left = QFormLayout()
        form_right = QFormLayout()

        # Layouty
        form_layout = QVBoxLayout()
        hbox_up = QHBoxLayout()
        vbox_down = QVBoxLayout()
        hbox_btn = QHBoxLayout()

        # Ustawianie widgetów
        self.targer.addItem('Cel')
        self.targer.addItem('Efekt')
        self.targer.addItem('Obszar')
        self.targer.addItem('Linia efektu')
        button_box.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        form_left.addRow(QLabel('Nazwa:'), self.name)
        form_left.addRow(QLabel('Podręcznik:'), self.source_book)
        form_left.addRow(QLabel('Strona:'), self.source_page)
        form_left.addRow(QLabel('Szkoła magii:'), self.school)
        form_left.addRow(QLabel('Podszkoła:'), self.sub_school)
        form_left.addRow(QLabel('Określnik:'), self.descriptor)
        form_left.addRow(QLabel('Poziom i klasa:'), self.lvl_class)
        form_right.addRow(QLabel('Komponenty:'), self.components)
        form_right.addRow(QLabel('Czas rzucania:'), self.casting_time)
        form_right.addRow(QLabel('Zasięg:'), self.scope)
        form_right.addRow(self.targer, self.magic_targeting)
        form_right.addRow(QLabel('Czas działania:'), self.duration)
        form_right.addRow(QLabel('Rzut obronny:'), self.saving_throw)
        form_right.addRow(QLabel('Odporność na czary:'), self.resistance)
        form_right.addRow(QLabel('Koncentrator:'), self.focus)
        form_right.addRow(QLabel('Opis krótki:'), self.descriptor_short)

        # Ustawianie widoków
        hbox_up.addLayout(form_left)
        hbox_up.addLayout(form_right)
        hbox_btn.addWidget(btn_import)
        hbox_btn.addWidget(button_box)
        vbox_down.addWidget(lbl_description)
        vbox_down.addWidget(self.plain_text_edit)
        vbox_down.addLayout(hbox_btn)
        form_layout.addLayout(hbox_up)
        form_layout.addLayout(vbox_down)
        self.setLayout(form_layout)

        # Ustawianie Slotów i sygnałów
        button_box.accepted.connect(self.add)
        button_box.rejected.connect(self.close)

    def add(self):
        """Obsługa zdarzenia kliknięcia w przycisk OK"""
        if self.name.text():
            self.close()
        else:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Nie podano wszystkich danych!")
            msg.setWindowTitle("Nie podano danych")
            msg.exec_()

    def closeEvent(self, event):
        """
        Obsługa zdarzenia wyłączenia okna.
        W momencie, gdy niezbędne dane są podane, następuje wywołanie funkcji
        nadrzędnej z parametrem danych.
        """

        data = [
            self.name.text(),
            self.source_book.text(),
            self.source_page.text(),
            self.school.text(),
            self.sub_school.text(),
            self.descriptor.text(),
            str(self.lvl_class.leaveEvent(SIGNAL)),
            self.components.text(),
            self.casting_time.text(),
            self.scope.text(),
            str({self.targer.currentText(): self.magic_targeting.text()}),
            self.duration.text(),
            self.saving_throw.text(),
            self.resistance.text(),
            str({'Koncentrator': self.focus.text()}),
            '<p>' + self.descriptor_short.text() + '</p>',
            '<p>' + self.plain_text_edit.toPlainText() + '</p>'
        ]
        if self.parent:
            self.parent.add_new_spell(data)


if __name__ == '__main__':
    os.chdir(normpath(join(os.getcwd(), '..\\')))
    app = QApplication(sys.argv)
    add_spell = AddSpells()
    add_spell.show()
    sys.exit(app.exec_())
