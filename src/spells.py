"""Menu Księgi Zaklęć"""
import sys

from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import QIcon, QFont
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QTextBrowser, QPushButton


class Spells(QWidget):
    """
    Klasa odpowiedzialna za Widget księgi zaklęć
    """

    def __init__(self):
        super().__init__()
        self.vbox_child = QVBoxLayout()
        self.btn_subback = QPushButton('Cofnij')
        self.btn_list = QPushButton('Lista zaklęć')
        self.btn_class = QPushButton('Zaklęcia poszczególnych klas')
        self.btn_magic = QPushButton('Rzucanie czarów')
        self.btn_decript = QPushButton('Opis czarów')
        self.btn_arcane = QPushButton('Zaklęcia wtajemniczeń - opis')
        self.btn_divine = QPushButton('Zaklęcia objawień - opis')
        self.btn_power = QPushButton('Zdolności specjalne')
        self.text_desc = QTextBrowser()
        self.initUI()

    def initUI(self):
        """
        Inicjuje wygląd
        """
        # Widzety
        # shadow = QGraphicsDropShadowEffect()
        btn_back = QPushButton('Cofnij do menu')
        icon = QIcon()

        # Layouty
        vbox = QVBoxLayout()
        vbox_main = QVBoxLayout()
        hbox = QHBoxLayout()

        # Ustawianie widgetów
        font = QFont()
        font.setFamily('Krub')
        font.setBold(True)
        self.btn_subback.setFont(font)
        btn_back.setFont(font)
        icon.addFile('./resources/icons/undo-alt-solid.svg', QSize(), QIcon.Normal, QIcon.Off)
        self.btn_subback.setIcon(icon)
        icon.addFile('./resources/icons/arrow-left-solid.svg', QSize(), QIcon.Normal, QIcon.Off)
        btn_back.setIcon(icon)
        # TODO usuń to po wprowadzeniu odpowiednich wartości w bazie danych
        self.btn_list.setEnabled(False)

        # Ustawianie widoków
        self.widget_switch()
        vbox.addLayout(self.vbox_child)
        vbox.addWidget(btn_back, 0, Qt.AlignBottom)
        hbox.addLayout(vbox)
        hbox.addWidget(self.text_desc)
        vbox_main.addLayout(hbox)
        self.setLayout(vbox_main)

        # Ustawianie Slotów i sygnałów
        btn_back.clicked.connect(lambda: self.parent().setCurrentIndex(0))
        self.btn_subback.clicked.connect(self.subback)
        self.btn_list.clicked.connect(self.power)
        self.btn_class.clicked.connect(self.classes_spells)
        self.btn_magic.clicked.connect(self.magic)
        self.btn_decript.clicked.connect(self.description)
        self.btn_arcane.clicked.connect(self.arcane)
        self.btn_divine.clicked.connect(self.divine)
        self.btn_power.clicked.connect(self.power)

        self.show()

    def widget_switch(self):
        """
        Wyświetla przyciski w Layoucie menu
        """
        self.vbox_child.addWidget(self.btn_list)
        self.vbox_child.addWidget(self.btn_class)
        self.vbox_child.addWidget(self.btn_magic)
        self.vbox_child.addWidget(self.btn_decript)
        self.vbox_child.addWidget(self.btn_arcane)
        self.vbox_child.addWidget(self.btn_divine)
        self.vbox_child.addWidget(self.btn_power)

    def clear_layout(self):
        """
        Czyści Layuot menu z niepotrzebnych widgetów
        """
        for i in reversed(range(self.vbox_child.count())):
            self.vbox_child.itemAt(i).widget().setParent(None)

    def subback(self):
        """
        Odpowiada za funkcję powrotu do podmenu Księgi czarów
        """
        self.clear_layout()
        self.text_desc.setText('')
        self.widget_switch()

    def submenu_create(self, *buttons):
        """
        Tworzy podmenu
        @param buttons: QPushButton
        """
        self.vbox_child.addWidget(self.btn_subback)
        for btn in buttons:
            # TODO usuń to po wprowadzeniu odpowiednich wartości w bazie danych
            btn.setDisabled(True)
            self.vbox_child.addWidget(btn)

    def classes_spells(self):
        """
        Odpowiada za wyświetlenie menu zaklęć klas
        """
        self.clear_layout()

        btn_cls1 = QPushButton('Zaklęcia BARDA')
        btn_cls2 = QPushButton('Zaklęcia CZARODZIEJA/ZAKLINACZA')
        btn_cls3 = QPushButton('Zaklęcia DRUIDA')
        btn_cls4 = QPushButton('Zaklęcia KAPŁANA')
        btn_cls5 = QPushButton('Zaklęcia PALADYNA')
        btn_cls6 = QPushButton('Zaklęcia TROPICIELA')
        btn_cls7 = QPushButton('DOMENY KAPŁAŃSKIE')

        self.submenu_create(btn_cls1, btn_cls2, btn_cls3, btn_cls4, btn_cls5, btn_cls6, btn_cls7)

        self.text_desc.setText('Na początku tego rozdziału...')

    def magic(self):
        """
        Odpowiada za wyświetlenie menu funkcjonowania czarów
        """
        self.clear_layout()

        btn_mag1 = QPushButton('Funkcjonowanie czarowania')
        btn_mag2 = QPushButton('Wybór czarów')
        btn_mag3 = QPushButton('Koncentracja')
        btn_mag4 = QPushButton('Kontrczarowanie')
        btn_mag5 = QPushButton('Poziom czarującego')
        btn_mag6 = QPushButton('Nieudane rzucenie zaklęcia')
        btn_mag7 = QPushButton('Wyniki działania czaru')
        btn_mag8 = QPushButton('Specjalne efekty czarów')
        btn_mag9 = QPushButton('Łączenie efektów magicznych')

        self.submenu_create(btn_mag1, btn_mag2, btn_mag3, btn_mag4, btn_mag5, btn_mag6, btn_mag7, btn_mag8, btn_mag9)

        self.text_desc.setText('Rzucanie czarów to taki sam proces...')

    def description(self):
        """
        Odpowiada za wyświetlenie menu opisu zaklęć
        """
        self.clear_layout()

        btn_desc1 = QPushButton('Nazwa')
        btn_desc2 = QPushButton('Szkoła (Podszkoła)')
        btn_desc3 = QPushButton('[Określnik]')
        btn_desc4 = QPushButton('Poziom')
        btn_desc5 = QPushButton('Komponenty')
        btn_desc6 = QPushButton('Czas rzucania')
        btn_desc7 = QPushButton('Zasięg')
        btn_desc8 = QPushButton('Celowanie czarem')
        btn_desc9 = QPushButton('Czas działania')
        btn_desc10 = QPushButton('Rzut obronny')
        btn_desc11 = QPushButton('Odporność na czary')
        btn_desc12 = QPushButton('Opis działania')

        self.submenu_create(btn_desc1, btn_desc2, btn_desc3, btn_desc4, btn_desc5, btn_desc6, btn_desc7, btn_desc8,
                            btn_desc9, btn_desc10, btn_desc11, btn_desc12)

        self.text_desc.setText('Listy czarów dostępne bohaterom...')

    def arcane(self):
        """
        Odpowiada za wyświetlenie menu opisu zaklęć wtajemniczeń
        """
        self.clear_layout()

        btn_arc1 = QPushButton('Jak czarodziej przygotowuje zaklęcia')
        btn_arc2 = QPushButton('Magiczne zapiski wtajemniczeń')
        btn_arc3 = QPushButton('Zaklinacze i bardowie')

        self.submenu_create(btn_arc1, btn_arc2, btn_arc3)

        self.text_desc.setText('Czarodzieje, zaklinacze oraz bardowie...')

    def divine(self):
        """
        Odpowiada za wyświetlenie menu opisu zakleć objawień
        """
        self.clear_layout()

        btn_div1 = QPushButton('Jak przygotowuje się zaklęcia objawień')
        btn_div2 = QPushButton('Magiczne zapiski objawień')
        btn_div3 = QPushButton('Nowe czary objawień')

        self.submenu_create(btn_div1, btn_div2, btn_div3)

        self.text_desc.setText('Kapłani, druidzi, doświadczeni paladyni...')

    def power(self):
        """
        Odpowiada za wyświetlenie menu zdolności specjalnych
        """
        self.clear_layout()

        btn_pow1 = QPushButton('Zdolności czaropodobne')
        btn_pow2 = QPushButton('Zdolności nadnaturalne')
        btn_pow3 = QPushButton('Zdolności nadzwyczajne')
        btn_pow4 = QPushButton('Zdolności naturalne')

        self.submenu_create(btn_pow1, btn_pow2, btn_pow3, btn_pow4)

        self.text_desc.setText('Meduzy, driady, harpie...')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Spells()
    sys.exit(app.exec_())
