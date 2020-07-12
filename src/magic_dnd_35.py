"""Menu Księgi Zaklęć"""
import ast
import datetime
import os
import queue
import sys
import threading
from os.path import normpath, join

from PySide2 import QtSql
from PySide2.QtCore import QSize, Qt, QPersistentModelIndex, QModelIndex
from PySide2.QtGui import QIcon, QPalette, QColor, QBrush, QStandardItemModel, QStandardItem
from PySide2.QtSql import QSqlDatabase, QSqlQuery
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QTextBrowser, \
    QGraphicsDropShadowEffect, QListView, QLineEdit, QSizePolicy, QAbstractItemView, QMessageBox
from bs4 import BeautifulSoup

from compress_txt import gzip_read
from src.add_spells_35 import AddSpells
from src.ui import ButtonBack, Button, ButtonAdd, ButtonDelete, ButtonEdit


class Spells(QWidget):
    """
    Klasa odpowiedzialna za Widget księgi zaklęć
    """

    def __init__(self):
        super().__init__()
        self.list_spells = QListView()
        self.add_new = AddSpells(self)
        self.btn_remove = ButtonDelete('Usuń')
        self.btn_edit = ButtonEdit('Edytuj')
        self.vbox_list = QVBoxLayout()
        self.hbox_list = QHBoxLayout()
        self.vbox_child = QVBoxLayout()
        self.btn_subback = ButtonBack('Cofnij')
        self.btn_list = Button('Lista zaklęć')
        self.btn_class = Button('Zaklęcia poszczególnych klas')
        self.btn_magic = Button('Rzucanie czarów')
        self.btn_decript = Button('Opis czarów')
        self.btn_arcane = Button('Zaklęcia wtajemniczeń - opis')
        self.btn_divine = Button('Zaklęcia objawień - opis')
        self.btn_power = Button('Zdolności specjalne')
        self.text_desc = QTextBrowser()
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('dnd3.5.db')
        self.model = QtSql.QSqlTableModel()
        self.model.setTable('spells')
        self.model.select()
        self.i = self.model.rowCount()
        self.initUI()

    def initUI(self):
        """
        Inicjuje wygląd
        """
        # Wygląd okna
        palette = QPalette()
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setOffset(0, 0)
        palette.setBrush(QPalette.Active, QPalette.Window, QBrush(QColor(250, 250, 250, 128)))

        # Widzety
        btn_back = ButtonBack('Cofnij do menu')
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
        icon.addFile('./resources/icons/undo-alt-solid.svg', QSize(), QIcon.Normal, QIcon.Off)
        self.btn_subback.setIcon(icon)
        icon.addFile('./resources/icons/arrow-left-solid.svg', QSize(), QIcon.Normal, QIcon.Off)
        btn_back.setIcon(icon)
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
        self.btn_list.clicked.connect(self.listing_spells)

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
        Czyści Layuot menu z wszystkich widgetów i Layoutów
        """
        for i in reversed(range(self.vbox_child.count())):
            try:
                # Usuwa widgety
                self.vbox_child.itemAt(i).widget().setParent(None)
            except AttributeError:
                # Usuwanie widgetów z layoutów list_spell
                for j in reversed(range(self.hbox_list.count())):
                    self.hbox_list.itemAt(j).widget().setParent(None)
                for j in reversed(range(self.vbox_list.count())):
                    try:
                        self.vbox_list.itemAt(j).widget().setParent(None)
                    except AttributeError:
                        layout_item = self.vbox_list.itemAt(j)
                        self.vbox_list.removeItem(layout_item)
                        self.vbox_list.takeAt(j)

                # Usuwa Layouty
                layout_item = self.vbox_child.itemAt(i)
                self.vbox_child.removeItem(layout_item)
                self.vbox_child.takeAt(i)

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
        @param buttons: Button
        """
        self.vbox_child.addWidget(self.btn_subback)
        for btn in buttons:
            if btn.isWidgetType():
                self.vbox_child.addWidget(btn)
            else:
                self.vbox_child.addLayout(btn)

    def classes_spells(self):
        """
        Odpowiada za wyświetlenie menu zaklęć klas
        """
        self.clear_layout()

        btn_cls1 = Button('Zaklęcia BARDA')
        btn_cls2 = Button('Zaklęcia CZARODZIEJA/ZAKLINACZA')
        btn_cls3 = Button('Zaklęcia DRUIDA')
        btn_cls4 = Button('Zaklęcia KAPŁANA')
        btn_cls5 = Button('Zaklęcia PALADYNA')
        btn_cls6 = Button('Zaklęcia TROPICIELA')
        btn_cls7 = Button('DOMENY KAPŁAŃSKIE')

        self.submenu_create(btn_cls1, btn_cls2, btn_cls3, btn_cls4, btn_cls5, btn_cls6, btn_cls7)

        self.description_thread('./resources/descriptions/classes_spells.txt.gz')

    def magic(self):
        """
        Odpowiada za wyświetlenie menu funkcjonowania czarów
        """
        path = './resources/descriptions/magic.txt.gz'
        self.clear_layout()

        btn_mag1 = Button('Funkcjonowanie czarowania')
        btn_mag2 = Button('Wybór czarów')
        btn_mag3 = Button('Koncentracja')
        btn_mag4 = Button('Kontrczarowanie')
        btn_mag5 = Button('Poziom czarującego')
        btn_mag6 = Button('Nieudane rzucenie zaklęcia')
        btn_mag7 = Button('Wyniki działania czaru')
        btn_mag8 = Button('Specjalne efekty czarów')
        btn_mag9 = Button('Łączenie efektów magicznych')

        self.create_btn_connect(path, btn_mag1, btn_mag2, btn_mag3, btn_mag4, btn_mag5, btn_mag6, btn_mag7, btn_mag8,
                                btn_mag9)

        self.description_thread(path, 'description')

    def description(self):
        """
        Odpowiada za wyświetlenie menu opisu zaklęć
        """
        path = './resources/descriptions/desc_magic.txt.gz'
        self.clear_layout()

        btn_desc1 = Button('Nazwa')
        btn_desc2 = Button('Szkoła (Podszkoła)')
        btn_desc3 = Button('[Określnik]')
        btn_desc4 = Button('Poziom')
        btn_desc5 = Button('Komponenty')
        btn_desc6 = Button('Czas rzucania')
        btn_desc7 = Button('Zasięg')
        btn_desc8 = Button('Celowanie czarem')
        btn_desc9 = Button('Czas działania')
        btn_desc10 = Button('Rzut obronny')
        btn_desc11 = Button('Odporność na czary')
        btn_desc12 = Button('Opis działania')

        self.create_btn_connect(path, btn_desc1, btn_desc2, btn_desc3, btn_desc4, btn_desc5, btn_desc6, btn_desc7,
                                btn_desc8, btn_desc9, btn_desc10, btn_desc11, btn_desc12)

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
        path = './resources/descriptions/arcane.txt.gz'
        self.clear_layout()

        btn_arc1 = Button('Jak czarodziej przygotowuje zaklęcia')
        btn_arc2 = Button('Magiczne zapiski wtajemniczeń')
        btn_arc3 = Button('Zaklinacze i bardowie')

        self.create_btn_connect(path, btn_arc1, btn_arc2, btn_arc3)

        self.description_thread(path, 'description')

    def divine(self):
        """
        Odpowiada za wyświetlenie menu opisu zakleć objawień
        """
        path = './resources/descriptions/divine.txt.gz'
        self.clear_layout()

        btn_div1 = Button('Jak przygotowuje się zaklęcia objawień')
        btn_div2 = Button('Magiczne zapiski objawień')
        btn_div3 = Button('Nowe czary objawień')

        self.create_btn_connect(path, btn_div1, btn_div2, btn_div3)
        self.description_thread(path, 'description')

    def power(self):
        """
        Odpowiada za wyświetlenie menu zdolności specjalnych
        """
        path = './resources/descriptions/power.txt.gz'
        self.clear_layout()

        self.submenu_create()

        self.description_thread(path)

    def model_list(self):
        """
        Odświeża listę zaklęć
        """
        self.model.setTable('spells')
        self.model.select()
        model_list = QStandardItemModel(self.list_spells)
        for row in range(self.model.rowCount()):
            name = self.model.data(self.model.index(row, 1))
            model_list.appendRow(QStandardItem(name))
        self.list_spells.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.list_spells.setModel(model_list)
        self.list_spells.clicked.connect(self.on_item_clicked)

    def listing_spells(self):
        """
        Pokazuje listę zaklęć
        """
        # Widżety i layouty
        search = QLineEdit()
        btn_add = ButtonAdd('Dodaj')

        # Ustawianie modelu dla listy
        self.model_list()

        # Konfiguracja
        self.btn_edit.setEnabled(False)
        self.btn_remove.setEnabled(False)
        self.hbox_list.addWidget(self.btn_edit)
        self.hbox_list.addWidget(self.btn_remove)
        self.vbox_list.addWidget(search)
        self.vbox_list.addWidget(self.list_spells)
        self.vbox_list.addWidget(btn_add)
        self.vbox_list.addLayout(self.hbox_list)
        size_policy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        size_policy.setHeightForWidth(self.list_spells.sizePolicy().hasHeightForWidth())
        self.list_spells.setSizePolicy(size_policy)
        size_policy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        size_policy.setHeightForWidth(search.sizePolicy().hasHeightForWidth())
        search.setSizePolicy(size_policy)

        # Signal and slots
        btn_add.clicked.connect(lambda: self.add_new.show())
        self.btn_remove.clicked.connect(self.remove_spell)

        self.submenu_create(self.vbox_list)

        self.text_desc.setText('''<p>Lista zaklęć</p>''')

    def remove_spell(self):
        if self.list_spells.currentIndex().row() > -1:
            query_string = 'DELETE FROM spells WHERE name="{}";'.format(self.list_spells.currentIndex().data())
            query = QSqlQuery()
            query.prepare(query_string)
            query.exec_()
            self.model.setQuery(query)
            self.model_list()
            self.i = self.model.rowCount()
        else:
            QMessageBox.warning(self, 'Uwaga', "Proszę wybrać zaklęcie zanim dokonasz usunięcia", QMessageBox.Ok)
            self.show()

    def add_new_spell(self, data):
        """
        Funkcja ta wprowadza nowe zaklęcie do bazy danych. Jest to funkcja wywoływana
        tylko poprzez wewnętrzną klasę.
        :param data: Dane zaklęcia do bazy
        """
        if data[0]:
            self.model.insertRows(self.i, 1)
            for col in range(1, self.model.columnCount() - 1):
                self.model.setData(self.model.index(self.i, col), data[col - 1])
            self.model.setData(self.model.index(self.i, self.model.columnCount()), datetime.datetime.utcnow)
            self.model.submitAll()

            self.model_list()

    def on_item_clicked(self, item):
        """
        Wyświetla dane z bazy, zależnie od klikniętego czaru.
        :param item: QModel
        """
        self.btn_edit.setEnabled(True)
        self.btn_remove.setEnabled(True)
        self.model.setFilter("name LIKE '%{}%'".format(item.data()))
        self.model.select()

        # Ustalanie danych
        title = self.model.data(self.model.index(0, 1))
        source_book = self.model.data(self.model.index(0, 2))
        source_page = self.model.data(self.model.index(0, 3))
        school = self.model.data(self.model.index(0, 4))
        sub_school = self.model.data(self.model.index(0, 5))
        descriptor = self.model.data(self.model.index(0, 6))
        class_lvl = ast.literal_eval(self.model.data(self.model.index(0, 7)))
        components = self.model.data(self.model.index(0, 8))
        casting_time = self.model.data(self.model.index(0, 9))
        range_spell = self.model.data(self.model.index(0, 10))
        magic_targeting = ast.literal_eval(self.model.data(self.model.index(0, 11)))
        for x, y in magic_targeting.items():
            mt_keys, mt_values = x, y
        duration = self.model.data(self.model.index(0, 12))
        saving_throw = self.model.data(self.model.index(0, 13))
        resistance = self.model.data(self.model.index(0, 14))
        description = self.model.data(self.model.index(0, 17))
        try:
            focus = ast.literal_eval(self.model.data(self.model.index(0, 15)) or None)
            for x, y in focus.items():
                f_keys, f_values = x, y
        except ValueError:
            f_keys, f_values = 'Koncentrator', 'Brak'

        # Modyfikowanie danych
        source_book += ', str.' + source_page
        if sub_school:
            school += ' (' + sub_school + ')'
        if descriptor:
            school += ' [' + descriptor + ']'
        class_lvl = list(class_lvl.items())
        class_lvl_spell = ''
        if len(class_lvl) > 1:
            for value in class_lvl:
                for result in value:
                    class_lvl_spell += str(result) + ' '
                class_lvl_spell += ', '
            class_lvl_spell = class_lvl_spell[:-2]
        else:
            class_lvl_spell += str(class_lvl[0][0]) + str(class_lvl[0][1])

        # Tworzenie tekstu do wyświetlenia
        full_text = '''
        <html>
            <body>
                <table width=100%>
                    <tr>
                        <td ><h1>{}</h1></td>
                        <td align="right">{}</td>
                    </tr>
                </table>
                <div>
                    <p><small>{}</small></p>
                <p>
                    <strong>Poziom:</strong>
                    {}
                </p>
                <p>
                    <strong>Komponenty:</strong>
                    {}
                </p>
                <p>
                    <strong>Czas rzucania:</strong>
                    {}
                </p>
                <p>
                    <strong>Zasięg:</strong>
                    {}
                </p>
                <p>
                    <strong>{}:</strong>
                    {}
                </p>
                <p>
                    <strong>Czas działania:</strong>
                    {}
                </p>
                <p>
                    <strong>Rzut obronny:</strong>
                    {}
                </p>
                <p>
                    <strong>Odporność na czary:</strong>
                    {}
                </p>
                <p>
                    <em>{}:</em>
                    {}
                </p>
                </div>
                <p style="-qt-paragraph-type:empty; margin-top:15px; margin-bottom:15px; margin-left:0px; 
                margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;"><br /></p>
                <div> 
                    {}
                </div>
            </body>
        </html>
        '''.format(title, source_book, school, class_lvl_spell, components, casting_time, range_spell, mt_keys,
                   mt_values, duration, saving_throw, resistance, f_keys, f_values, description)

        self.text_desc.setText(full_text)

    def create_btn_connect(self, path, *args):
        """
        Służy do utworzenia odpowiednich powiązań z przyciskami podmenu. Wymaga ścieżki do pliku z danym opisem
        oraz argumentów w postaci przycisków Button
        :param path: ścieżka do pliku z opisem
        :param args: przyciski Button
        """
        self.submenu_create(*args)
        for i, val in enumerate(args):
            if val.isWidgetType():
                y = 'btn' + str(i + 1)
                val.pressed.connect(lambda x=y: self.description_thread(path, x))

    def description_thread(self, path, bs_id=None):
        """
        Wykonuje odczyt opisu danego podrozdziału z pliku, w osobnym wątku
        :param bs_id: id div
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

    def closeEvent(self, QCloseEvent):
        """Zamyka łącze do bazy"""
        self.db.close()

if __name__ == '__main__':
    os.chdir(normpath(join(os.getcwd(), '..\\')))
    app = QApplication(sys.argv)
    ex = Spells()
    sys.exit(app.exec_())
