import datetime as dt
import os, sys, json
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *
#from mygui import Ui_MainWindow
from hd_defs import ex


class MainWindow(ex):
    def __init__(s, form):
        super().__init__()
        s.setupUi(form)
        s.UIset()
        
    #main function
    def UIset(s):
        s.calcmode = 0
        s.mapmode = 0
        s.loadc()
        s.arr = [s.img_consult,s.label_info,s.button_next,s.button_back,\
                 s.button_map]
        s.arr2 = [s.lc_info,s.lc_indev]
        s.arr3 = [s.img_consult,s.label_info,s.button_next,s.button_back,\
                  s.button_calc]
        s.arr4 = [s.mapmetro]
        s.stud_group.hide()
        s.cabs_group.hide()
        s.abitur_group.hide()
        #1
        s.button_abit.clicked.connect(s.bt_abit_clicked)
        s.button_stud.clicked.connect(s.bt_stud_clicked)
        #2
        s.button_mainmenu.clicked.connect(s.bt_mainmenu_clicked)
        s.button_next.clicked.connect(s.bt_next_clicked)
        s.button_back.clicked.connect(s.bt_back_clicked)
        s.button_calc.clicked.connect(s.bt_calc_clicked)
        s.button_map.clicked.connect(s.bt_map_clicked)
        #3
        s.button_mainmenu_2.clicked.connect(s.bt_mainmenu_clicked)
        s.button_gorasp.clicked.connect(s.bt_gorasp_clicked)
        s.button_gonav.clicked.connect(s.bt_gonav_clicked)
        s.button_gocab.clicked.connect(s.bt_gocab_clicked)
        #4
        s.button_backtostud.clicked.connect(s.bt_backtostud_clicked)



if __name__=='__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = MainWindow(window)
    window.show()
    sys.exit(app.exec_())
