from mygui import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *
import rasp,nav
class ex(Ui_MainWindow):
    def __init__(s):
        pass
    #1
    #show abitur menu
    def bt_abit_clicked(s):
        s.choose_group.hide()
        s.abitur_group.show()
        s.label_info.setText(s.linfo[0])
        for i in s.arr2:
            i.hide()
        for i in s.arr4:
            i.hide()

    #show stud menu
    def bt_stud_clicked(s):
        s.choose_group.hide()
        s.stud_group.show()

    #2
    #back to choose menu
    def bt_mainmenu_clicked(s):
        s.choose_group.show()
        s.stud_group.hide()
        s.abitur_group.hide()

    #next page
    def bt_next_clicked(s):
        #next
        pass

    #prev page
    def bt_back_clicked(s):
        #prev
        pass

    def bt_calc_clicked(s):
        if s.calcmode==0:
            for i in s.arr:
                i.hide()
            for i in s.arr2:
                i.show()
            s.calcmode=1
        else:
            for i in s.arr:
                i.show()
            for i in s.arr2:
                i.hide()
            s.calcmode=0
            
    def bt_map_clicked(s):
        if s.mapmode==0:
            for i in s.arr3:
                i.hide()
            for i in s.arr4:
                i.show()
            s.mapmode=1
        else:
            for i in s.arr3:
                i.show()
            for i in s.arr4:
                i.hide()
            s.mapmode=0
    
    #3
    #open rasp program
    def bt_gorasp_clicked(s):
        #open program
        #s.raspwindow = QMainWindow()
        s.rasp = rasp.Example()
        #rasp.start()
        pass

    #open nav program
    def bt_gonav_clicked(s):
        #open program
        s.mnav = QMainWindow()
        s.nav = nav.Example(s.mnav)
        print('s2')
        s.mnav.show()
        pass

    #open cabs_group
    def bt_gocab_clicked(s):
        s.stud_group.hide()
        s.cabs_group.show()

    #4
    #back to stud_group
    def bt_backtostud_clicked(s):
        s.stud_group.show()
        s.cabs_group.hide()
    #-
    #Load consts
    def loadc(s):
        s.linfo = []
        s.linfo.append('<html><head/><body><p><span style=" font-size:14pt;">Привет абитуриент! Мы рады, что</span></p><p><span style=" font-size:14pt;">ты выбрал именно наш университет!</span></p><p><span style=" font-size:14pt;">Давай я покажу и расскажу, чем мы</span></p><p><span style=" font-size:14pt;">тут занимаемся! </span><span style=" font-size:10pt;">)</span><span style=" font-size:12pt;">)</span><span style=" font-size:14pt;">)</span></p></body></html>')
