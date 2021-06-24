import sys, os, json
import datetime as dt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication

class Const():
    def __init__(c):
        c.load()

    def find(c,ctype,cname):
        a = c.fjson[ctype]
        for i in a:
            name = i['name']
            if name==cname:
                return i

    def load(c,path = 'consts.json',loaded = False):
        c.spath = 'design/'+path
        if os.path.exists('design/'+path):
            f = open('design/'+path,'r')
            ft = f.read()
            c.fjson = json.loads(ft)
            f.close()
        else:
            raise FileNotFoundError
            QCoreApplication.instance().quit
        if (c.fjson['selected']!='default') and \
           (os.path.exists('design/'+c.fjson['selected'])) and \
           (c.fjson['name']=='default') and (not loaded):
            c.load(path = c.fjson['selected'])
        c.upd()

    def sel_sav(c,p):
        fc = open('design/consts.json','r')
        fc_t = json.loads(fc.read())
        sp = p
        if sp=='consts.json':
            sp = 'default'
        fc_t['selected']=sp
        fc.close()
        fc = open('design/consts.json','w')
        fc_w = json.dumps(fc_t,sort_keys=True,indent=4)
        fc.write(fc_w)
        fc.close()

    def ret_cur(c):
        fc = open('design/consts.json','r')
        fc_t = json.loads(fc.read())
        sel = fc_t['selected']
        #if sel=='default':
        #    sel = 'default'
        fc.close()
        return sel

    def save(c,path = 'consts.json'):
        f = open('design/'+path,'w')
        st = json.dumps(c.fjson,sort_keys=True,indent=4)
        f.write(st)
        f.close()

    def upd(c):
        
            
        c.RFrame = c.find('frame','RightPanel')
        c.CFrame = c.find('frame','CenterPanel')
        c.CurWek = c.find('label','CurWeek')
        c.BT_edit = c.find('button','Edit')
        c.Wsize = c.find('frame','Window')
        c.CurDay = c.find('label','CurDay')
        c.BT_rm1 = c.find('button','mod1')
        c.LB_wek = c.find('label','m0_week')
        c.BT_pm0 = c.find('button','m0_pos')
        c.CB_m0 = c.find('combobox','m0_box')
        c.LB_wd = c.find('label','m0_day')
        c.LB_dp = c.find('label','m0_num')
        c.LB_pr = c.find('label','m0_para')
        c.LB_et = c.find('label','m1_et')
        c.LE_et = c.find('LineEdit','m1_et')
        c.CB_m1 = c.find('combobox','m1_box')
        c.CB_de = c.find('combobox','de_box')
        c.BT_de = c.find('button','de_button')
        c.LB_de = c.find('label','de_label')
        c.LE_de = c.find('LineEdit','de_edit')
        pass

class Example(QMainWindow):
    def __init__(s):
        super().__init__()
        #app = QApplication(sys.argv)
        #exp = Example()
        #app.exec_()
        s.initUI()

    def loadjson(s):
        if os.path.exists('rasp.json'):
            f = open('rasp.json','r')
            ft = f.read()
            s.fjson = json.loads(ft)
            f.close()
        
        
    def findweek(s,st):
        ss = int(str(st).split(' ')[0])
        return ss//7+1

    def switch_mod(s):
        if s.cmod==1:
            for i in s.mod1:
                #print(i)
                i.hide()
            for i in s.mod0:
                i.show()
            s.testWidget.hide()
            s.cmod=0
        elif s.cmod==0:
            for i in s.mod1:
                i.show()
            for i in s.mod0:
                i.hide()
            s.testWidget.show()
            s.cmod=1

    def style_set(s,st,ob):
        hold,hover,pressed,bgclr,selclr,presclr,fgclr,font,fsize,falign,\
             fghoclr,fgprclr= \
                                         ob['bgimg'],ob['hoimg'],ob['primg'],\
                                         ob['bgclr'],ob['selclr'],ob['presclr'],\
                                         ob['fgclr'],ob['font'][0],\
                                         ob['font'][1],ob['font'][2],\
                                         ob['fghoclr'],ob['fgprclr']
                                         
        styl = ''
        if hold!='':
            styl += st+'{border-image:url('+hold+');}\n'
        if hover!='':
            styl += st+'::hover{border-image:url('+hover+');}\n'
        if pressed!='':
            styl += st+'::pressed{border-image:url('+pressed+');}\n'
        if bgclr!='':
            styl += st+'{background-color:'+bgclr+';}\n'
        if selclr!='':
            styl += st+':hover{background-color:'+selclr+';}\n'
        if presclr!='':
            styl += st+':pressed{background-color:'+presclr+';}\n'
        if fgclr!='':
            styl += st+'{color:'+fgclr+';}\n'
        if fghoclr!='':
            styl += st+':hover{color:'+fghoclr+';}\n'
        if fgprclr!='':
            styl += st+':pressed{color:'+fgprclr+';}\n'
        if font!='':
            styl += st+'{font:'+font+';}\n'
        if fsize!='':
            styl += st+'{font-size:'+str(fsize)+'pt;}\n'
        if falign!='':
            styl += st+'{qproperty-alignment:'+falign+';}\n'
        if st=='QComboBox':
            ddimg,ddclr = ob['other'][0],ob['other'][1]
            if ddimg!='':
                styl += st+'::drop-down{image:url('+ddimg+');}\n'
            if ddclr!='':
                styl += st+'::drop-down{background-color:'+ddclr+';}\n'
        return styl

    def b_edit(s):
        s.switch_mod()

    def b_add(s):
        a = s.fjson['data']
        s.curid = a.index(a[-1])
        s.fjson['data'].append({"id":int(s.curid)+1,"name":'',"week":'',\
                                       "teacher":'',"cab":'',"day":'',\
                                       "number":''})
        s.CB_m1.addItem(str(a[-1]['id'])+': ')
        s.CB_m1.setCurrentIndex(s.curid+1)
        
        a = s.fjson['data']
        s.curid = a.index(a[-1])
        j = 0
        for i in s.LE_et:
            i.setText(str(a[-1][s.JJ[j]]))
            j += 1
                      
    def b_del(s):
        a = s.fjson['data']
        l = len(a)-1
        if l!=0:
            s.fjson['data'].pop(s.curid)
            if s.curid==l:
                s.CB_m1.removeItem(s.curid)
                #s.curid -= 1
                s.CB_m1.setCurrentIndex(s.curid)
            else:
                s.CB_m1.removeItem(s.curid)
            s.listclick(s.curid)
        pass

    def b_save(s):
        st = json.dumps(s.fjson,sort_keys=True,indent=4)
        file = open('rasp.json','w')
        file.write(st)
        file.close()

    def b_prevW(s):
        if s.curwk>1:
            s.curwk -= 1
            s.CB_m0.setCurrentIndex(s.curwk-1)
            s.upd(-1)

    def b_nextW(s):
        if s.curwk<18:
            s.curwk += 1
            s.CB_m0.setCurrentIndex(s.curwk-1)
            s.upd(-1)

    def findp(s,week,day,num):
        a = s.fjson['data']
        ret = '-'
        for i in a:
            weks = map(int,i['week'].split(','))
            if (week in weks) and (day == int(i['day'])) and \
               (num == int(i['number'])):
                ret = i['name']+'\n'+i['teacher']+'\n'+i['cab']
        return ret

    def upd(s,k):
        if k!=-1:
            s.curwk = k+1
        s.LB_wek.setText(s.c.LB_wek['other'][1]+str(s.curwk))
        for i in range(30):
            s.LB_pr[i].setText(s.findp(s.curwk,i//5+1,i%5+1))
        for i in range(6):
            td = dt.timedelta(days=(s.curwk-1)*7+i)
            t = s.fd+td
            s.LB_wd[i].setText(s.c.LB_wd['other'][i+1]+t.strftime(' (%d.%m)'))

    def listclick(s,idd):
        s.curid = idd
        for i in range(len(s.fjson['data'])):
            s.fjson['data'][i]['id'] = i
        a = s.fjson['data'][s.curid]
        j = 0
        for i in s.LE_et:
            i.setText(str(a[s.JJ[j]]))
            j += 1
        s.keychange()
        pass

    def keychange(s):
        a = s.fjson['data']
        j = 0
        for i in s.LE_et:
            a[s.curid][s.JJ[j]] = i.text()
            j += 1
        s.fjson['data'][s.curid] = a[s.curid]
        for i in range(len(a)):
            s.CB_m1.setItemText(i,str(i)+': '+a[i]['name'])

    def design_type(s,ind):
        st = s.CB_Et.currentText()
        s.cur_type = st
        list_names = [i['name'] for i in s.c.fjson[st]]
        s.checked = False
        s.CB_En.clear()
        s.CB_Ei.clear()
        s.LE_Ev.clear()
        s.CB_Eo.clear()
        s.CB_Eo.addItems(list_names)
        s.checked = True
        s.CB_Eo.setCurrentIndex(0)
        s.design_object(0)

    def design_object(s,ind):
        if s.checked:
            st = s.CB_Eo.currentText()
            s.cur_ind = ind
            s.cur_obj = st
            s.checked = False
            s.CB_En.clear()
            s.CB_Ei.clear()
            s.LE_Ev.clear()
            for i in s.c.fjson[s.cur_type]:
                if i['name']==st:
                    list_vars = [k for k,_ in i.items()]
            s.CB_En.addItems(list_vars)
            s.checked = True
            s.CB_En.setCurrentIndex(0)
            s.design_name(0)

    def design_name(s,ind):
        if s.checked:
            st = s.CB_En.currentText()
            s.cur_var = st
            s.checked = False
            s.CB_Ei.clear()
            s.LE_Ev.clear()
            a = s.c.fjson[s.cur_type][s.cur_ind][s.cur_var]
            list_data = []
            if str(type(a))=="<class 'list'>":
                s.cur_vartype = 'list'
                list_data += a
            elif str(type(a))=="<class 'int'>":
                s.cur_vartype = 'int'
                list_data += [int(a)]
            else:
                s.cur_vartype = 'str'
                list_data += [str(a)]
            for i in range(len(list_data)):
                if str(type(list_data[i]))=="<class 'int'>":
                    list_data[i]='int:'+str(list_data[i])
                elif str(type(list_data[i]))=="<class 'str'>":
                    list_data[i]='str:'+list_data[i]
            #print(list_data)
            #print('type: '+s.cur_vartype)
            s.CB_Ei.addItems(list_data)
            s.checked = True
            s.CB_Ei.setCurrentIndex(0)
            s.design_i(0)
            
            
    def design_i(s,ind):
        if s.checked:
            st1 = s.CB_Ei.currentText()
            s.cur_value = st1
            s.cur_val = st1[4:]
            #print('i '+s.cur_val)
            s.checked = False
            s.LE_Ev.clear()
            s.LE_Ev.setText(s.cur_val)
            s.checked = True
            s.cur_indedit = ind
            s.design_value('')
            

    def design_value(s,_):
        if s.checked:
            ind = s.cur_indedit
            st2 = s.LE_Ev.text()
            #print(st2)
            s.checked = False
            s.CB_Ei.setItemText(ind,s.cur_value[:4]+st2)
            #print(ind)
            b = []
            if s.CB_Ei.count()>1:
                #print('список')
                b += [s.CB_Ei.itemText(i) for i in range(s.CB_Ei.count())]
                for i in range(len(b)):
                    if b[i][:4]=='int:':
                        b[i] = int(b[i][4:])
                    elif b[i][:4]=='str:':
                        b[i] = b[i][4:]
            elif s.CB_Ei.count()==1:
                #print('один элемент')
                if len(s.CB_Ei.itemText(0))==4:
                    b = ''
                elif len(s.CB_Ei.itemText(0))>4:
                    b = s.CB_Ei.itemText(0)[4:]
                #print('значение b '+b)
            s.checked = True
            #print('конец цикла')
            s.c.fjson[s.cur_type][s.cur_ind][s.cur_var] = b
            
            '''try:
                print('Удалить тест')
                s.testWidget.setParent(None)
            except:
                print('уже удален')
                pass
            if s.cur_type=='button':
                s.testWidget = QPushButton(s)
                tt = 'QPushButton'
            elif s.cur_type=='LineEdit':
                s.testWidget = QLineEdit(s)
                tt = 'QLineEdit'
            elif s.cur_type=='combobox':
                s.testWidget = QComboBox(s)
                tt = 'QComboBox'
            elif s.cur_type=='label':
                s.testWidget = QLabel(s)
                tt = 'QLabel'
            elif s.cur_type=='frame':
                s.testWidget = QLabel(s)
                tt = 'QLabel'
            if s.testWidget!=None:
                s.test_des = s.c.fjson[s.cur_type][s.cur_ind]
                s.testWidget.resize(s.test_des['size'][0],\
                                    s.test_des['size'][1])
                s.testWidget.move(s.x_test,s.y_test)
                s.testWidget.setStyleSheet(s.style_set(tt,s.test_des))
                s.testWidget.setText('test')
                
                if s.cmod==0:
                    s.testWidget.hide()
                else:
                    s.testWidget.show()''' #test widget
    def bd_applytest(s):
        try:
            #print('Удалить тест')
            s.testWidget.setParent(None)
        except:
            #print('уже удален')
            pass
        if s.cur_type=='button':
            s.testWidget = QPushButton(s)
            tt = 'QPushButton'
        elif s.cur_type=='LineEdit':
            s.testWidget = QLineEdit(s)
            tt = 'QLineEdit'
        elif s.cur_type=='combobox':
            s.testWidget = QComboBox(s)
            tt = 'QComboBox'
        elif s.cur_type=='label':
            s.testWidget = QLabel(s)
            tt = 'QLabel'
        elif s.cur_type=='frame':
            s.testWidget = QLabel(s)
            tt = 'QLabel'
        if s.testWidget!=None:
            s.test_des = s.c.fjson[s.cur_type][s.cur_ind]
            s.testWidget.resize(s.test_des['size'][0],\
                                s.test_des['size'][1])
            s.testWidget.move(s.x_test,s.y_test)
            s.testWidget.setStyleSheet(s.style_set(tt,s.test_des))
            if tt == 'QComboBox':
                s.testWidget.addItem('test')
            else:
                s.testWidget.setText('test')
                
            if s.cmod==0:
                s.testWidget.hide()
            else:
                s.testWidget.show()
                
    def bd_save(s):
        file = open(s.c.spath,'w')
        ft = json.dumps(s.c.fjson,sort_keys=True,indent=4)
        file.write(ft)
        file.close()
        pass

    def bd_saveas(s):
        filename = QFileDialog.getSaveFileName(s,'Сохранить как..','design/')
        if filename[0][-5:]=='.json':
            file = open(filename[0],'w')
            s.c.spath = filename[0]
        else:
            file = open(filename[0]+'.json','w')
            s.c.spath = filename[0]+'.json'
        s.c.fjson['name']=filename[0].split('/')[-1]
        #print(filename[0].split('/')[-1])
        ft = json.dumps(s.c.fjson,sort_keys=True,indent=4)
        file.write(ft)
        file.close()
        pass

    def delall(s):
        for i in s.mod0:
            i.setParent(None)
        for i in s.mod1:
            i.setParent(None)
        for i in s.modC:
            i.setParent(None)
        s.exitAct.setParent(None)
        s.menuBar().clear()
        s.menuBar().setParent(None)
        s.Menu.setParent(None)
    
    def bd_apply(s):
        s.delall()
        s.c.upd()
        s.MainInit()
        s.GUIMenuInit()

    def cb_load(s,ind):
        #if s.c.fjson['name']=='default':
            #s.c.fjson['selected']=s.CB_lo.currentText()
        s.c.sel_sav(s.CB_lo.currentText())
        s.c.load(s.CB_lo.currentText(),loaded=True)
        #if s.c.fjson['name']=='default':
        #    s.c.fjson['selected']='default'
        #    s.c.save()
        s.c.spath = 'design/'+s.CB_lo.currentText()
        s.design_type(0)
        pass
    
    def GUIMenuInit(s):
        s.exitAct = QAction('&Exit',s)
        s.exitAct.setShortcut('Ctrl+Q')
        s.exitAct.setStatusTip('Exit application')
        s.exitAct.triggered.connect(qApp.quit)
        s.statusBar()
        s.menuBar().clear()
        s.Menu = s.menuBar()
        s.FileMenu = s.Menu.addMenu('&File')
        s.FileMenu.addAction(s.exitAct)

    def MainInit(s):
        #s.destroy()
        s.cmod = 1
        list_m = [str(s.data[i]['id'])+': '+s.data[i]['name'] \
                  for i in range(len(s.data))]
        s.mod0 = []
        s.mod1 = []
        s.modC = []
        s.rightFrame = QLabel(s)
        s.rightFrame.setFrameStyle(QFrame.StyledPanel)
        s.rightFrame.setLineWidth(2)
        s.rightFrame.resize(s.c.RFrame['size'][0],s.c.Wsize['size'][1])
        s.rightFrame.move(s.c.Wsize['size'][0]-s.c.RFrame['size'][0],0)
        s.rightFrame.setStyleSheet(s.style_set('QLabel',s.c.RFrame))
        
        s.centerFrame = QLabel(s)
        s.centerFrame.setFrameStyle(QFrame.StyledPanel)
        s.centerFrame.setLineWidth(2)
        s.centerFrame.resize(s.c.Wsize['size'][0]-s.c.RFrame['size'][0],\
                             s.c.Wsize['size'][1])
        s.centerFrame.move(0,0)
        s.centerFrame.setStyleSheet(s.style_set('QLabel',s.c.CFrame))
        #rightpanel static
        xc_pan = s.c.Wsize['size'][0]-s.c.RFrame['size'][0]//2
        s.LB_currweek = QLabel(s)
        s.LB_currweek.resize(s.c.CurWek['size'][0],s.c.CurWek['size'][1])
        s.LB_currweek.move(xc_pan-s.c.CurWek['size'][0]//2,\
                           s.c.CurWek['other'][0]//2)
        s.LB_currweek.setStyleSheet(s.style_set('QLabel',s.c.CurWek))
        s.LB_currweek.setFont(QFont(s.c.CurWek['font'][0],pointSize=\
                                    s.c.CurWek['font'][1]))
        s.LB_currweek.setText(s.c.CurWek['other'][1]+str(s.wk))
        
        y_d = s.c.CurWek['other'][0]//2+s.c.CurWek['size'][1]+\
              s.c.CurDay['other'][0]
        s.LB_curday = QLabel(s)
        s.LB_curday.resize(s.c.CurDay['size'][0],s.c.CurDay['size'][1])
        s.LB_curday.move(xc_pan-s.c.CurDay['size'][0]//2,y_d  )
        s.LB_curday.setStyleSheet(s.style_set('QLabel',s.c.CurDay))
        s.LB_curday.setText(s.c.CurDay['other'][1]+'\n'+\
                            s.c.CurDay['other'][s.nd.isoweekday()+1]+\
                            s.nd.strftime(' (%d.%m)'))
        s.modC += [s.rightFrame,s.centerFrame,s.LB_currweek,s.LB_curday]
        #rightpanel mod0
        y_d += s.c.CurDay['size'][1]+s.c.BT_edit['other'][0]
        s.BT_edit = QPushButton(s)
        s.BT_edit.clicked.connect(s.b_edit)
        s.BT_edit.resize(s.c.BT_edit['size'][0],s.c.BT_edit['size'][1])
        s.BT_edit.move(xc_pan-s.c.BT_edit['size'][0]//2,y_d)
        s.BT_edit.setStyleSheet(s.style_set('QPushButton',s.c.BT_edit))
        s.BT_edit.setText(s.c.BT_edit['other'][1])
        
        #rightpanel mod1
        s.BT_mod1 = []
        for i in range(4):
            s.BT_mod1.append(QPushButton(s))
            s.mod1.append(s.BT_mod1[i])
            s.BT_mod1[i].resize(s.c.BT_rm1['size'][0],s.c.BT_rm1['size'][1])
            s.BT_mod1[i].move(xc_pan-s.c.BT_rm1['size'][0]//2,y_d)
            y_d += s.c.BT_rm1['size'][1]+s.c.BT_rm1['other'][0]
            s.BT_mod1[i].setStyleSheet(s.style_set('QPushButton',s.c.BT_rm1))
            s.BT_mod1[i].setText(s.c.BT_rm1['other'][i+1])
        s.BT_mod1[0].clicked.connect(s.b_edit)
        s.BT_mod1[1].clicked.connect(s.b_add)
        s.BT_mod1[2].clicked.connect(s.b_del)
        s.BT_mod1[3].clicked.connect(s.b_save)
        #centerpanel mod0
        x_m0 = (s.c.Wsize['size'][0]-s.c.RFrame['size'][0])//2
        y_m0 = s.c.LB_wek['other'][0]-s.c.LB_wek['size'][1]//2
        s.LB_wek = QLabel(s)
        s.LB_wek.resize(s.c.LB_wek['size'][0],s.c.LB_wek['size'][1])
        s.LB_wek.move(x_m0-s.c.LB_wek['size'][0]//2,y_m0)
        s.LB_wek.setStyleSheet(s.style_set('QLabel',s.c.LB_wek))
        s.LB_wek.setText(s.c.LB_wek['other'][1]+str(s.curwk))
        x_m1 = x_m0-s.c.LB_wek['size'][0]//2-s.c.BT_pm0['size'][0]-\
               s.c.BT_pm0['other'][0]
        x_m2 = x_m0+s.c.LB_wek['size'][0]//2+s.c.BT_pm0['other'][0]
        s.BT_prevW = QPushButton(s)
        s.BT_prevW.resize(s.c.BT_pm0['size'][0],s.c.BT_pm0['size'][1])
        s.BT_prevW.move(x_m1,y_m0)
        s.BT_prevW.setStyleSheet(s.style_set('QPushButton',s.c.BT_pm0))
        s.BT_prevW.setText('<<')
        s.BT_prevW.clicked.connect(s.b_prevW)
        s.BT_nextW = QPushButton(s)
        s.BT_nextW.resize(s.c.BT_pm0['size'][0],s.c.BT_pm0['size'][1])
        s.BT_nextW.move(x_m2,y_m0)
        s.BT_nextW.setStyleSheet(s.style_set('QPushButton',s.c.BT_pm0))
        s.BT_nextW.setText('>>')
        s.BT_nextW.clicked.connect(s.b_nextW)
        y_m3 = y_m0+s.c.LB_wek['size'][1]+s.c.LB_wek['other'][2]
        s.CB_m0 = QComboBox(s)
        s.CB_m0.resize(s.c.CB_m0['size'][0],s.c.CB_m0['size'][1])
        s.CB_m0.move(x_m0-s.c.CB_m0['size'][0]//2,y_m3)
        s.CB_m0.setStyleSheet(s.style_set('QComboBox',s.c.CB_m0))
        for i in range(18):
            s.CB_m0.addItem(str(i+1))
        s.CB_m0.setCurrentIndex(s.curwk-1)
        s.CB_m0.currentIndexChanged.connect(s.upd)
        
        s.LB_wd = []
        x_m4 = x_m0-s.c.LB_wd['size'][0]-s.c.LB_wd['size'][0]//2
        y_m4 = y_m3+s.c.LB_wek['other'][3]+s.c.CB_m0['size'][1]
        for i in range(6):
            s.LB_wd.append(QLabel(s))
            s.mod0.append(s.LB_wd[i])
            s.LB_wd[i].resize(s.c.LB_wd['size'][0],s.c.LB_wd['size'][1])
            s.LB_wd[i].move(x_m4+(i%3)*s.c.LB_wd['size'][0],\
                            y_m4+(i//3)*s.c.LB_wd['other'][0])
            s.LB_wd[i].setStyleSheet(s.style_set('QLabel',s.c.LB_wd))
            s.LB_wd[i].setText(s.c.LB_wd['other'][i+1])
        y_s = (s.c.LB_wd['other'][0]-s.c.LB_wd['size'][1])//5
        s.LB_dp = []
        for i in range(30):
            s.LB_dp.append(QLabel(s))
            s.mod0.append(s.LB_dp[i])
            s.LB_dp[i].resize(s.c.LB_dp['size'][0],y_s)
            s.LB_dp[i].move(x_m4+(i//5)*s.c.LB_wd['size'][0]-\
                         3*(i//15)*s.c.LB_wd['size'][0],\
                         y_m4+(i%5)*y_s+s.c.LB_wd['size'][1]+\
                         (i//15)*s.c.LB_wd['other'][0])
            s.LB_dp[i].setStyleSheet(s.style_set('QLabel',s.c.LB_dp))
            s.LB_dp[i].setText(s.c.LB_dp['other'][i%5+1])
        s.LB_pr = []
        x_s = s.c.LB_wd['size'][0]-s.c.LB_dp['size'][0]
        x_m5 = x_m4+s.c.LB_dp['size'][0]
        for i in range(30):
            s.LB_pr.append(QLabel(s))
            s.mod0.append(s.LB_pr[i])
            s.LB_pr[i].resize(x_s,y_s)
            s.LB_pr[i].move(x_m5+(i//5)*s.c.LB_wd['size'][0]-\
                         3*(i//15)*s.c.LB_wd['size'][0],\
                         y_m4+(i%5)*y_s+s.c.LB_wd['size'][1]+\
                         (i//15)*s.c.LB_wd['other'][0])
            s.LB_pr[i].setStyleSheet(s.style_set('QLabel',s.c.LB_pr))
        s.mod0 += [s.BT_edit,s.LB_wek,s.BT_prevW,s.BT_nextW,s.CB_m0]
        #s.upd()
        #centerpanel mod1
        s.LB_et = []
        x_m0 = s.c.LB_et['other'][0]
        y_m0 = s.c.LB_et['other'][1]
        for i in range(7):
            s.LB_et.append(QLabel(s))
            s.mod1.append(s.LB_et[i])
            s.LB_et[i].resize(s.c.LB_et['size'][0],s.c.LB_et['size'][1])
            s.LB_et[i].move(x_m0,y_m0+i*s.c.LB_et['size'][1])
            s.LB_et[i].setStyleSheet(s.style_set('QLabel',s.c.LB_et))
            s.LB_et[i].setText(s.c.LB_et['other'][i+2])
        s.LE_et = []
        x_m0 = x_m0+s.c.LB_et['size'][0]
        for i in range(7):
            s.LE_et.append(QLineEdit(s))
            s.mod1.append(s.LE_et[i])
            s.LE_et[i].resize(s.c.LE_et['size'][0],s.c.LE_et['size'][1])
            s.LE_et[i].move(x_m0,y_m0+i*s.c.LE_et['size'][1])
            s.LE_et[i].setStyleSheet(s.style_set('QLineEdit',s.c.LE_et))
            s.LE_et[i].textEdited.connect(s.keychange)
        x_m0 = x_m0+s.c.LE_et['other'][0]+s.c.LE_et['size'][0]
        s.CB_m1 = QComboBox(s)
        s.CB_m1.resize(s.c.CB_m1['size'][0],s.c.CB_m1['size'][1])
        s.CB_m1.move(x_m0,y_m0)
        s.CB_m1.setStyleSheet(s.style_set('QComboBox',s.c.CB_m1))
        for i in list_m:
            s.CB_m1.addItem(i)
        s.CB_m1.setCurrentIndex(0)
        s.CB_m1.currentIndexChanged.connect(s.listclick)
        s.listclick(0)

        y_m1 = y_m0+7*s.c.LB_et['size'][1]+s.c.CB_de['other'][3]
        y_m2 = s.c.LB_de['size'][1]+s.c.LB_de['other'][0]
        list_t = ['button','combobox','label','LineEdit','frame']
        
        s.LB_Et = QLabel(s)
        s.LB_Et.resize(s.c.LB_de['size'][0],s.c.LB_de['size'][1])
        s.LB_Et.move(s.c.LB_de['other'][0],y_m1)
        s.LB_Et.setStyleSheet(s.style_set('QLabel',s.c.LB_de))
        s.LB_Et.setText(s.c.LB_de['other'][1])

        s.LB_Eo = QLabel(s)
        s.LB_Eo.resize(s.c.LB_de['size'][0],s.c.LB_de['size'][1])
        s.LB_Eo.move(s.c.LB_de['other'][0],y_m1+y_m2)
        s.LB_Eo.setStyleSheet(s.style_set('QLabel',s.c.LB_de))
        s.LB_Eo.setText(s.c.LB_de['other'][2])

        s.LB_En = QLabel(s)
        s.LB_En.resize(s.c.LB_de['size'][0],s.c.LB_de['size'][1])
        s.LB_En.move(s.c.LB_de['other'][0],y_m1+2*y_m2)
        s.LB_En.setStyleSheet(s.style_set('QLabel',s.c.LB_de))
        s.LB_En.setText(s.c.LB_de['other'][3])

        s.LB_Ei = QLabel(s)
        s.LB_Ei.resize(s.c.LB_de['size'][0],s.c.LB_de['size'][1])
        s.LB_Ei.move(s.c.LB_de['other'][0],y_m1+3*y_m2)
        s.LB_Ei.setStyleSheet(s.style_set('QLabel',s.c.LB_de))
        s.LB_Ei.setText(s.c.LB_de['other'][4])

        s.LB_Ev = QLabel(s)
        s.LB_Ev.resize(s.c.LB_de['size'][0],s.c.LB_de['size'][1])
        s.LB_Ev.move(s.c.LB_de['other'][0],y_m1+4*y_m2)
        s.LB_Ev.setStyleSheet(s.style_set('QLabel',s.c.LB_de))
        s.LB_Ev.setText(s.c.LB_de['other'][5])
            
        x_m1 = s.c.LB_de['other'][0]+s.c.CB_de['other'][2]+\
                     s.c.LB_de['size'][0]
        s.CB_Et = QComboBox(s)
        s.CB_Et.resize(s.c.CB_de['size'][0],s.c.CB_de['size'][1])
        s.CB_Et.move(x_m1,y_m1)
        s.CB_Et.setStyleSheet(s.style_set('QComboBox',s.c.CB_de))
        s.CB_Et.addItems(list_t)
        s.CB_Et.setCurrentIndex(0)

        s.CB_Eo = QComboBox(s)
        s.CB_Eo.resize(s.c.CB_de['size'][0],s.c.CB_de['size'][1])
        s.CB_Eo.move(x_m1,y_m1+y_m2)
        s.CB_Eo.setStyleSheet(s.style_set('QComboBox',s.c.CB_de))
        
                       
        s.CB_En = QComboBox(s)
        s.CB_En.resize(s.c.CB_de['size'][0],s.c.CB_de['size'][1])
        s.CB_En.move(x_m1,y_m1+2*y_m2)
        s.CB_En.setStyleSheet(s.style_set('QComboBox',s.c.CB_de))

        s.CB_Ei = QComboBox(s)
        s.CB_Ei.resize(s.c.CB_de['size'][0],s.c.CB_de['size'][1])
        s.CB_Ei.move(x_m1,y_m1+3*y_m2)
        s.CB_Ei.setStyleSheet(s.style_set('QComboBox',s.c.CB_de))
    
        s.x_test = x_m1
        s.y_test = y_m1+4*y_m2+s.c.LE_de['size'][1]+20
        
        s.LE_Ev = QLineEdit(s)
        s.LE_Ev.resize(s.c.LE_de['size'][0],s.c.LE_de['size'][1])
        s.LE_Ev.move(x_m1,y_m1+4*y_m2)
        s.LE_Ev.setStyleSheet(s.style_set('QLineEdit',s.c.LE_de))

        s.design_type(0)
        s.design_object(0)
        s.CB_Et.currentIndexChanged.connect(s.design_type)
        s.CB_Eo.currentIndexChanged.connect(s.design_object)
        s.CB_En.currentIndexChanged.connect(s.design_name)
        s.CB_Ei.currentIndexChanged.connect(s.design_i)
        s.LE_Ev.textEdited.connect(s.design_value)
        
        x_m2 = x_m1+s.c.CB_de['size'][0]+s.c.BT_de['other'][0]
        s.BT_sv = QPushButton(s)
        s.BT_sv.resize(s.c.BT_de['size'][0],s.c.BT_de['size'][1])
        s.BT_sv.move(x_m2,y_m1)
        s.BT_sv.setStyleSheet(s.style_set('QPushButton',s.c.BT_de))
        s.BT_sv.setText(s.c.BT_de['other'][2])

        s.BT_sa = QPushButton(s)
        s.BT_sa.resize(s.c.BT_de['size'][0],s.c.BT_de['size'][1])
        s.BT_sa.move(x_m2,y_m1+y_m2)
        s.BT_sa.setStyleSheet(s.style_set('QPushButton',s.c.BT_de))
        s.BT_sa.setText(s.c.BT_de['other'][3])

        s.BT_co = QPushButton(s)
        s.BT_co.resize(s.c.BT_de['size'][0],s.c.BT_de['size'][1])
        s.BT_co.move(x_m2,y_m1+2*y_m2)
        s.BT_co.setStyleSheet(s.style_set('QPushButton',s.c.BT_de))
        s.BT_co.setText(s.c.BT_de['other'][4])

        s.BT_ap = QPushButton(s)
        s.BT_ap.resize(s.c.BT_de['size'][0],s.c.BT_de['size'][1])
        s.BT_ap.move(x_m2,y_m1+4*y_m2)
        s.BT_ap.setStyleSheet(s.style_set('QPushButton',s.c.BT_de))
        s.BT_ap.setText(s.c.BT_de['other'][5])

        s.CB_lo = QComboBox(s)
        s.CB_lo.resize(s.c.CB_de['size'][0],s.c.CB_de['size'][1])
        s.CB_lo.move(x_m2+s.c.BT_de['size'][0]+s.c.CB_de['other'][2],\
                     y_m1)
        s.CB_lo.setStyleSheet(s.style_set('QComboBox',s.c.CB_de))
        files = os.listdir('design/')
        jsons = list(filter(lambda x: x.endswith('.json'),files))
        s.CB_lo.addItems(jsons)
        if s.c.ret_cur()!='default':
            idd = jsons.index(s.c.ret_cur())
        else:
            idd = jsons.index('consts.json')
        s.CB_lo.currentIndexChanged.connect(s.cb_load)
        s.CB_lo.setCurrentIndex(idd)
        
        s.BT_sv.clicked.connect(s.bd_save)
        s.BT_sa.clicked.connect(s.bd_saveas)
        s.BT_co.clicked.connect(s.bd_apply)
        s.BT_ap.clicked.connect(s.bd_applytest)
        s.bd_applytest()
        #s.LB_
        s.mod1 += [s.CB_m1,s.CB_Et,s.LB_Et,s.LB_En,s.LB_Ei,s.LB_Ev,s.CB_En,\
                   s.CB_Ei,s.LE_Ev,s.BT_sv,s.BT_sa,s.CB_Eo,s.LB_Eo,s.BT_co,\
                   s.BT_ap,s.CB_lo]
        s.setGeometry(100,100,s.c.Wsize['size'][0],s.c.Wsize['size'][1])
        s.setFixedSize(s.size())
        s.setWindowTitle('Application')
        #s.hide()
        for i in s.modC:
            i.show()
        s.show()
        s.switch_mod()
        s.upd(-1)           
        pass

    def initUI(s):
        s.JJ = ('id','name','week','teacher','cab','day','number')
        s.fd = dt.date(2017,2,6)
        s.nd = dt.date.today()
        s.c = Const()
        s.wk = s.findweek(s.nd-s.fd)
        s.curwk = s.wk
        
        s.loadjson()
        s.data = s.fjson['data']
        
        s.MainInit()
        s.GUIMenuInit()
        
def start():
    app = QApplication(sys.argv)
    exp = Example()
    app.exec_()
    
