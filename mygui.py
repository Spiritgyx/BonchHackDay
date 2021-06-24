# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\projects\hackday\gui.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.choose_group = QtWidgets.QGroupBox(self.centralwidget)
        self.choose_group.setEnabled(True)
        self.choose_group.setGeometry(QtCore.QRect(0, 0, 800, 580))
        self.choose_group.setStyleSheet("QPushButton{\n"
"font: 36pt \"Arial Narrow\";\n"
"}\n"
"QPushButton::hover{\n"
"selection-background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton::hold{\n"
"background-color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton::pressed{\n"
"background-color :rgb(255, 255, 117);\n"
"}\n"
"\n"
"\n"
"")
        self.choose_group.setTitle("")
        self.choose_group.setObjectName("choose_group")
        self.bonch_logo = QtWidgets.QLabel(self.choose_group)
        self.bonch_logo.setGeometry(QtCore.QRect(5, 5, 240, 40))
        self.bonch_logo.setText("")
        self.bonch_logo.setPixmap(QtGui.QPixmap("images/logo_footer.png"))
        self.bonch_logo.setObjectName("bonch_logo")
        self.welcome_logo = QtWidgets.QLabel(self.choose_group)
        self.welcome_logo.setGeometry(QtCore.QRect(300, 0, 200, 50))
        self.welcome_logo.setText("")
        self.welcome_logo.setPixmap(QtGui.QPixmap("images/welcome_logo.png"))
        self.welcome_logo.setObjectName("welcome_logo")
        self.PsyNabla_logo = QtWidgets.QLabel(self.choose_group)
        self.PsyNabla_logo.setGeometry(QtCore.QRect(690, 20, 50, 20))
        self.PsyNabla_logo.setText("")
        self.PsyNabla_logo.setObjectName("PsyNabla_logo")
        self.button_abit = QtWidgets.QPushButton(self.choose_group)
        self.button_abit.setGeometry(QtCore.QRect(0, 50, 400, 460))
        self.button_abit.setStyleSheet("")
        self.button_abit.setObjectName("button_abit")
        self.button_stud = QtWidgets.QPushButton(self.choose_group)
        self.button_stud.setEnabled(True)
        self.button_stud.setGeometry(QtCore.QRect(400, 50, 400, 460))
        self.button_stud.setObjectName("button_stud")
        self.test = QtWidgets.QLabel(self.choose_group)
        self.test.setGeometry(QtCore.QRect(20, 520, 271, 16))
        self.test.setObjectName("test")
        self.abitur_group = QtWidgets.QGroupBox(self.centralwidget)
        self.abitur_group.setEnabled(True)
        self.abitur_group.setGeometry(QtCore.QRect(0, 0, 800, 580))
        self.abitur_group.setTitle("")
        self.abitur_group.setObjectName("abitur_group")
        self.bonch_logo_2 = QtWidgets.QLabel(self.abitur_group)
        self.bonch_logo_2.setGeometry(QtCore.QRect(5, 5, 240, 40))
        self.bonch_logo_2.setStyleSheet("")
        self.bonch_logo_2.setText("")
        self.bonch_logo_2.setPixmap(QtGui.QPixmap("images/logo_footer.png"))
        self.bonch_logo_2.setObjectName("bonch_logo_2")
        self.welcome_logo_2 = QtWidgets.QLabel(self.abitur_group)
        self.welcome_logo_2.setGeometry(QtCore.QRect(300, 0, 200, 50))
        self.welcome_logo_2.setText("")
        self.welcome_logo_2.setPixmap(QtGui.QPixmap("images/welcome_logo.png"))
        self.welcome_logo_2.setObjectName("welcome_logo_2")
        self.PsyNabla_logo_2 = QtWidgets.QLabel(self.abitur_group)
        self.PsyNabla_logo_2.setGeometry(QtCore.QRect(720, 10, 50, 20))
        self.PsyNabla_logo_2.setText("")
        self.PsyNabla_logo_2.setObjectName("PsyNabla_logo_2")
        self.img_bg_abit = QtWidgets.QLabel(self.abitur_group)
        self.img_bg_abit.setGeometry(QtCore.QRect(0, 0, 800, 510))
        self.img_bg_abit.setText("")
        self.img_bg_abit.setPixmap(QtGui.QPixmap("images/background.png"))
        self.img_bg_abit.setObjectName("img_bg_abit")
        self.img_consult = QtWidgets.QLabel(self.abitur_group)
        self.img_consult.setGeometry(QtCore.QRect(0, 50, 800, 460))
        self.img_consult.setText("")
        self.img_consult.setPixmap(QtGui.QPixmap("images/consult.png"))
        self.img_consult.setObjectName("img_consult")
        self.button_next = QtWidgets.QPushButton(self.abitur_group)
        self.button_next.setGeometry(QtCore.QRect(670, 470, 60, 40))
        self.button_next.setStyleSheet("QPushButton{\n"
"border-image: url(\"images/knopka1.png\");\n"
"}\n"
"QPushButton::hover{\n"
"border-image: url(\"images/knopka1h.png\");\n"
"}\n"
"QPushButton::pressed{\n"
"border-image: url(\"images/knopka1p.png\");\n"
"}")
        self.button_next.setText("")
        self.button_next.setObjectName("button_next")
        self.button_back = QtWidgets.QPushButton(self.abitur_group)
        self.button_back.setGeometry(QtCore.QRect(600, 470, 60, 40))
        self.button_back.setStyleSheet("QPushButton{\n"
"border-image: url(\"images/knopka2.png\");\n"
"}\n"
"QPushButton::hover{\n"
"border-image: url(\"images/knopka2h.png\");\n"
"}\n"
"QPushButton::pressed{\n"
"border-image: url(\"images/knopka2p.png\");\n"
"}")
        self.button_back.setText("")
        self.button_back.setObjectName("button_back")
        self.button_mainmenu = QtWidgets.QPushButton(self.abitur_group)
        self.button_mainmenu.setGeometry(QtCore.QRect(325, 520, 150, 40))
        self.button_mainmenu.setObjectName("button_mainmenu")
        self.img_hat = QtWidgets.QLabel(self.abitur_group)
        self.img_hat.setGeometry(QtCore.QRect(0, 0, 800, 50))
        self.img_hat.setText("")
        self.img_hat.setPixmap(QtGui.QPixmap("images/hat1.png"))
        self.img_hat.setObjectName("img_hat")
        self.label_info = QtWidgets.QLabel(self.abitur_group)
        self.label_info.setGeometry(QtCore.QRect(230, 80, 501, 391))
        self.label_info.setText("")
        self.label_info.setObjectName("label_info")
        self.test_2 = QtWidgets.QLabel(self.abitur_group)
        self.test_2.setGeometry(QtCore.QRect(20, 520, 271, 16))
        self.test_2.setObjectName("test_2")
        self.button_calc = QtWidgets.QPushButton(self.abitur_group)
        self.button_calc.setGeometry(QtCore.QRect(735, 90, 60, 60))
        self.button_calc.setStyleSheet("QPushButton{\n"
"border-image:url(\"images/calc.png\");\n"
"}\n"
"QPushButton::hover{\n"
"border-image:url(\"images/calch.png\");\n"
"}\n"
"QPushButton::pressed{\n"
"border-image:url(\"images/calcp.png\");\n"
"}")
        self.button_calc.setText("")
        self.button_calc.setObjectName("button_calc")
        self.button_map = QtWidgets.QPushButton(self.abitur_group)
        self.button_map.setGeometry(QtCore.QRect(735, 170, 60, 60))
        self.button_map.setStyleSheet("QPushButton{\n"
"border-image:url(\"images/map.png\");\n"
"}\n"
"QPushButton::hover{\n"
"border-image:url(\"images/maph.png\");\n"
"}\n"
"QPushButton::pressed{\n"
"border-image:url(\"images/mapp.png\");\n"
"}")
        self.button_map.setText("")
        self.button_map.setObjectName("button_map")
        self.mapmetro = QtWidgets.QLabel(self.abitur_group)
        self.mapmetro.setGeometry(QtCore.QRect(10, 60, 720, 450))
        self.mapmetro.setStyleSheet("QLabel{\n"
"image:url(\"images/mapmetro.png\");\n"
"}")
        self.mapmetro.setObjectName("mapmetro")
        self.lc_info = QtWidgets.QLabel(self.abitur_group)
        self.lc_info.setGeometry(QtCore.QRect(30, 50, 491, 20))
        self.lc_info.setObjectName("lc_info")
        self.lc_indev = QtWidgets.QTextBrowser(self.abitur_group)
        self.lc_indev.setGeometry(QtCore.QRect(30, 90, 256, 192))
        self.lc_indev.setObjectName("lc_indev")
        self.img_bg_abit.raise_()
        self.img_hat.raise_()
        self.bonch_logo_2.raise_()
        self.welcome_logo_2.raise_()
        self.PsyNabla_logo_2.raise_()
        self.img_consult.raise_()
        self.button_next.raise_()
        self.button_back.raise_()
        self.button_mainmenu.raise_()
        self.label_info.raise_()
        self.test_2.raise_()
        self.button_calc.raise_()
        self.button_map.raise_()
        self.mapmetro.raise_()
        self.lc_info.raise_()
        self.lc_indev.raise_()
        self.stud_group = QtWidgets.QGroupBox(self.centralwidget)
        self.stud_group.setEnabled(True)
        self.stud_group.setGeometry(QtCore.QRect(0, 0, 800, 580))
        self.stud_group.setTitle("")
        self.stud_group.setObjectName("stud_group")
        self.bonch_logo_3 = QtWidgets.QLabel(self.stud_group)
        self.bonch_logo_3.setGeometry(QtCore.QRect(5, 5, 240, 40))
        self.bonch_logo_3.setStyleSheet("")
        self.bonch_logo_3.setText("")
        self.bonch_logo_3.setPixmap(QtGui.QPixmap("images/logo_footer.png"))
        self.bonch_logo_3.setObjectName("bonch_logo_3")
        self.img_bg_abit_2 = QtWidgets.QLabel(self.stud_group)
        self.img_bg_abit_2.setGeometry(QtCore.QRect(0, 0, 800, 510))
        self.img_bg_abit_2.setText("")
        self.img_bg_abit_2.setPixmap(QtGui.QPixmap("images/background.png"))
        self.img_bg_abit_2.setObjectName("img_bg_abit_2")
        self.welcome_logo_3 = QtWidgets.QLabel(self.stud_group)
        self.welcome_logo_3.setGeometry(QtCore.QRect(300, 0, 200, 50))
        self.welcome_logo_3.setText("")
        self.welcome_logo_3.setPixmap(QtGui.QPixmap("images/welcome_logo.png"))
        self.welcome_logo_3.setObjectName("welcome_logo_3")
        self.img_consult_2 = QtWidgets.QLabel(self.stud_group)
        self.img_consult_2.setGeometry(QtCore.QRect(0, 50, 800, 460))
        self.img_consult_2.setText("")
        self.img_consult_2.setPixmap(QtGui.QPixmap("images/consult.png"))
        self.img_consult_2.setObjectName("img_consult_2")
        self.img_hat_2 = QtWidgets.QLabel(self.stud_group)
        self.img_hat_2.setGeometry(QtCore.QRect(0, 0, 800, 50))
        self.img_hat_2.setText("")
        self.img_hat_2.setPixmap(QtGui.QPixmap("images/hat1.png"))
        self.img_hat_2.setObjectName("img_hat_2")
        self.test_3 = QtWidgets.QLabel(self.stud_group)
        self.test_3.setGeometry(QtCore.QRect(20, 520, 271, 16))
        self.test_3.setObjectName("test_3")
        self.button_mainmenu_2 = QtWidgets.QPushButton(self.stud_group)
        self.button_mainmenu_2.setGeometry(QtCore.QRect(325, 520, 150, 40))
        self.button_mainmenu_2.setObjectName("button_mainmenu_2")
        self.label_hello = QtWidgets.QLabel(self.stud_group)
        self.label_hello.setGeometry(QtCore.QRect(340, 90, 271, 71))
        self.label_hello.setObjectName("label_hello")
        self.button_gorasp = QtWidgets.QPushButton(self.stud_group)
        self.button_gorasp.setGeometry(QtCore.QRect(400, 170, 150, 41))
        self.button_gorasp.setObjectName("button_gorasp")
        self.button_gonav = QtWidgets.QPushButton(self.stud_group)
        self.button_gonav.setGeometry(QtCore.QRect(400, 230, 150, 40))
        self.button_gonav.setObjectName("button_gonav")
        self.button_gocab = QtWidgets.QPushButton(self.stud_group)
        self.button_gocab.setGeometry(QtCore.QRect(400, 290, 150, 40))
        self.button_gocab.setObjectName("button_gocab")
        self.img_bg_abit_2.raise_()
        self.img_hat_2.raise_()
        self.bonch_logo_3.raise_()
        self.welcome_logo_3.raise_()
        self.img_consult_2.raise_()
        self.test_3.raise_()
        self.button_mainmenu_2.raise_()
        self.label_hello.raise_()
        self.button_gorasp.raise_()
        self.button_gonav.raise_()
        self.button_gocab.raise_()
        self.cabs_group = QtWidgets.QGroupBox(self.centralwidget)
        self.cabs_group.setEnabled(True)
        self.cabs_group.setGeometry(QtCore.QRect(0, 0, 800, 580))
        self.cabs_group.setTitle("")
        self.cabs_group.setObjectName("cabs_group")
        self.img_bg_abit_3 = QtWidgets.QLabel(self.cabs_group)
        self.img_bg_abit_3.setGeometry(QtCore.QRect(0, 0, 800, 510))
        self.img_bg_abit_3.setText("")
        self.img_bg_abit_3.setPixmap(QtGui.QPixmap("images/background.png"))
        self.img_bg_abit_3.setObjectName("img_bg_abit_3")
        self.img_hat_3 = QtWidgets.QLabel(self.cabs_group)
        self.img_hat_3.setEnabled(False)
        self.img_hat_3.setGeometry(QtCore.QRect(0, 0, 800, 50))
        self.img_hat_3.setText("")
        self.img_hat_3.setPixmap(QtGui.QPixmap("images/hat1.png"))
        self.img_hat_3.setObjectName("img_hat_3")
        self.bonch_logo_4 = QtWidgets.QLabel(self.cabs_group)
        self.bonch_logo_4.setGeometry(QtCore.QRect(5, 5, 240, 40))
        self.bonch_logo_4.setStyleSheet("")
        self.bonch_logo_4.setText("")
        self.bonch_logo_4.setPixmap(QtGui.QPixmap("images/logo_footer.png"))
        self.bonch_logo_4.setObjectName("bonch_logo_4")
        self.text_1corp = QtWidgets.QTextBrowser(self.cabs_group)
        self.text_1corp.setEnabled(True)
        self.text_1corp.setGeometry(QtCore.QRect(800, 60, 390, 440))
        self.text_1corp.setAutoFillBackground(True)
        self.text_1corp.setObjectName("text_1corp")
        self.test_4 = QtWidgets.QLabel(self.cabs_group)
        self.test_4.setGeometry(QtCore.QRect(20, 520, 271, 16))
        self.test_4.setObjectName("test_4")
        self.button_backtostud = QtWidgets.QPushButton(self.cabs_group)
        self.button_backtostud.setGeometry(QtCore.QRect(325, 520, 150, 40))
        self.button_backtostud.setObjectName("button_backtostud")
        self.text_2corp = QtWidgets.QTextBrowser(self.cabs_group)
        self.text_2corp.setGeometry(QtCore.QRect(800, 60, 390, 440))
        self.text_2corp.setAutoFillBackground(False)
        self.text_2corp.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.text_2corp.setObjectName("text_2corp")
        self.label_1corp = QtWidgets.QLabel(self.cabs_group)
        self.label_1corp.setGeometry(QtCore.QRect(10, 60, 390, 440))
        self.label_1corp.setWordWrap(True)
        self.label_1corp.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_1corp.setObjectName("label_1corp")
        self.label_2corp = QtWidgets.QLabel(self.cabs_group)
        self.label_2corp.setGeometry(QtCore.QRect(400, 60, 390, 440))
        self.label_2corp.setAcceptDrops(False)
        self.label_2corp.setWordWrap(True)
        self.label_2corp.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_2corp.setObjectName("label_2corp")
        self.img_podarok = QtWidgets.QLabel(self.cabs_group)
        self.img_podarok.setGeometry(QtCore.QRect(10, 60, 780, 440))
        self.img_podarok.setText("")
        self.img_podarok.setPixmap(QtGui.QPixmap("images/podarok.png"))
        self.img_podarok.setObjectName("img_podarok")
        self.line = QtWidgets.QFrame(self.cabs_group)
        self.line.setGeometry(QtCore.QRect(395, 60, 3, 440))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.img_bg_abit_3.raise_()
        self.img_podarok.raise_()
        self.img_hat_3.raise_()
        self.bonch_logo_4.raise_()
        self.text_1corp.raise_()
        self.test_4.raise_()
        self.button_backtostud.raise_()
        self.text_2corp.raise_()
        self.label_1corp.raise_()
        self.label_2corp.raise_()
        self.line.raise_()
        self.choose_group.raise_()
        self.stud_group.raise_()
        self.cabs_group.raise_()
        self.abitur_group.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Program"))
        self.button_abit.setText(_translate("MainWindow", "Абитуриенту"))
        self.button_stud.setText(_translate("MainWindow", "Студенту"))
        self.test.setText(_translate("MainWindow", "Язык             Обратная связь (в разработке)"))
        self.button_mainmenu.setText(_translate("MainWindow", "Главное меню"))
        self.test_2.setText(_translate("MainWindow", "Язык             Обратная связь (в разработке)"))
        self.mapmetro.setText(_translate("MainWindow", "TextLabel"))
        self.lc_info.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Выберите предмет по профилю и введите кол-во баллов по предметам</span></p></body></html>"))
        self.lc_indev.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">В РАЗРАБОТКЕ</span></p></body></html>"))
        self.test_3.setText(_translate("MainWindow", "Язык             Обратная связь (в разработке)"))
        self.button_mainmenu_2.setText(_translate("MainWindow", "Главное меню"))
        self.label_hello.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Здравствуй, студент!</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Чем тебе помочь?</span></p></body></html>"))
        self.button_gorasp.setText(_translate("MainWindow", "Расписание"))
        self.button_gonav.setText(_translate("MainWindow", "Найти кабинет"))
        self.button_gocab.setText(_translate("MainWindow", "Список важных кабинетов"))
        self.text_1corp.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">1 корпус:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">102</span><span style=\" font-size:10pt;\"> - Медпункт (с 10:00 до 15:00)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">109</span><span style=\" font-size:10pt;\"> - Договорной отдел (пн-ср,пт 10:00-13:00,</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">14:00-16:30, чт приема нет)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">119</span><span style=\" font-size:10pt;\"> - Студенческий совет</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">121</span><span style=\" font-size:10pt;\"> - Касса</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">227</span><span style=\" font-size:10pt;\"> - Военно-учетный стол (второй отдел)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">(пн,вт,чт 10:00-16:00;ср приема нет; пт 10:00-15:00; обед 13:00-14:00)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">423 </span><span style=\" font-size:10pt;\">- Научный фонд (электронный читательский зал)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">503 </span><span style=\" font-size:10pt;\">- Общий отдел (10:00-13:00, 14:00-16:00)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">522 </span><span style=\" font-size:10pt;\">- Студ. отдел кадров (пн,вт,чт 11:00-13:00, 15:00-17:00;ср приема нет;пт 11:00-13:00)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">625 </span><span style=\" font-size:10pt;\">- Группа по расчету стипендии</span></p></body></html>"))
        self.test_4.setText(_translate("MainWindow", "Язык             Обратная связь (в разработке)"))
        self.button_backtostud.setText(_translate("MainWindow", "Назад"))
        self.text_2corp.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">2 корпус:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">100 </span><span style=\" font-size:10pt;\">- Читательский зал (пн,чт 11:00-17:45; вт,ср 11:00-18:45; пт 11:00-16:45; сб,вс Выходной; проветривание 15:00-15:15, 17:00-17:15)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">103</span><span style=\" font-size:10pt;\"> - Абонемент младших курсов</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">108 </span><span style=\" font-size:10pt;\">- Абонемент старших курсов (пн,чт 11:00-18:45; вт,ср 11:00-17:45; пт 11:00-16:45; сб,вс выходной; проветривание 15:00-15:15, 17:00-17:15)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">117 </span><span style=\" font-size:10pt;\">- Бюро пропусков (пн-пт 10:30-17:00; сб,вс выходной; обед 13:00-14:00)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">139</span><span style=\" font-size:10pt;\"> - Отдел по социальной работе</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">148</span><span style=\" font-size:10pt;\"> - Департамент &quot;Студенческий городок&quot; (пн 10:00-13:00; вт,ср,чт 10:00-16:30; пт приема нет; обед 13:00-14:00)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">150</span><span style=\" font-size:10pt;\"> - Начальник департамента &quot;Студенческий городок&quot;</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">227 </span><span style=\" font-size:10pt;\">- Управление по воспитательной работе</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">306 </span><span style=\" font-size:10pt;\">- Профсоюзный комитет (пн,чт,пт 11:00-13:00,14:00-16:00; вт 12:00-13:00,14:00-16:00;ср приема нет)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">341 </span><span style=\" font-size:10pt;\">- НОЦ &quot;Медиацентр&quot;</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">364</span><span style=\" font-size:10pt;\"> - Психологическая служба</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">368</span><span style=\" font-size:10pt;\"> - Научно-течнический совет</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">347 </span><span style=\" font-size:10pt;\">- Отдел научно-исследовательской работы студентов</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">370</span><span style=\" font-size:10pt;\"> - Начальник Управления организации научной работы и подготовки научных кадров</span></p></body></html>"))
        self.label_1corp.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">1 корпус:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">102</span><span style=\" font-size:10pt;\"> - Медпункт (с 10:00 до 15:00)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">109</span><span style=\" font-size:10pt;\"> - Договорной отдел (пн-ср,пт 10:00-13:00,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">14:00-16:30, чт приема нет)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">119</span><span style=\" font-size:10pt;\"> - Студенческий совет</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">121</span><span style=\" font-size:10pt;\"> - Касса</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">227</span><span style=\" font-size:10pt;\"> - Военно-учетный стол (второй отдел)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">(пн,вт,чт 10:00-16:00;ср приема нет; пт 10:00-15:00; обед 13:00-14:00)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">423 </span><span style=\" font-size:10pt;\">- Научный фонд (электронный читательский зал)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">503 </span><span style=\" font-size:10pt;\">- Общий отдел (10:00-13:00, 14:00-16:00)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">522 </span><span style=\" font-size:10pt;\">- Студ. отдел кадров (пн,вт,чт 11:00-13:00, 15:00-17:00;ср приема нет;пт 11:00-13:00)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">625 </span><span style=\" font-size:10pt;\">- Группа по расчету стипендии</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))
        self.label_2corp.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">2 корпус:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">100 </span><span style=\" font-size:10pt;\">- Читательский зал (пн,чт 11:00-17:45; вт,ср 11:00-18:45; пт 11:00-16:45; сб,вс Выходной; проветривание 15:00-15:15, 17:00-17:15)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">103</span><span style=\" font-size:10pt;\"> - Абонемент младших курсов</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">108 </span><span style=\" font-size:10pt;\">- Абонемент старших курсов (пн,чт 11:00-18:45; вт,ср 11:00-17:45; пт 11:00-16:45; сб,вс выходной; проветривание 15:00-15:15, 17:00-17:15)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">117 </span><span style=\" font-size:10pt;\">- Бюро пропусков (пн-пт 10:30-17:00; сб,вс выходной; обед 13:00-14:00)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">139</span><span style=\" font-size:10pt;\"> - Отдел по социальной работе</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">148</span><span style=\" font-size:10pt;\"> - Департамент &quot;Студенческий городок&quot; (пн 10:00-13:00; вт,ср,чт 10:00-16:30; пт приема нет; обед 13:00-14:00)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">150</span><span style=\" font-size:10pt;\"> - Начальник департамента &quot;Студенческий городок&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">227 </span><span style=\" font-size:10pt;\">- Управление по воспитательной работе</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">306 </span><span style=\" font-size:10pt;\">- Профсоюзный комитет (пн,чт,пт 11:00-13:00,14:00-16:00; вт 12:00-13:00,14:00-16:00;ср приема нет)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">341 </span><span style=\" font-size:10pt;\">- НОЦ &quot;Медиацентр&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">364</span><span style=\" font-size:10pt;\"> - Психологическая служба</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">368</span><span style=\" font-size:10pt;\"> - Научно-течнический совет</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">347 </span><span style=\" font-size:10pt;\">- Отдел научно-исследовательской работы студентов</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">370</span><span style=\" font-size:10pt;\"> - Начальник Управления организации научной работы и подготовки научных кадров</span></p></body></html>"))

