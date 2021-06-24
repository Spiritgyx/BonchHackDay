import os, json
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication, Qt
from navgui import Ui_MainWindow

'''class canvasVec(QWidget):
    def __init__(self,s):
        QWidget.__init__(self)
        self.initc(s)
        
    def initcords(self,cords):
        self.cords = cords
        self.newvec = True
        self.repaint()
        #self.update()
        
    def paintEvent(self,e):
        super().paintEvent(e)
        if self.newvec:
            qp = QPainter()
            qp.begin(self)
            self.drawVec(qp)
            qp.end()
            ''''''qp.setPen(QPen(QColor('#000000'),5,Qt.SolidLine, Qt.RoundCap))
            qp.setBrush(QBrush(QColor('#000000'),Qt.SolidPattern))
            qp.drawLine(100,100,700,700)
            print('drawed')
            q = QPainter(self)
            q.drawImage(0,0,self.im)''''''
            self.newvec = False
        
    def drawVec(self,qp):
        
        pen = QPen(QColor('#000000'),5,Qt.SolidLine, Qt.RoundCap)
        qp.setPen(pen)
        x1 = self.cords[0]
        y1 = self.cords[1]
        x2 = x1+self.cords[2]
        y2 = y1+self.cords[3]
        print(x1,y1,x2,y2)
        qp.drawLine(x1,y1,x2,y2)
        
    def initc(self,s):
        self.newvec = False
        #self.setParent(s)
        self.setGeometry(40,40,1000,750)
        self.show()'''
        


class Example(Ui_MainWindow):
    def __init__(s,form):
        super().__init__()
        s.setupUi(form)
        s.initUI()
        
    def test(s):
        a = s.data['data'][10]
        print('se')
        s.arrow.setStyleSheet('QLabel{image:url("source/'+a['vec']+'.png");}')
        print('s')
        
        stor = a['vec']
        if (stor=='left') or (stor=='right'):
            s.arrow.resize(40,20)
            xs = 20
            ys = 10
        else:
            s.arrow.resize(20,40)
            xs = 10
            ys = 20
        s.arrow.move(s.x0+a['cords'][0]-xs,s.y0+a['cords'][1]-ys)    
        s.arrow.update()

    def drawArrow(s,a):
        s.map.setStyleSheet('QLabel{image:url("source/'+str(s.cur_corp)+\
                            'k'+str(s.cur_cab//100)+'e.png")}')
        s.arrow.setStyleSheet('QLabel{image:url("source/'+a['vec']+'.png");}')
        stor = a['vec']
        if (stor=='left') or (stor=='right'):
            s.arrow.resize(40,20)
            xs = 20
            ys = 10
        else:
            s.arrow.resize(20,40)
            xs = 10
            ys = 20
        s.arrow.move(s.x0+a['cords'][0]-xs,s.y0+a['cords'][1]-ys)    
        s.arrow.update()
    
    def bt_check_clicked(s):
        a = s.data['data']
        s.cur_corp = int(s.corpus.currentText())
        s.cur_cab = int(s.cabin.value())
        flag = True
        for i in a:
            if (i['corp']==s.cur_corp) and (i['num']==s.cur_cab):
                flag = False
                s.drawArrow(i)
                break
        if flag:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Данный кабинет не найден")
            msg.setInformativeText("")
            msg.setWindowTitle("Внимание")
            msg.setDetailedText("Возможно, вы ошиблись при вводе номера кабинета")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
        

    def initUI(s):
        #s.canvasVEC = QWidget(s.centralwidget)
        #s.canv = canvasVec(s.centralwidget)
        s.button_check.clicked.connect(s.bt_check_clicked)
        s.x0 = s.map.x()
        s.y0 = s.map.y()
        if os.path.exists('nav.json'):
            f = open('nav.json','r')
            ft = f.read()
            s.data = json.loads(ft)
            f.close()
            del(ft)
        print('s')
        #s.test()
        #s.drawing()
        
        
        pass
