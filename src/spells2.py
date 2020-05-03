"""Lista zaklęć"""
import sys

import lorem as lorem
from PySide2.QtCore import QMetaObject, Slot
from PySide2.QtGui import QStandardItemModel, QStandardItem, QFont
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QListView, QHBoxLayout, \
    QSizePolicy, QTextBrowser, QMessageBox


class Spells2(QWidget):
    """
    Klasa odpowiedzialna za Widget czarów
    """

    def __init__(self):
        super().__init__()
        self.btn_level = [QPushButton('Poziom {}'.format(i)) for i in range(10)]
        self.font = QFont()
        self.list_lvl = [QListView() for _ in range(10)]
        self.vbox_l = QVBoxLayout()
        self.vbox_r = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.initUI()

    def initUI(self):
        """
        Inicjuje wygląd
        """
        # Ustawienie fontu
        self.font.setFamily('Krub')
        self.font.setPointSize(11)
        self.setFont(self.font)

        text_spell = QTextBrowser()
        text_spell.setHtml(lorem.text())
        # Ustawianie kontrolek
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        # Ustawianie wyglądu
        entries = ['Czar ', 'Czary ', 'Czaruś ']
        model_lvl = [QStandardItemModel() for _ in range(10)]
        vbox_lvl = [QVBoxLayout() for _ in range(10)]

        for i, value in enumerate(vbox_lvl):
            self.font.setPointSize(10)
            self.list_lvl[i].setFont(self.font)
            self.btn_level[i].setObjectName('poziom_{}'.format(i))
            self.list_lvl[i].setObjectName('lista_{}'.format(i))

            # Uzupełnienie list
            for j in entries:
                item = QStandardItem(j + str(i))
                model_lvl[i].appendRow(item)
            self.list_lvl[i].setModel(model_lvl[i])
            self.list_lvl[i].hide()

            # Ustawianie widoków
            sizePolicy.setHeightForWidth(self.list_lvl[i].sizePolicy().hasHeightForWidth())
            self.list_lvl[i].setSizePolicy(sizePolicy)
            value.addWidget(self.btn_level[i])
            value.addWidget(self.list_lvl[i])
            self.vbox_l.addLayout(value)

        # Ustawianie widoków
        self.vbox_r.addWidget(text_spell)
        self.hbox.addLayout(self.vbox_l)
        self.hbox.addLayout(self.vbox_r)
        self.setLayout(self.hbox)

        # Ustawianie akcji
        QMetaObject.connectSlotsByName(self)

        self.show()

    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

    def click_lvl(self, lvl):
        for i in range(10):
            self.font.setBold(False)
            if i == lvl:
                self.list_lvl[i].show()
                self.font.setBold(True)
                self.btn_level[i].setFont(self.font)
                self.list_lvl[i].clicked.connect(self.click_spell)
                continue
            self.list_lvl[i].hide()
            self.btn_level[i].setFont(self.font)

    def click_spell(self, q_list_view):
        QMessageBox.information(self, 'ListWidget', 'Wiersz：' + q_list_view.data())

    @Slot()
    def on_poziom_0_clicked(self):
        self.click_lvl(0)

    @Slot()
    def on_poziom_1_clicked(self):
        self.click_lvl(1)

    @Slot()
    def on_poziom_2_clicked(self):
        self.click_lvl(2)

    @Slot()
    def on_poziom_3_clicked(self):
        self.click_lvl(3)

    @Slot()
    def on_poziom_4_clicked(self):
        self.click_lvl(4)

    @Slot()
    def on_poziom_5_clicked(self):
        self.click_lvl(5)

    @Slot()
    def on_poziom_6_clicked(self):
        self.click_lvl(6)

    @Slot()
    def on_poziom_7_clicked(self):
        self.click_lvl(7)

    @Slot()
    def on_poziom_8_clicked(self):
        self.click_lvl(8)

    @Slot()
    def on_poziom_9_clicked(self):
        self.click_lvl(9)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Spells2()
    sys.exit(app.exec_())
