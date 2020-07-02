"""Wygląd poszczególnych przycisków"""
from PySide2.QtGui import QPalette, QBrush, QColor, QFont
from PySide2.QtWidgets import QPushButton


class ButtonBack(QPushButton):
    def __init__(self, title):
        super().__init__()
        self.setText(title)
        palette = QPalette()
        font = QFont()
        font.setFamily('Krub')
        font.setBold(True)

        # Przyciski cofania
        palette.setBrush(QPalette.Active, QPalette.ButtonText, QBrush(QColor(0, 0, 0, 178)))
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, QBrush(QColor(0, 0, 0, 50)))

        palette.setBrush(QPalette.Active, QPalette.Button, QBrush(QColor('#ffdd57')))
        palette.setBrush(QPalette.Inactive, QPalette.Button, QBrush(QColor('#fff8de')))

        self.setPalette(palette)
        self.setFont(font)


class Button(QPushButton):
    def __init__(self, title):
        super().__init__()
        self.setText(title)
        palette = QPalette()

        # Przyciski nieaktywne
        palette.setBrush(QPalette.Disabled, QPalette.Button, QBrush(QColor(241, 70, 104, 0)))
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, QBrush(QColor(255, 255, 255, 255)))

        # Przyciski aktywne
        palette.setBrush(QPalette.Active, QPalette.Button, QBrush(QColor(238, 246, 252)))
        palette.setBrush(QPalette.Inactive, QPalette.Button, QBrush(QColor(255, 255, 255)))

        palette.setBrush(QPalette.Active, QPalette.ButtonText, QBrush(QColor(29, 114, 170)))
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, QBrush(QColor(54, 54, 54, 128)))

        self.setPalette(palette)


class ButtonAdd(QPushButton):
    def __init__(self, title):
        super().__init__()
        self.setText(title)
        palette = QPalette()
        font = QFont()
        font.setFamily('Krub')
        font.setBold(True)

        # Przyciski dodawania
        palette.setBrush(QPalette.Active, QPalette.ButtonText, QBrush(QColor(250, 250, 250, 178)))
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, QBrush(QColor(0, 0, 0, 50)))

        palette.setBrush(QPalette.Active, QPalette.Button, QBrush(QColor('#4d9032')))
        palette.setBrush(QPalette.Inactive, QPalette.Button, QBrush(QColor('#ceeac3')))

        self.setPalette(palette)
        self.setFont(font)


class ButtonDelete(QPushButton):
    def __init__(self, title):
        super().__init__()
        self.setText(title)
        palette = QPalette()

        # Przyciski usuwania
        palette.setBrush(QPalette.Active, QPalette.ButtonText, QBrush(QColor(63, 11, 15, 178)))
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, QBrush(QColor(0, 0, 0, 50)))

        palette.setBrush(QPalette.Active, QPalette.Button, QBrush(QColor('#E6717C')))
        palette.setBrush(QPalette.Inactive, QPalette.Button, QBrush(QColor('#F4C2C7')))

        self.setPalette(palette)


class ButtonEdit(QPushButton):
    def __init__(self, title):
        super().__init__()
        self.setText(title)
        palette = QPalette()

        # Przyciski edytowania
        palette.setBrush(QPalette.Active, QPalette.ButtonText, QBrush(QColor(9, 64, 73, 178)))
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, QBrush(QColor(0, 0, 0, 50)))

        palette.setBrush(QPalette.Active, QPalette.Button, QBrush(QColor('#2EABBF')))
        palette.setBrush(QPalette.Inactive, QPalette.Button, QBrush(QColor('#D0ECF0')))

        self.setPalette(palette)
