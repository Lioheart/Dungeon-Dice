"""Główne okno programu"""

from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import QIcon, QFont, QBrush, QColor, QPalette, QLinearGradient
from PySide2.QtWidgets import QMainWindow, QAction, QWidget, QVBoxLayout, QScrollArea, QPushButton, QSizePolicy, \
    QStackedWidget

from check_state import updating
from src.about import Ui_About
from src.licence import Licence
from src.magic_dnd_35 import Spells


class MenuWidget(QWidget):
    """
    Klasa Menu - wybór odpowiednich funkcji w głównym oknie
    """

    def __init__(self):
        super().__init__()
        self.scrollAreaWidgetContents = QWidget()
        self.vbox_scroll = QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollArea = QScrollArea(self)
        self.verticalLayout = QVBoxLayout(self)
        self.initUI()

    def initUI(self):
        """
        Inicjuje UI wyglądu menu głównego. Zawiera przyciski z ikonami
        """
        # widgety
        btn_spells = QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        font = QFont()
        icon = QIcon()

        # Ustawianie widgetów
        font.setFamily('Krub')
        font.setBold(True)
        font.setPointSize(16)
        icon.addFile('./resources/icons/spellbook.svg', QSize(), QIcon.Normal, QIcon.Off)

        btn_spells.setMinimumSize(QSize(0, 72))
        btn_spells.setSizePolicy(sizePolicy)
        btn_spells.setFont(font)
        btn_spells.setIcon(icon)
        btn_spells.setIconSize(QSize(48, 48))
        btn_spells.setText('Księga czarów')

        # Ustawianie Slotów i sygnałów
        btn_spells.clicked.connect(lambda: self.parent().setCurrentIndex(1))

        # Ustawianie widoku
        self.vbox_scroll.addWidget(btn_spells, 0, Qt.AlignHCenter)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.show()


class MainWindow(QMainWindow):
    """
    Klasa głównego okna
    """

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.about_widget = QWidget()
        self.licence = Licence()
        self.setWindowTitle("Dungeon Dice")
        self.verticalLayout = QVBoxLayout(self)
        self.initUI()

    def initUI(self):
        """
        Inicjuje wygląd UI
        """
        # Widok
        palette = QPalette()
        palette.setBrush(QPalette.Normal, QPalette.Button, QBrush(QColor('#effaf3')))
        palette.setBrush(QPalette.Inactive, QPalette.Button, QBrush(QColor('#effaf3')))

        palette.setBrush(QPalette.Normal, QPalette.ButtonText, QBrush(QColor('#257942')))
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, QBrush(QColor(72, 199, 116)))

        grad = QLinearGradient(0, 0, 0, self.size().height())
        grad.setColorAt(0.0, QColor(255, 255, 255))
        grad.setColorAt(1.0, QColor('#e5e5e5'))
        palette.setBrush(QPalette.Active, QPalette.Window, QBrush(grad))

        # Ustawienie ikony
        icon = QIcon()
        icon.addFile('./resources/icons/dice.svg', QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        # Ustawienie fontu
        font = QFont()
        font.setFamily('Krub')
        font.setPointSize(11)
        self.setFont(font)

        # Widgety
        spells_widget = Spells()
        menu_widget = MenuWidget()
        centralwidget = QWidget(self)
        stackedWidget = QStackedWidget(centralwidget)

        # Layouty
        verticalLayout = QVBoxLayout(centralwidget)

        # Kontrolki
        menubar = self.menuBar()
        viewMenu = menubar.addMenu('O mnie...')
        act_licence = QAction('Licencja otwartej gry', self)
        act_about = QAction('O mnie', self)
        act_update = QAction('Sprawdź dostępność aktualizacji', self)
        menubar.setFont(font)

        # Ustawianie kontrolek
        verticalLayout.addWidget(stackedWidget)
        stackedWidget.addWidget(menu_widget)
        stackedWidget.addWidget(spells_widget)
        stackedWidget.setCurrentIndex(0)
        viewMenu.addAction(act_licence)
        viewMenu.addAction(act_update)
        viewMenu.addAction(act_about)
        act_about.setFont(font)
        act_licence.setFont(font)
        act_update.setFont(font)

        # Ustawianie widoku
        stackedWidget.setPalette(palette)
        self.setCentralWidget(centralwidget)

        # Ustawianie akcji
        act_about.triggered.connect(self.about)
        act_update.triggered.connect(updating)
        act_licence.triggered.connect(lambda: self.licence.show())

    def about(self):
        """
        Metoda ta otwiera okienko O mnie
        """
        Ui_About(self.about_widget, './resources/icons/dice.svg')
        self.about_widget.show()
