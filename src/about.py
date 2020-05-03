# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'O_mnievQjsRq.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from platform import python_version

import PySide2
from PySide2.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide2.QtGui import (QFont, QIcon, QPixmap, QPalette, QLinearGradient, QColor, QBrush)
from PySide2.QtWidgets import QLabel, QFormLayout, QVBoxLayout, QHBoxLayout, QSizePolicy, QApplication, QWidget


class Ui_About(object):
    """
    Klasa odpowiadająca za okienko O mnie
    """

    def __init__(self, obj_about, path_svg="../resources/icons/dice.svg"):
        self.lbl_stopka = QLabel(obj_about)
        self.lbl_python_version = QLabel(obj_about)
        self.lbl_pyside2_version = QLabel(obj_about)
        self.lbl_pyside2 = QLabel(obj_about)
        self.lbl_dnd_version = QLabel(obj_about)
        self.lbl_dnd = QLabel(obj_about)
        self.lbl_python = QLabel(obj_about)
        self.fbox = QFormLayout()
        self.lbl_opis = QLabel(obj_about)
        self.lbl_tytul = QLabel(obj_about)
        self.vbox = QVBoxLayout()
        self.lbl_icon = QLabel(obj_about)
        self.hbox = QHBoxLayout()
        self.verticalLayout_2 = QVBoxLayout(obj_about)
        self.setupUi(obj_about, path_svg)

    def setupUi(self, obj_about, path_svg):
        """
        Inicjalizuje wygląd okna
        :param obj_about: QWidget
        """
        palette = QPalette()

        grad = QLinearGradient(0, 200, 600, 300)
        grad.setColorAt(0.0, QColor(255,228,181))
        grad.setColorAt(1.0, QColor(255,250,205))
        brush = QBrush(grad)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        obj_about.setPalette(palette)

        if not obj_about.objectName():
            obj_about.setObjectName(u"About")
        obj_about.setFixedSize(700, 400)
        font = QFont()
        font.setFamily(u"Baloo Tammudu 2")
        font.setPointSize(11)
        obj_about.setFont(font)
        icon = QIcon()
        icon.addFile(path_svg, QSize(), QIcon.Normal, QIcon.Off)
        obj_about.setWindowIcon(icon)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.hbox.setObjectName(u"hbox")
        self.lbl_icon.setObjectName(u"lbl_icon")
        self.lbl_icon.setMaximumSize(QSize(300, 300))
        self.lbl_icon.setPixmap(QPixmap(path_svg))
        self.lbl_icon.setScaledContents(True)

        self.hbox.addWidget(self.lbl_icon)

        self.vbox.setObjectName(u"vbox")
        self.lbl_tytul.setObjectName(u"lbl_tytul")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_tytul.sizePolicy().hasHeightForWidth())
        self.lbl_tytul.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"Amarante")
        font1.setPointSize(14)
        self.lbl_tytul.setFont(font1)
        self.lbl_tytul.setAlignment(Qt.AlignCenter)

        self.vbox.addWidget(self.lbl_tytul)

        self.lbl_opis.setObjectName(u"lbl_opis")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_opis.sizePolicy().hasHeightForWidth())
        self.lbl_opis.setSizePolicy(sizePolicy1)
        self.lbl_opis.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.lbl_opis.setWordWrap(True)

        self.vbox.addWidget(self.lbl_opis)

        self.fbox.setObjectName(u"fbox")
        self.fbox.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.fbox.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.fbox.setHorizontalSpacing(60)
        self.fbox.setVerticalSpacing(20)
        self.fbox.setContentsMargins(20, -1, -1, -1)
        self.lbl_python.setObjectName(u"lbl_python")

        self.fbox.setWidget(0, QFormLayout.LabelRole, self.lbl_python)

        self.lbl_pyside2.setObjectName(u"lbl_pyside2")

        self.lbl_dnd.setObjectName(u"lbl_dnd")

        self.fbox.setWidget(1, QFormLayout.LabelRole, self.lbl_pyside2)

        self.lbl_pyside2_version.setObjectName(u"lbl_pyside2_version")

        self.lbl_dnd_version.setObjectName(u"lbl_dnd_version")

        self.fbox.setWidget(1, QFormLayout.FieldRole, self.lbl_pyside2_version)

        self.lbl_python_version.setObjectName(u"lbl_python_version")

        self.fbox.setWidget(0, QFormLayout.FieldRole, self.lbl_python_version)

        self.fbox.setWidget(2, QFormLayout.LabelRole, self.lbl_dnd)

        self.fbox.setWidget(2, QFormLayout.FieldRole, self.lbl_dnd_version)

        self.vbox.addLayout(self.fbox)

        self.hbox.addLayout(self.vbox)

        self.verticalLayout_2.addLayout(self.hbox)

        self.lbl_stopka.setObjectName(u"lbl_stopka")
        font2 = QFont()
        font2.setPointSize(10)
        self.lbl_stopka.setFont(font2)
        self.lbl_stopka.setScaledContents(True)
        self.lbl_stopka.setAlignment(Qt.AlignCenter)
        self.lbl_stopka.setOpenExternalLinks(True)

        self.verticalLayout_2.addWidget(self.lbl_stopka)

        self.retranslateUi(obj_about)

        QMetaObject.connectSlotsByName(obj_about)

    # setupUi

    def retranslateUi(self, obj_about):
        """
        Inicjalizuje translację
        :param obj_about: QWidget
        """
        obj_about.setWindowTitle(QCoreApplication.translate("About", u"O mnie...", None))
        self.lbl_icon.setText("")
        self.lbl_tytul.setText(QCoreApplication.translate("About", u"Dungeon Dice", None))
        self.lbl_opis.setText(QCoreApplication.translate("About",
                                                         u"Program zawieraj\u0105cy opis wszystkich zakl\u0119\u0107 do D&D edycji 3.5",
                                                         None))
        self.lbl_python.setText(QCoreApplication.translate("About", u"Python:", None))
        self.lbl_pyside2.setText(QCoreApplication.translate("About", u"PySide2:", None))
        self.lbl_dnd.setText(QCoreApplication.translate("About", u"Wersja programu:", None))
        self.lbl_dnd_version.setText(QCoreApplication.translate("About", u"0.0.1", None))
        self.lbl_pyside2_version.setText(QCoreApplication.translate("About", PySide2.__version__, None))
        self.lbl_python_version.setText(QCoreApplication.translate("About", python_version(), None))
        self.lbl_stopka.setText(QCoreApplication.translate("About",
                                                           u"<html><head/><body><div>Icons made by <a href='https://www.flaticon.com/authors/freepik' title='Freepik'>Freepik</a> from <a href='https://www.flaticon.com/' title='Flaticon'>www.flaticon.com</a></div><p>Wesprzyj: <a href=\"https://www.paypal.me/lioheart\"><span style=\" font-weight:600; color:#000000;\">https://www.paypal.me/lioheart</span></a></p></body></html>",
                                                           None))
    # retranslateUi


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    about = QWidget()
    ui = Ui_About(about)
    about.show()
    sys.exit(app.exec_())
