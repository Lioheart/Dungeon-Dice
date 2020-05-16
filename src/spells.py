"""Menu Księgi Zaklęć"""
import os
import queue
import sys
import threading
from os.path import normpath, join

from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import QIcon, QFont, QPalette, QColor, QBrush
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QTextBrowser, QPushButton, \
    QGraphicsDropShadowEffect
from bs4 import BeautifulSoup

from compress_txt import gzip_read


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
        # Wygląd
        palette = QPalette()
        palette_back = QPalette()
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setOffset(0, 0)
        palette.setBrush(QPalette.Active, QPalette.Window, QBrush(QColor(250, 250, 250, 128)))

        # Przyciski nieaktywne
        palette.setBrush(QPalette.Disabled, QPalette.Button, QBrush(QColor(241, 70, 104, 0)))
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, QBrush(QColor(255, 255, 255, 255)))

        # Przyciski aktywne
        palette.setBrush(QPalette.Active, QPalette.Button, QBrush(QColor(238, 246, 252)))
        palette.setBrush(QPalette.Inactive, QPalette.Button, QBrush(QColor(255, 255, 255)))

        palette.setBrush(QPalette.Active, QPalette.ButtonText, QBrush(QColor(29, 114, 170)))
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, QBrush(QColor(54, 54, 54, 128)))

        # Przyciski cofania
        palette_back.setBrush(QPalette.Active, QPalette.ButtonText, QBrush(QColor(0, 0, 0, 178)))
        palette_back.setBrush(QPalette.Inactive, QPalette.ButtonText, QBrush(QColor(0, 0, 0, 50)))

        palette_back.setBrush(QPalette.Active, QPalette.Button, QBrush(QColor('#ffdd57')))
        palette_back.setBrush(QPalette.Inactive, QPalette.Button, QBrush(QColor('#fff8de')))

        # Widzety
        btn_back = QPushButton('Cofnij do menu')
        icon = QIcon()

        # Layouty
        vbox = QVBoxLayout()
        vbox_main = QVBoxLayout()
        hbox = QHBoxLayout()

        # Ustawianie widgetów
        self.description_thread('./resources/descriptions/magic_descr.txt.gz')
        btn_back.setFixedWidth(280)
        self.setPalette(palette)
        self.text_desc.setGraphicsEffect(shadow)
        self.btn_subback.setPalette(palette_back)
        btn_back.setPalette(palette_back)
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
        self.text_desc.setViewportMargins(10, 10, 10, 10)

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
        Wyświetla główne przyciski w Layoucie menu
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
        Czyści Layuot menu z wszystkich widgetów
        """
        for i in reversed(range(self.vbox_child.count())):
            self.vbox_child.itemAt(i).widget().setParent(None)

    def subback(self):
        """
        Odpowiada za funkcję powrotu do menu Księgi czarów
        """
        self.clear_layout()
        self.description_thread('./resources/descriptions/magic_descr.txt.gz')
        self.widget_switch()

    def submenu_create(self, *buttons):
        """
        Tworzy podmenu
        @param buttons: QPushButton
        """
        self.vbox_child.addWidget(self.btn_subback)
        for btn in buttons:
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

        self.description_thread('./resources/descriptions/classes_spells.txt.gz')

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

        self.description_thread('./resources/descriptions/magic.txt.gz')

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

        self.text_desc.setText(
            '''
            <p>Listy czarów dostępne bohaterom oraz opisy zaklęć zaprezentowano w ten sam sposób,
            a każdą kategorię informacji wyjaśniono i zdefiniowano odpowiednio.</p>
            '''
        )

    def arcane(self):
        """
        Odpowiada za wyświetlenie menu opisu zaklęć wtajemniczeń
        """
        self.clear_layout()

        btn_arc1 = QPushButton('Jak czarodziej przygotowuje zaklęcia')
        btn_arc2 = QPushButton('Magiczne zapiski wtajemniczeń')
        btn_arc3 = QPushButton('Zaklinacze i bardowie')

        self.submenu_create(btn_arc1, btn_arc2, btn_arc3)

        btn_arc1.clicked.connect(lambda: self.description_thread('./resources/descriptions/arcane.txt.gz', 'btn1'))
        btn_arc2.clicked.connect(lambda: self.description_thread('./resources/descriptions/arcane.txt.gz', 'btn2'))
        btn_arc3.clicked.connect(lambda: self.description_thread('./resources/descriptions/arcane.txt.gz', 'btn3'))

        self.description_thread('./resources/descriptions/arcane.txt.gz', 'description')

    def divine(self):
        """
        Odpowiada za wyświetlenie menu opisu zakleć objawień
        """
        self.clear_layout()

        btn_div1 = QPushButton('Jak przygotowuje się zaklęcia objawień')
        btn_div2 = QPushButton('Magiczne zapiski objawień')
        btn_div3 = QPushButton('Nowe czary objawień')

        self.submenu_create(btn_div1, btn_div2, btn_div3)

        btn_div1.clicked.connect(
            lambda: self.description_thread('./resources/descriptions/divine.txt.gz', 'btn1'))
        btn_div2.clicked.connect(
            lambda: self.description_thread('./resources/descriptions/divine.txt.gz', 'btn2'))
        btn_div3.clicked.connect(
            lambda: self.description_thread('./resources/descriptions/divine.txt.gz', 'btn3'))

        self.description_thread('./resources/descriptions/divine.txt.gz', 'description')

    def power(self):
        """
        Odpowiada za wyświetlenie menu zdolności specjalnych
        """
        self.clear_layout()

        self.submenu_create()

        self.description_thread('./resources/descriptions/power.txt.gz')

    def description_thread(self, path, bs_id=None):
        """
        Wykonuje odczyt opisu danego podrozdziału z pliku, w osobnym wątku
        :param path: ścieżka do pliku z opisem
        """
        que = queue.Queue()
        x = threading.Thread(target=gzip_read, args=(que, path))
        x.start()  # Rozpoczyna wątek
        x.join()  # Kończy wątek. Aby sprawdzić wystarczy x.is_alive()
        text = que.get()
        if bs_id:
            soup = BeautifulSoup(text, 'html.parser')  # make soup that is parse-able by bs
            text = str(soup.find('div', id=bs_id))
        self.text_desc.setHtml(text)


if __name__ == '__main__':
    os.chdir(normpath(join(os.getcwd(), '..\\')))
    app = QApplication(sys.argv)
    ex = Spells()
    sys.exit(app.exec_())
