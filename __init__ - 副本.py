# -*- coding: utf-8 -*-
import configparser,hashlib,sys,os,json,datetime,qrcode,win32print,win32api
import time
from time import strftime,asctime,ctime,gmtime,mktime
from PyQt5.QtPrintSupport import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt,QTimer,QObject
from lib.tool import *
#子窗体
from Ui_Minaco import Ui_Minaco #主体
from Ui_Dataset import Ui_Dataset #数据库配置
from Ui_Login import Ui_Login #数据库配置
from Ui_MainDant import Ui_MainDant #主要框架
from Ui_OutSideCode import Ui_OutSideCode #外箱条码
from Ui_DantCode import Ui_DantCode #条码生成
from Ui_OutCode import Ui_OutCode #扫描条码
from Ui_OutProt import Ui_OutProt #出货扫描
from Ui_CodeSet1 import Ui_CodeSet1 #出货扫描
from Ui_CodeSet2 import Ui_CodeSet2 #出货扫描

from Ui_Admin import Ui_Admin #后台管理员登录
from Ui_MainDantA import Ui_MainDantA #后台主框架
from Ui_AdminUser import Ui_AdminUser #后台用户列表
from Ui_AddUser import Ui_AddUser #后台管理员登录
from Ui_EditUser import Ui_EditUser #后台管理员登录





#加载配置
class Ui_Minaco(QWidget,Ui_Minaco):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #查看配置文件 如果没有开始执行引导程序
        self.loadtext.setText("正在检验本地配置...")
        self.timer = QTimer(self)
        self.checkconfig()
       
        
    def checkconfig(self):
        cf = configparser.ConfigParser()
        if cf.read('config.ini')==[]:
            self.loadtext.setText("初始化配置...")           
            node = Node()
            node.creat()
            self.timer.timeout.connect(self.DataConfig)
            self.timer.start(1500)
        else:
            self.timer.timeout.connect(self.startlogin)
            self.timer.start(1500)

    def DataConfig(self):       
        self.timer.stop()
        self.hide()
        self.log = Dataset() 
        self.log.show()  
        
    def startlogin(self):
        self.timer.stop()
        self.hide()
        self.log = UserLogin() 
        self.log.show()  
#加载数据库
class Dataset(QWidget, Ui_Dataset):
    def __init__(self):
        super(Dataset, self).__init__()
        self.setupUi(self)
        self.timer = QTimer(self)
        self.timer2 = QTimer(self)
        self.loginbtn.clicked.connect(self.setConfig)
        
    def setConfig(self):
        n = Node()
        n.set('sqlserver','db_host',self.host.text())
        n.set('sqlserver','db_name',self.dataname.text())
        n.set('sqlserver','db_user',self.username.text())
        n.set('sqlserver','db_pass',self.password.text())
        self.timer.timeout.connect(self.checklink)
        self.timer.start(1000)
        
    def checklink(self):
        self.timer.stop()
        ms = MSSQL()
        isok = ms.test()
        if isok == True:
            self.tip.setText("链接成功!!!!")
            self.tip.setStyleSheet("color:#41CD52;")
            self.timer2.timeout.connect(self.closewrap)
            self.timer2.start(1000)
        else:
            self.tip.setText("链接失败!!!!")
            self.tip.setStyleSheet("color:red;")
            
    def closewrap(self):
        self.timer2.stop()
        self.hide()
        self.log = UserLogin() 
        self.log.show() 
        
#加载登录界面  
class UserLogin(QWidget, Ui_Login):
    def __init__(self):
        super(UserLogin, self).__init__()
        self.setupUi(self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.start)
        self.timer.start(1000)
        self.loginbtn.clicked.connect(self.Login)
        self.inadmin.clicked.connect(self.GoAdmin)
        self.limitword()
        #self.intologin()
       
    
    def intologin(self):        
        self.username.setText("dabai")
        self.password.setText("123456")
        self.Login()
        
    def limitword(self):
        #限制账户验证
        reg1 = QRegExp("^[a-zA-Z0-9_-]{4,16}$")
        limitUser = QRegExpValidator(self)
        limitUser.setRegExp(reg1)
        #限制密码验证
        reg2 = QRegExp("^.*(?=.{6,})(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*? ]).*$")
        limitPass = QRegExpValidator(self)
        limitPass.setRegExp(reg2)
        self.username.setValidator(limitUser)
        self.password.setValidator(limitPass)
        
    def start(self):
        self.timer.stop()
        ms = MSSQL()
        isok = ms.test()
        if isok == False:
            self.hide()
            self.log = Dataset() 
            self.log.show()
            
    def Login(self):
        username = self.username.text()
        password = self.password.text()
        password = hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()
        ms = MSSQL()
        relust = ms.get("select root from users where username='"+username+"'and password='"+password+"'")
        if relust==[]:
            self.tip.setText("账户或密码错误！")
            self.tip.setStyleSheet("color:red;")
        else:
            node = Node()          
            node.set("userinfo","username",username)
            node.set("userinfo","root",str(relust[0][0]))
            self.tip.setText("正在登录...")
            self.tip.setStyleSheet("color:#41CD52;")
            self.timer.start(1000)
            self.timer.timeout.connect(self.operation)
            
    def operation(self):
        self.timer.stop()
        self.hide()
        self.log = MainDant() 
        self.log.show()
        
    def GoAdmin(self):
        self.close()
        self.log = LoginAdmin() 
        self.log.show()
        
        
#加载主界面        
class MainDant(QMainWindow, Ui_MainDant, BoxSing):
    def __init__(self,parent=None):
        super(MainDant, self).__init__(parent)
        self.setupUi(self)
        ns = Node()
        self.root = int(ns.get("userinfo","root"))
        #1是只开条码 2是只开出库3是全开对吧        
        if self.root==1:
            self.loadDantCode()
        elif  self.root==2:
            self.loadOutCode()
        elif self.root==3:
            self.loadOutSideCode()#修改
   
    #条码生成
    def loadDantCode(self):
        self.child = DantCode()
        self.child.SonClick.connect(self.recv)#桥接子窗口链接
        self.MaingridLayout.addWidget(self.child)
        self.child.show()
    #扫描条码   
    def loadOutCode(self):
        self.child = OutCode()
        self.child.SonClick.connect(self.recv)#桥接子窗口链接
        self.MaingridLayout.addWidget(self.child)
        self.child.show()
    #出货扫描      
    def loadOutProt(self):
        self.child = OutProt()
        self.child.SonClick.connect(self.recv)#桥接子窗口链接
        self.MaingridLayout.addWidget(self.child)
        self.child.show()
    #外箱条码    
    def loadOutSideCode(self):
        self.child = OutSideCode()
        self.child.SonClick.connect(self.recv)#桥接子窗口链接
        self.MaingridLayout.addWidget(self.child)
        self.child.show()
        
    def recv(self,s):       
    #1是只开条码 2是只开出库3是全开对吧
        print(s)
        tab = int(s)
        if tab==1:
            if self.root != 1:
                self.loadOutSideCode()
            else:
                self.Alert("没有权限！")
        elif tab==2:
            if self.root != 2:
                self.loadDantCode()
            else:
                self.Alert("没有权限！")
                
        elif tab==3:
            if self.root != 1:
                self.loadOutCode()
            else:
                self.Alert("没有权限！")
                
        elif tab==4:
            if self.root != 1:
                self.loadOutProt()
            else:
                self.Alert("没有权限！")


#加载二维码生成界面Ui_DantCode
class DantCode(QWidget, Ui_DantCode, BoxSing):
    SonClick = pyqtSignal(str)  
    def __init__(self,parent=None):
        super(DantCode, self).__init__(parent)
        self.setupUi(self)
        self.file_path=""
        #缓存打印
        self.Dis=''
        self.lstid=''
        self.Lent=0
        node = Node()
        self.username = node.get("userinfo","username")
        self.root = int(node.get("userinfo","root"))
        #type 1为出厂 2为出货
        self.tab1.clicked.connect(self.meau1)
        self.tab2.clicked.connect(self.meau2)
        self.tab3.clicked.connect(self.meau3)
        self.tab4.clicked.connect(self.meau4)
        self.choosurl.clicked.connect(self.choosefile)
        self.codeset.clicked.connect(self.ChengeConfig)
        self.shuaxin.clicked.connect(self.CreatTable)
        self.bulkprint.clicked.connect(self.PrintCode)
        self.bulkdel.clicked.connect(self.DelCode)
        self.creatcode.clicked.connect(self.Printing)        
        self.selectAll.clicked.connect(self.isChoseAll)        
        self.CreatTable()
    def DelCode(self):
        ms = MSSQL()
        self.TabItemClick()
        ftxt=self.Dis
        if ftxt!='':
            sql = "delete from code where id IN ("+self.lstid[0:-1]+") and isuse = 'false'"
            ms.run(sql)
            self.Alert("删除成功！")
            self.CreatTable()
        else:
            self.Alert("您还没有选择条码！")
    def CreatTable(self):
        ms = MSSQL()
        data = ms.get("select id,code,codetitle,datetimes from code where isuse='false' order by id desc")
        if data!=():
            data = list(data)
        else:
            data = []
        self.Lent = len(data)
        self.codelist.setRowCount(len(data))
        self.codelist.setColumnCount(5)#设置列    
        self.codelist.setHorizontalHeaderLabels(['','id','二维码','标识码','创建时间'])
        for i in range(len(data)):
            for n in range(len(data[i])):
               
                datas = str(data[i][n])
                if n==3:
                    if  len(datas)==26:
                        datas=datas[:-3]
                    elif len(datas)==19:
                        datas=datas+'.000'
                    
                newItem = QTableWidgetItem(datas)
                newItem.setTextAlignment(Qt.AlignCenter)
                checkBox = QTableWidgetItem()
                checkBox.setCheckState(Qt.Unchecked)
                self.codelist.setItem(i, 0, checkBox)
                self.codelist.setColumnWidth(0,50)
                if n==0:
                    newItem.setTextAlignment(Qt.AlignCenter)
                    self.codelist.setItem(i,1, newItem)
                    self.codelist.setColumnWidth(1,200)
                
                if n==1:
                    newItem.setTextAlignment(Qt.AlignCenter)
                    self.codelist.setItem(i,2, newItem)
                    self.codelist.setColumnWidth(2,320)
                
                if n==2:
                    newItem.setTextAlignment(Qt.AlignCenter)
                    self.codelist.setItem(i,3, newItem)
                    self.codelist.setColumnWidth(3,280)
                
                if n==3:                  
                    newItem.setTextAlignment(Qt.AlignCenter)
                    self.codelist.setItem(i,4, newItem)
                    self.codelist.setColumnWidth(4,250)

    def choosefile(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Files)
        if dlg.exec_():
            #获取文件所有路径
            file_path= dlg.selectedFiles()
            file_path = file_path[0]
            savestr = file_path.split("/")
            lent = len(savestr)
            #获取文件名
            filename = savestr[lent-1]
            #获取文件路径
            file_path = file_path.replace(filename, "")
            self.GetBtwList(r''+file_path)
    
    def GetBtwList(self,path):
        self.file_path = path
        btwlst = ''
        pathlist = os.listdir(path)
        self.comboBox.clear()
        for filename in pathlist:
            if filename.endswith('btw'):
                self.comboBox.addItem(filename)
 
    def PrintCode(self):
        ms = MSSQL()
        self.TabItemClick()
        ftxt=self.Dis
        if ftxt!='':
            pmode = self.file_path+self.comboBox.currentText()
            if self.comboBox.currentText()!='':
                sql1 = "delete from printcode where username='"+self.username+"' and type=1"
                isdelete = ms.run(sql1)
                #是否已经删除
                if isdelete == True:
                    #是否已经添加
                    isinsert = ms.run(self.Dis)
                    if isinsert == True:                    
                        currentprinter = win32print.GetDefaultPrinter()
                        win32api.ShellExecute(0, "print", pmode, '/d:"%s"' % currentprinter, ".", 0)
                        sql = "update code set isuse='true' where id IN ("+self.lstid[0:-1]+")"
                        ms.run(sql)
                        self.CreatTable()
            else:
                self.Alert("请选择模板")
        else:
            self.Alert("您还没有选择条码！")
            
    def ChengeConfig(self):
        self.child = CodeSet2()
        self.child.show()
    def TabItemClick(self):
        self.Dis='INSERT INTO printcode (code,codetitle1,codetitle2,username,type)VALUES'
        self.lstid=''
        num = 0
        while num < self.Lent:
            item=self.codelist.item(num,0)
            if item.checkState()!=0:
                colum1=self.codelist.item(num,1).text()
                colum2=self.codelist.item(num,2).text()
                colum3 = self.codelist.item(num,3).text()
                colum3 = colum3.split(",")
                self.Dis+="('"+colum2+"','"+colum3[0]+"','"+colum3[1]+"','"+self.username+"',1),"
                self.lstid+=colum1+","
            num=+num+1
        self.Dis=self.Dis[0:-1]
    def isChoseAll(self):
        ischecked = self.selectAll.isChecked()
        if ischecked==True:
            self.TabItemClick()
            self.nSelectAll()
        else:
            self.nSelectNo()
    
    def nSelectAll(self):
        num = 0
        while num < self.Lent:
            item=self.codelist.item(num,0)
            if item.checkState()==0:
                self.codelist.item(num,0).setCheckState(Qt.Checked)      
            #如果值为1就全选    
            num=+num+1
            
    def nSelectNo(self):
        num = 0
        while num < self.Lent:
            item=self.codelist.item(num,0)
            if item.checkState()!=0:
                self.codelist.item(num,0).setCheckState(Qt.Unchecked)
            #如果值为1就全选    
            num=+num+1      
            
    def Printing(self):
        box = QMessageBox(QMessageBox.Question, self.tr("提示"), self.tr("请确认所有参数设置正确后再生成条码，以免生成错误数据和垃圾数据!"), QMessageBox.NoButton, self)
        yr_btn = box.addButton(self.tr("继续生成"), QMessageBox.YesRole)
        box.addButton(self.tr("返回设置"), QMessageBox.NoRole)
        box.exec_()
        if box.clickedButton()!= yr_btn:
            print('返回设置')
            self.ChengeConfig()
            return
        else:
            print('继续生成')
        #获取操作人员
        node = Node()
        ms = MSSQL()
        dirn = ms.get("select * from codeset ")
        dirn = list(dirn)[0]
        sql = "select count(id) from code where compy='"+dirn[1]+"' and product='"+dirn[2]+"' and dat='"+dirn[3]+"' and comboBox='"+dirn[4]+"' and froms='"+dirn[5]+"'"
        sql += "and fromid='"+dirn[6]+"' and dropid='"+dirn[7]+"' and mode='"+dirn[8]+"' and hole='"+dirn[9]+"' and project='"+dirn[10]+"'"
        sql += "and picbate='"+dirn[11]+"' and machine='"+dirn[12]+"' and tiefrom='"+dirn[13]+"'"
        counts = ms.get(sql)
        if counts==():
            counts = 0
        else:
            counts = list(counts)[0][0]
            
        
        #==================================================================SQL初始部分==================================================================   
        
        
        newcode=''
        num = int(self.creatnum.text())
        while num > 0:
        #==================================================================循环开始=====================================================================
            insql =  "INSERT INTO code (compy, product, dat, comboBox, froms, fromid,"
            insql += "dropid, mode, hole, project, picbate, machine, tiefrom, keyint, code, datetimes, creatuser, isuse,codetitle) VALUES "
            newcount = int(counts)+1
            #获取新二维码序列
            newcount = self.ChangeNum(newcount)
            #判断缺几个数就补上几个0
            if len(newcount)==1:
                newcount ='000'+str(newcount)
            elif len(newcount)==2:
                newcount ='00'+str(newcount)
            elif len(newcount)==3:
                newcount ='0'+str(newcount)
                
            newcode = dirn[1]+dirn[2]+dirn[3]+dirn[4]+dirn[5]+dirn[6]+dirn[7]+dirn[8]+dirn[9]+dirn[10]+dirn[11]+dirn[12]+dirn[13]+newcount
            codetitle = dirn[1]+dirn[2]+'-'+dirn[3][1:3]+'-'+dirn[11]+','+dirn[8]+'-'+dirn[9]+'-'+newcount
           
            insql += "('"+dirn[1]+"', '"+dirn[2]+"', '"+dirn[3]+"', '"+dirn[4]+"', '"+dirn[5]+"', '"+dirn[6]+"', '"+dirn[7]+"', '"+dirn[8]+"', '"+dirn[9]+"', '"+dirn[10]+"',"
            insql += "'"+dirn[11]+"', '"+dirn[12]+"', '"+dirn[13]+"', '"+newcount+"', '"+newcode+"',(getdate()), '"+self.username+"', 'false','"+codetitle+"')"
            ms.run(insql) #插入新记录
            counts=counts+1
            num=num-1
            
        #==================================================================循环结束=====================================================================
        # insql = insql[0:-1]
        # ms.run(insql) #插入新记录
        self.CreatTable()
        self.Alert('生成成功！')
 
    def meau1(self):
        #1是只开条码 2是只开出库3是全开对吧  
        self.SonClick.emit("1")
        if self.root!=1:
            self.close()
    def meau2(self):
        self.SonClick.emit("2")
        if self.root!=2:
            self.close()
    def meau3(self):
        self.SonClick.emit("3")
        if self.root!=1:
            self.close()
    def meau4(self):
        self.SonClick.emit("4")
        if self.root!=1:            
            self.close()

#加载扫描条码界面
class OutCode(QWidget, Ui_OutCode, BoxSing):
    SonClick = pyqtSignal(str)
    def __init__(self,parent=None):
        super(OutCode, self).__init__(parent)
        self.setupUi(self)
        node = Node()
        self.username = node.get("userinfo","username")
        self.root = int(node.get("userinfo","root"))
        self.ms = MSSQL()
        self.Lent=0
        self.lstid=''
        self.nowdate = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        
        self.loading()
        self.CreatTable()
        
        self.tab1.clicked.connect(self.meau1)
        self.tab2.clicked.connect(self.meau2)
        self.tab3.clicked.connect(self.meau3)
        self.tab4.clicked.connect(self.meau4)
    def loading(self):
        self.outcode.returnPressed.connect(self.push1)
        self.pack.clicked.connect(self.packed)
        self.code.returnPressed.connect(self.push2)
        self.shuaxin.clicked.connect(self.CreatTable)
        
        
    def packed(self):        
        sql = "update outcode set ischecked='PASS',count="+self.nownum.text()+" where carton= '"+self.outcode.text()+"'"
       # print(sql)
        isresult = self.ms.run(sql)
        if isresult==True:
            self.Alert("打包成功！")
            self.outcode.setText('')
            self.yushe.setText('0')
            self.nownum.setText('0')
            self.outcode.setFocus(True)
            return True
        else:
            self.Alert("打包失败！")
            return False
        
    def auth(self):
        allcount = int(self.yushe.text())
        nownum = int(self.nownum.text())
        if nownum<allcount:            
            self.nownum.setText(str(nownum))
            return True
        else:
            return False
            
        
    #扫描验证    
    def push1(self):
        outcode_str = self.outcode.text()
        outcode_str = outcode_str.replace(' ','')
        outcode_str = outcode_str.replace("\n",'')
        self.outcode.setText(outcode_str)
        
        print(outcode_str)
        if self.outcode.text()=="":
            self.Alert("外箱码不得为空！")
            return False
        else:            
            sql1 = "select ischecked,count from outcode where carton ='"+self.outcode.text()+"'"
            data = list(self.ms.get(sql1))
            if len(data)!=0:     
                data = data[0]
                if data[0]=='false':
                    self.Alert("扫描异常！")
                elif  data[0]=='PASS':
                    self.Alert("该条码已关闭使用！")
                else:
                    self.code.setFocus(True)
                    #self.yushe.setText(str(data[1]))
                    self.yushe.setText("3")
                    
                    sql = "select count(*) from getout where cartonno ='"+self.outcode.text()+"'"
                    datas = list(self.ms.get(sql))
                    if len(datas)!=0:
                        self.nownum.setText(str(datas[0][0]))
            else:
                print("NO DATA!")
    #扫描验证    
    def push2(self):
        if len(self.outcode.text())!=0:            
            if len(self.code.text())!=34:
                self.Alert("您扫描的二维码有误！")
            else:
                #=========================判断数量是否符合大===============================
                allcount = int(self.yushe.text())
                nownum = int(self.nownum.text())
                if nownum<allcount:            
                    self.nownum.setText(str(nownum))
                    sql1 = "select id from code where code ='"+self.code.text()+"' and isuse = 'true' "
                    data = self.ms.get(sql1)
                    if data!=[]:
                        orderid     =   'TR8BE11TW06I5G10050021XX20C02U000I'
                        preid       =   '10086'
                        code        =   self.code.text()
                        creatuser   =   self.username
                        isout       =   'true'
                        data2 = self.ms.get("select id from getout where code ='"+code+"'")
                        if data2==[]:
                            insql =  "INSERT INTO getout (code, datetimes, creatuser, isout,cartonno) VALUES"
                            insql += "('"+code+"',(getdate()),'"+creatuser+"','"+isout+"','"+self.outcode.text()+"')"
                            self.ms.run(insql)
                            self.Lent=self.Lent+1
                            self.count.setText(str(self.Lent))
                            #--------------------------------------
                            nownum=nownum+1
                            if nownum!=allcount:
                                self.nownum.setText(str(nownum))
                            else:
                                self.nownum.setText(str(nownum))
                                self.packed()
                            
                        else:
                            self.Alertm("已出库！")
                    else:
                        self.Alertm("没有该条码！")
                    self.code.setText('')
                    
                    
                    

                #========================================================
            
            
            
            
            
                
        else:
            self.Alert("外箱条码不得为空！")
            
    def CreatTable(self):
        data = self.ms.get("select top 100 id,code,creatuser,datetimes,cartonno from getout where isout='true' and creatuser='"+self.username+"' and  CONVERT(VARCHAR(10),datetimes,120)= CONVERT(VARCHAR(10),GETDATE(),120) order by id desc")
       # print(data)
        if data!=():
            data = list(data)
        else:
            data = []
        self.codelist.setRowCount(len(data))
        self.codelist.setColumnCount(5)#设置列    
        self.codelist.setHorizontalHeaderLabels(['id','SN','操作人员','操作日期','外箱条码'])
        for i in range(len(data)):
            for n in range(len(data[i])):
                datas = str(data[i][n])
                if n==3:
                    if  len(datas)==26:
                        datas=datas[:-3]
                    elif len(datas)==19:
                        datas=datas+'.000'                        
                     
                newItem = QTableWidgetItem(datas)
                if n==0:
                    newItem.setTextAlignment(Qt.AlignCenter)
                    self.codelist.setItem(i,0, newItem)
                    self.codelist.setColumnWidth(0,160)
                
                if n==1:
                    newItem.setTextAlignment(Qt.AlignCenter)
                    self.codelist.setItem(i,1, newItem)
                    self.codelist.setColumnWidth(1,410)
                    
                if n==2:
                    newItem.setTextAlignment(Qt.AlignCenter)
                    self.codelist.setItem(i,2, newItem)
                    self.codelist.setColumnWidth(2,120)
                    
                if n==3:
                    newItem.setTextAlignment(Qt.AlignCenter)
                    self.codelist.setItem(i,3, newItem)
                    self.codelist.setColumnWidth(3,200)
                if n==4:
                    newItem.setTextAlignment(Qt.AlignCenter)
                    self.codelist.setItem(i,4, newItem)
                    self.codelist.setColumnWidth(4,200)
     
    def meau1(self):
        #1是只开条码 2是只开出库3是全开对吧  
        self.SonClick.emit("1")
        if self.root!=1:
            self.close()
    def meau2(self):
        self.SonClick.emit("2")
        if self.root!=2:
            self.close()
    def meau3(self):
        self.SonClick.emit("3")
        if self.root!=1:
            self.close()
    def meau4(self):
        self.SonClick.emit("4")
        if self.root!=1:            
            self.close()
      
     
#加载出货扫描界面
class OutProt(QWidget, Ui_OutProt, BoxSing):
    SonClick = pyqtSignal(str)
    def __init__(self,parent=None):
        super(OutProt, self).__init__(parent)
        self.setupUi(self)
        self.file_path=""
        self.Dis=""
        self.node = Node()
        self.ms = MSSQL()
        self.username = self.node.get("userinfo","username")
        self.root = int(self.node.get("userinfo","root"))
        self.loadings()
        
    def loadings(self):
        self.tab1.clicked.connect(self.meau1)
        self.tab2.clicked.connect(self.meau2)
        self.tab3.clicked.connect(self.meau3)
        self.tab4.clicked.connect(self.meau4)
        
        self.outcode.returnPressed.connect(self.push1)
        self.out.returnPressed.connect(self.push2)
        self.shuaxin.clicked.connect(self.CreatTable)
        self.choosurl.clicked.connect(self.choosefile)
        self.reset.clicked.connect(self.saveConfig)
        self.bulkprint.clicked.connect(self.PrintCode)
        
        #原产地
        self.gudingno.setText(self.node .get("product", "gudingno"))
        #固定编号
        self.yuanchanno.setText(self.node .get("product", "yuanchanno"))
        #批号
        self.pihaono.setText(self.node .get("product", "pihaono")) 
        now2 = strftime('%Y/%m/%d',time.localtime(time.time()))
        now = datetime.datetime.strptime(now2,'%Y/%m/%d')
        noweek = strftime('%W',time.localtime(time.time()))
        self.zhoubieno.setText(noweek)
        self.dateEdit.setDate(now)
        self.CreatTable()
        
    def  get_date(self):
        now2 = self.dateEdit.date()
        mmm = now2.toString("M")
        if int(mmm)<10:
            mmm="0"+mmm
        timestr =now2.toString("yyyy")+mmm+now2.toString("dd")
        return timestr
    def push1(self):
        carton = self.outcode.text()
        datas = list(self.ms.get("select * from outcode where carton='"+carton+"' and ischecked='PASS'"))
        if datas!=[]:
            datas = datas[0]
            #客户料号
            self.metaid.setText(str(datas[8]))
            #模号
            self.mode.setText(str(datas[9]))
            #穴号
            self.hole.setText(str(datas[10]))
            
            #每箱数量
            self.meixiangno.setText(str(datas[4]))
            #流水号
            self.liushuino.setText(str(datas[12]))            
            datas2 = list(self.ms.get("select * from outproduct where cartonno='"+carton+"'"))
            if datas2==[]:
                self.PutOutCode()
            else:
                self.Alert("已存在记录！")
            
        else:
            self.Alert("条码为使用或条码不存在！")
            
    def push2(self):    
        sql = "select * from outproduct where isgo='true' and outproduct='"+self.out.text()+"'"
        isok = list(self.ms.get(sql))
        if isok==[]:
            sql = "update outproduct set isgo='true' where outproduct='"+self.out.text()+"'"
            isok = self.ms.run(sql)
            if isok==True:
                self.out.setText("")
               
        else:
            self.Alert("已出货！")
        
    def CreatTable(self):
        data = self.ms.get("select top 100 outproduct,addtime,cartonno,isgo from outproduct where 1=1 order by addtime desc")
        #@print(data)
        if data!=():
            data = list(data)
        else:
            data = []
        self.codelist.setRowCount(len(data))
        self.codelist.setColumnCount(4)#设置列    
        self.codelist.setHorizontalHeaderLabels(['出货码','生成时间','外箱条码','确认状态'])
        for i in range(len(data)):
            for n in range(len(data[i])):
                datas = str(data[i][n])
                if n==0:
                    newItem = QTableWidgetItem(datas)
                    newItem.setTextAlignment(Qt.AlignCenter)
                    self.codelist.setItem(i,0, newItem)
                    self.codelist.setColumnWidth(0,400)
                
                if n==1:       
                    time = datas.split(".")
                    if len(time)==2:
                        datas = time[0]
                    newItem = QTableWidgetItem(datas)
                    newItem.setTextAlignment(Qt.AlignCenter)
                    self.codelist.setItem(i,1, newItem)
                    self.codelist.setColumnWidth(1,200)
                    
                if n==2:                   
                    newItem = QTableWidgetItem(datas)
                    newItem.setTextAlignment(Qt.AlignCenter)
                    self.codelist.setItem(i,2, newItem)
                    self.codelist.setColumnWidth(2,200)

                if n==3:
                    if datas=="false":
                        datas="未出货"
                    else:
                        datas="已出货"
                    newItem = QTableWidgetItem(datas)
                    newItem.setTextAlignment(Qt.AlignCenter)
                    self.codelist.setItem(i,3, newItem)
                    self.codelist.setColumnWidth(3,200)
                    
        
    def saveConfig(self):
        self.node .set("product", "gudingno", self.gudingno.text())
        self.node .set("product", "yuanchanno", self.yuanchanno.text())
        self.node .set("product", "pihaono", self.pihaono.text())
        self.Alert("重载成功！")
    def PutOutCode(self):
        gudingno = self.gudingno.text()
        nowdate = self.get_date()
        pin = self.pin.text()
        mode = self.mode.text()
        if int(mode)<10:
            mode = "0"+mode
        hole = self.hole.text()
        waterid = self.liushuino.text()
        outproduct = gudingno+nowdate+pin+mode+hole+waterid
        self.outproduct.setText(outproduct)
        self.tip_4.setText(str(len(outproduct)))
        sql = "insert into printprod(metaid,meixiangno,mode,hole,banbenno,chanpinno,pin,gudingno,youxiao,pihaono,zhoubieno,yuanchanno,liushuino,outproduct)values"
        sql = sql+"('"+self.metaid.text()+"','"+self.meixiangno.text()+"','TD"+mode+"','"+self.hole.text()+"#','"+self.banbenno.text()+"','"+self.chanpinno.text()
        sql = sql+"','"+self.pin.text()+"','"+self.gudingno.text()+"','"+nowdate+"','"+self.pihaono.text()+"','"+self.zhoubieno.text()+"','"+self.yuanchanno.text()
        sql = sql+"','"+self.liushuino.text()+"','"+outproduct+"')"
        self.Dis = sql
        self.node .set("product", "gudingno", self.gudingno.text())
        self.node .set("product", "yuanchanno", self.yuanchanno.text())
        self.node .set("product", "pihaono", self.pihaono.text())
      
        
    def GetBtwList(self,path):
        self.file_path = path
        btwlst = ''
        pathlist = os.listdir(path)
        self.comboBox.clear()
        for filename in pathlist:
            if filename.endswith('btw'):
                self.comboBox.addItem(filename)    
                
    def choosefile(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Files)
        if dlg.exec_():
            #获取文件所有路径
            file_path= dlg.selectedFiles()
            file_path = file_path[0]
            savestr = file_path.split("/")
            lent = len(savestr)
            #获取文件名
            filename = savestr[lent-1]
            #获取文件路径
            file_path = file_path.replace(filename, "")
            self.GetBtwList(r''+file_path)  

    def PrintCode(self):        
        pmode = self.file_path+self.comboBox.currentText()
        if self.comboBox.currentText()!='':
            sql1 = "delete from printprod where 1=1"
            isdelete = self.ms.run(sql1)
            #是否已经删除
            if isdelete == True:
                #是否已经添加
                isinsert = self.ms.run(self.Dis)
                if isinsert == True: 
                    currentprinter = win32print.GetDefaultPrinter()
                    win32api.ShellExecute(0, "print", pmode, '/d:"%s"' % currentprinter, ".", 0)
                    sql = "insert into outproduct(outproduct,isgo,cartonno)values('"+self.outproduct.text()+"','false','"+self.outcode.text()+"')"
                    isinsert=self.ms.run(sql)
                    if isinsert == True:
                        self.CreatTable()
        else:
            self.Alert("请选择模板")
       
        
    def meau1(self):
        #1是只开条码 2是只开出库3是全开对吧  
        self.SonClick.emit("1")
        if self.root!=1:
            self.close()
    def meau2(self):
        self.SonClick.emit("2")
        if self.root!=2:
            self.close()
    def meau3(self):
        self.SonClick.emit("3")
        if self.root!=1:
            self.close()
    def meau4(self):
        self.SonClick.emit("4")
        if self.root!=1:            
            self.close()
        
#加载外箱条码界面
class OutSideCode(QWidget, Ui_OutSideCode, BoxSing):
    SonClick = pyqtSignal(str)  
    def __init__(self,parent=None):
        super(OutSideCode, self).__init__(parent)
        self.setupUi(self)
        self.file_path=""
        #缓存打印
        self.Dis=''
        self.lstid=''
        self.Lent=0
        node = Node()
        self.username = node.get("userinfo","username")
        self.root = int(node.get("userinfo","root"))
        #type 1为出厂 2为出货
        self.tab1.clicked.connect(self.meau1)
        self.tab2.clicked.connect(self.meau2)
        self.tab3.clicked.connect(self.meau3)
        self.tab4.clicked.connect(self.meau4)
        self.choosurl.clicked.connect(self.choosefile)
        self.codeset.clicked.connect(self.ChengeConfig)
        self.shuaxin.clicked.connect(self.CreatTable)
        self.bulkprint.clicked.connect(self.PrintCode)
        self.bulkdel.clicked.connect(self.DelCode)
        self.creatcode.clicked.connect(self.Printing)        
        self.selectAll.clicked.connect(self.isChoseAll)        
        self.CreatTable()
    def DelCode(self):
        ms = MSSQL()
        self.TabItemClick()
        ftxt=self.lstid
        if ftxt!='':
            sql = "delete from outcode where id IN ("+self.lstid[0:-1]+") and ischecked = 'false'"
            ms.run(sql)
            self.Alert("删除成功！")
            self.CreatTable()
        else:
            self.Alert("您还没有选择条码！")
    
    def CreatTable(self):
        ms = MSSQL()
        data = ms.get("select * from outcode where ischecked='false' order by id desc")
        if data!=():
            data = list(data)
        else:
            data = []
        self.Lent = len(data)
        self.codelist.setRowCount(len(data))
        self.codelist.setColumnCount(13)#设置列    
        self.codelist.setHorizontalHeaderLabels(['','id','条码','日期','品名','数量','机型','操作员','工单号','料号','模号','穴号','品质确认'])
        for i in range(len(data)):
            for n in range(len(data[i])):               
                datas = str(data[i][n])
                newItem = QTableWidgetItem(datas)
                newItem.setTextAlignment(Qt.AlignCenter)
                checkBox = QTableWidgetItem()
                checkBox.setCheckState(Qt.Unchecked)
                self.codelist.setItem(i, 0, checkBox)
                self.codelist.setColumnWidth(0,50)
                newItem.setTextAlignment(Qt.AlignCenter)
                if n==0:
                    self.codelist.setItem(i,1, newItem)
                    self.codelist.setColumnWidth(1,100)
                elif n==1:
                    self.codelist.setItem(i,2, newItem)
                    self.codelist.setColumnWidth(2,160)
                elif n==2:
                    self.codelist.setItem(i,n+1, newItem)
                    self.codelist.setColumnWidth(n+1,80)
                elif n==3 or n==4 or n==5 or n==9 or n==10 or n==11:
                    self.codelist.setItem(i,n+1, newItem)
                    self.codelist.setColumnWidth(n+1,70)
                else:
                    self.codelist.setItem(i,n+1, newItem)
                    self.codelist.setColumnWidth(n+1,100)


    def choosefile(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Files)
        if dlg.exec_():
            #获取文件所有路径
            file_path= dlg.selectedFiles()
            file_path = file_path[0]
            savestr = file_path.split("/")
            lent = len(savestr)
            #获取文件名
            filename = savestr[lent-1]
            #获取文件路径
            file_path = file_path.replace(filename, "")
            self.GetBtwList(r''+file_path)
    
    def GetBtwList(self,path):
        self.file_path = path
        btwlst = ''
        pathlist = os.listdir(path)
        self.comboBox.clear()
        for filename in pathlist:
            if filename.endswith('btw'):
                self.comboBox.addItem(filename)
 
    def PrintCode(self):
        ms = MSSQL()
        self.TabItemClick()
        ftxt=self.Dis
        if ftxt!='':
            pmode = self.file_path+self.comboBox.currentText()
            if self.comboBox.currentText()!='':
                sql1 = "delete from printout where 1=1"
                isdelete = ms.run(sql1)
                #是否已经删除
                if isdelete == True:
                    #是否已经添加
                    isinsert = ms.run(self.Dis)
                    if isinsert == True:                    
                        currentprinter = win32print.GetDefaultPrinter()
                        win32api.ShellExecute(0, "print", pmode, '/d:"%s"' % currentprinter, ".", 0)
                        sql = "update outcode set ischecked='true' where id IN ("+self.lstid[0:-1]+")"
                        ms.run(sql)
                        self.CreatTable()
            else:
                self.Alert("请选择模板")
        else:
            self.Alert("您还没有选择条码！")
            
    def ChengeConfig(self):
        self.child = CodeSet1()
        self.child.show()
    def TabItemClick(self):
        self.Dis =  "INSERT INTO printout(code,date,piname,count,machine,optname,kongid,metaid,mode,hole,ischecked,waterid) VALUES "
        self.lstid=''
        num = 0
        while num < self.Lent:
            item=self.codelist.item(num,0)
            if item.checkState()!=0:
                id=self.codelist.item(num,1).text()
                code=self.codelist.item(num,2).text()
                date=self.codelist.item(num,3).text()
                piname=self.codelist.item(num,4).text()
                count=self.codelist.item(num,5).text()
                machine=self.codelist.item(num,6).text()
                optname=self.codelist.item(num,7).text()
                kongid=self.codelist.item(num,8).text()
                metaid=self.codelist.item(num,9).text()
                mode=self.codelist.item(num,10).text()
                hole=self.codelist.item(num,11).text()
                ischecked=self.codelist.item(num,12).text()
                if ischecked == 'false':
                    ischecked = "PASS"                
                self.Dis+="('"+code+"','"+date+"','"+piname+"','"+count+"','"+machine+"','"+optname+"','"+kongid+"','"+metaid+"','"+mode+"','"+hole+"','"+ischecked+"','"+code[-6:]+"'),"
                self.lstid+=id+","
            num=+num+1
        self.Dis=self.Dis[0:-1]
        print(self.Dis)
    def isChoseAll(self):
        ischecked = self.selectAll.isChecked()
        if ischecked==True:
            self.TabItemClick()
            self.nSelectAll()
        else:
            self.nSelectNo()
    
    def nSelectAll(self):
        num = 0
        while num < self.Lent:
            item=self.codelist.item(num,0)
            if item.checkState()==0:
                self.codelist.item(num,0).setCheckState(Qt.Checked)      
            #如果值为1就全选    
            num=+num+1
            
    def nSelectNo(self):
        num = 0
        while num < self.Lent:
            item=self.codelist.item(num,0)
            if item.checkState()!=0:
                self.codelist.item(num,0).setCheckState(Qt.Unchecked)
            #如果值为1就全选    
            num=+num+1      
            
    def Printing(self):
        box = QMessageBox(QMessageBox.Question, self.tr("提示"), self.tr("请确认所有参数设置正确后再生成条码，以免生成错误数据和垃圾数据!"), QMessageBox.NoButton, self)
        yr_btn = box.addButton(self.tr("继续生成"), QMessageBox.YesRole)
        box.addButton(self.tr("返回设置"), QMessageBox.NoRole)
        box.exec_()
        if box.clickedButton()!= yr_btn:
            print('返回设置')
            self.ChengeConfig()
            return
        else:
            print('继续生成')
        #获取操作人员
       
        ms = MSSQL()
        dirn = ms.get("select * from outcodeset")
        dirn = list(dirn)[0]
        sql = "select count(*) from outcode where date='"+dirn[2]+"'and piname='"+dirn[3]+"'and machine='"+dirn[5]+"'and mode='"+dirn[9]+"'and hole='"+dirn[10]+"'"
        counts = ms.get(sql)
        if counts==():
            counts = 0
        else:
            counts = list(counts)[0][0]        
        
       # print(counts)
        #print(sql)
        #==================================================================SQL初始部分==================================================================   
        newcode=''
        num = int(self.creatnum.text())
       
        while num > 0:
        #==================================================================循环开始=====================================================================
            insql =  "INSERT INTO outcode(carton,date,piname,count,machine,optname,kongid,metaid,mode,hole,ischecked,waterid) VALUES "
            newcount = int(counts)+1
            count2 = newcount
            #获取新二维码序列
            newcount = self.ChangeNum(newcount)
            #判断缺几个数就补上几个0
            if len(newcount)==1:
                newcount ='00000'+str(newcount)
            elif len(newcount)==2:
                newcount ='0000'+str(newcount)
            elif len(newcount)==3:
                newcount ='000'+str(newcount)
            elif len(newcount)==4:
                newcount ='00'+str(newcount)
            elif len(newcount)==5:
                newcount ='0'+str(newcount)
                
            newcode = str(dirn[12])+"-"+dirn[3][0]+dirn[5]+dirn[9]+dirn[10]+newcount
            insql += "('"+newcode+"','"+dirn[2]+"','"+dirn[3]+"',"+str(dirn[4])+",'"+dirn[5]+"','"+self.username+"','"+dirn[7]+"','"+dirn[8]+"','"+dirn[9]+"','"+dirn[10]+"','false','"+newcount+"')"
            isgo = ms.run(insql) #插入新记录
            counts=counts+1
            num=num-1
        #==================================================================循环结束====================================================================
        self.CreatTable()
        self.Alert('生成成功！')
 
    def meau1(self):
        #1是只开条码 2是只开出库3是全开对吧  
        self.SonClick.emit("1")
        if self.root!=1:
            self.close()
    def meau2(self):
        self.SonClick.emit("2")
        if self.root!=2:
            self.close()
    def meau3(self):
        self.SonClick.emit("3")
        if self.root!=1:
            self.close()
    def meau4(self):
        self.SonClick.emit("4")
        if self.root!=1:            
            self.close()

            
#管理员登录
class LoginAdmin(QWidget, Ui_Admin, BoxSing):
    def __init__(self,parent=None):
        super(LoginAdmin, self).__init__(parent)
        self.setupUi(self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.start)
        self.timer.start(1000)
        self.gouser.clicked.connect(self.closewrap)
        self.limitword()
        self.loginbtn.clicked.connect(self.Login)
        self.password.returnPressed.connect(self.Login)
    def closewrap(self):
        self.close()
        self.log = UserLogin() 
        self.log.show() 
        
    def limitword(self):
        #限制账户验证
        reg1 = QRegExp("^[a-zA-Z0-9_-]{4,16}$")
        limitUser = QRegExpValidator(self)
        limitUser.setRegExp(reg1)
        #限制密码验证
        reg2 = QRegExp("^.*(?=.{6,})(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*? ]).*$")
        limitPass = QRegExpValidator(self)
        limitPass.setRegExp(reg2)
        self.username.setValidator(limitUser)
        #self.password.setValidator(limitPass)
        
    def start(self):
        self.timer.stop()
        ms = MSSQL()
        isok = ms.test()
        if isok == False:
            self.hide()
            self.log = Dataset() 
            self.log.show()
            
    def Login(self):
        username = self.username.text()
        password = self.password.text()
        password = hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()
        ms = MSSQL()
        relust = ms.get("select root from users where username='"+username+"'and password='"+password+"' and root = 9 ")
        if relust==[]:
            self.tip.setText("账户或密码错误！")
            self.tip.setStyleSheet("color:red;")
        else:
            node = Node()          
            node.set("userinfo","username",username)
            node.set("userinfo","root",str(relust[0][0]))
            self.tip.setText("正在登录...")
            self.tip.setStyleSheet("color:#41CD52;")
            self.timer.start(1000)
            self.timer.timeout.connect(self.operation)
            
    def operation(self):
        self.timer.stop()
        print("登录成功！")
        self.close()
        self.log = MainDantA() 
        self.log.show()
#加载主界面        
class MainDantA(QMainWindow, Ui_MainDantA, BoxSing):
    parentclicked = pyqtSignal(str) 
    def __init__(self,parent=None):
        super(MainDantA, self).__init__(parent)
        self.setupUi(self)
        ns = Node()
        self.root = int(ns.get("userinfo","root"))
        #1是只开条码 2是只开出库3是全开对吧        
        self.loadUserlist()
      
   
    #条码生成
    def loadUserlist(self):
        self.child = AdminUser()
        self.child.SonClick.connect(self.recv)#桥接子窗口链接
        self.MaingridLayout.addWidget(self.child)
        self.child.show()
    def recv(self,tab):       
        tab = tab.split(",")
        
        if tab[0]=="edituser":
            self.log = EditUser()
            self.log.username.setText(tab[1])
            self.log.nickname.setText(tab[2])
            self.log.root.setCurrentIndex(int(tab[3]))
            self.log.show()
        elif tab[0]=="exit":
            self.log = UserLogin() 
            self.log.show() 
            self.close()
            
            
#用户列表
class AdminUser(QWidget, Ui_AdminUser, BoxSing):
    SonClick = pyqtSignal(str)  
    def __init__(self,parent=None):
        super(AdminUser, self).__init__(parent)
        self.setupUi(self)
        self.ms = MSSQL()
        self.CreatTable()
        self.gosearch.clicked.connect(self.SearchTable)
        self.shuaxin.clicked.connect(self.CreatTable)
        self.exits.clicked.connect(self.ExitAdmin)
        self.add.clicked.connect(self.AddUser)
    
    def CreatTable(self):
        data = self.ms.get("select top 100 nickname,username,password,root,creattime from users")
        if data!=():
            data = list(data)
        else:
            data = []
        self.codelist.setRowCount(len(data))
        self.codelist.setColumnCount(5)#设置列    
        self.codelist.setHorizontalHeaderLabels(['用户名','用户ID','密码(当前为加密，不显示原密码)','权限','添加时间'])
        for i in range(len(data)):
            for n in range(len(data[i])):
                datas = str(data[i][n])
                if n==0:
                    newItem = QTableWidgetItem(datas)
                    newItem.setTextAlignment(Qt.AlignCenter)
                    self.codelist.setItem(i,0, newItem)
                    self.codelist.setColumnWidth(0,200)
                
                if n==1:       
                    time = datas.split(".")
                    if len(time)==2:
                        datas = time[0]
                    newItem = QTableWidgetItem(datas)
                    newItem.setTextAlignment(Qt.AlignCenter)
                    self.codelist.setItem(i,1, newItem)
                    self.codelist.setColumnWidth(1,200)
                    
                if n==2:                   
                    newItem = QTableWidgetItem(datas)
                    newItem.setTextAlignment(Qt.AlignCenter)
                    self.codelist.setItem(i,2, newItem)
                    self.codelist.setColumnWidth(2,300)

                if n==3:                   
                    if datas=="1":
                        datas = "打印条码"
                    elif datas=="2":
                        datas = "扫描条码"
                    elif datas=="3":
                        datas = "两个都行"
                    elif datas=="9":
                        datas = "超级管理员"
                    #print(datas)
                    newItem = QTableWidgetItem(datas)
                    newItem.setTextAlignment(Qt.AlignCenter)
                    self.codelist.setItem(i,3, newItem)
                    self.codelist.setColumnWidth(3,200)

                    self.codelist.setContextMenuPolicy(Qt.CustomContextMenu)######允许右键产生子菜单
                    self.codelist.customContextMenuRequested.connect(self.generateMenu)   ####右键菜单
                if n==4:                   
                    datas2 = datas.split(".")
                    if len(datas2)==2:
                        datas=datas2[0]
                    newItem = QTableWidgetItem(datas)
                    newItem.setTextAlignment(Qt.AlignCenter)
                    self.codelist.setItem(i,4, newItem)
                    self.codelist.setColumnWidth(4,200)

    def SearchTable(self):
        nickname =self.search.text()
        nickname = nickname.replace(" ","")
        data = self.ms.get("select nickname,username,password,root,creattime from users where nickname = '"+nickname+"'")
        if data!=():
            data = list(data)
        else:
            data = []
        self.codelist.setRowCount(len(data))
        self.codelist.setColumnCount(5)#设置列    
        self.codelist.setHorizontalHeaderLabels(['用户名','用户ID','密码(当前为加密，不显示原密码)','权限','添加时间'])
        for i in range(len(data)):
            for n in range(len(data[i])):
                datas = str(data[i][n])
                if n==0:
                    newItem = QTableWidgetItem(datas)
                    newItem.setTextAlignment(Qt.AlignCenter)
                    self.codelist.setItem(i,0, newItem)
                    self.codelist.setColumnWidth(0,200)
                
                if n==1:       
                    time = datas.split(".")
                    if len(time)==2:
                        datas = time[0]
                    newItem = QTableWidgetItem(datas)
                    newItem.setTextAlignment(Qt.AlignCenter)
                    self.codelist.setItem(i,1, newItem)
                    self.codelist.setColumnWidth(1,200)
                    
                if n==2:                   
                    newItem = QTableWidgetItem(datas)
                    newItem.setTextAlignment(Qt.AlignCenter)
                    self.codelist.setItem(i,2, newItem)
                    self.codelist.setColumnWidth(2,300)

                if n==3:                   
                    if datas=="1":
                        datas = "打印条码"
                    elif datas=="2":
                        datas = "扫描条码"
                    elif datas=="3":
                        datas = "两个都行"
                    elif datas=="9":
                        datas = "超级管理员"
                    print(datas)
                    newItem = QTableWidgetItem(datas)
                    newItem.setTextAlignment(Qt.AlignCenter)
                    self.codelist.setItem(i,3, newItem)
                    self.codelist.setColumnWidth(3,200)
                    
                if n==4:                   
                    datas2 = datas.split(".")
                    if len(datas2)==2:
                        datas=datas2[0]
                    newItem = QTableWidgetItem(datas)
                    newItem.setTextAlignment(Qt.AlignCenter)
                    self.codelist.setItem(i,4, newItem)
                    self.codelist.setColumnWidth(4,200)  
    
    def generateMenu(self,pos):
        #print( pos)
        row_num = -1
        column=0
        for i in self.codelist.selectionModel().selection().indexes():
            row_num = i.row()
            column=i.column()
        
        menu = QMenu()
        item1 = menu.addAction(u"编辑")
        item2 = menu.addAction(u"删除")
        action = menu.exec_(self.codelist.mapToGlobal(pos))
        if action == item1:
            username = self.codelist.item(row_num,1).text()
            nickname = self.codelist.item(row_num,0).text()
            root = self.codelist.item(row_num,3).text()
            if root=="超级管理员":
                root = "0"
            elif root=="打印条码":
                root = "1"
            elif root=="扫描条码":
                root = "2"
            elif root=="两个都行":
                root = "3"
            self.EditUser("edituser,"+username+","+nickname+","+root)
        elif action == item2:           
            bools = self.Comfirm("您确定要删除吗？")
            if bools==16384:
                print("开始删除")
                self.DelUser(self.codelist.item(row_num,1).text())
            else:
                return
        else:
            return
    #删除用户
    def DelUser(self,id):
        sql = "delete from users where username='"+id+"'"
        isrun = self.ms.run(sql)
        if isrun == True:
            self.Alert("删除成功！")
            self.CreatTable()
        else:
            self.Alert("删除失败！")
    #添加用户
    def AddUser(self):
        self.log = AddUser()
        self.log.show()  
        
    #编辑用户
    def EditUser(self,str):
        self.SonClick.emit(str)
        
    def ExitAdmin(self):
        self.SonClick.emit("exit,zero")
         

class AddUser(QWidget, Ui_AddUser, BoxSing):
    SonClick = pyqtSignal(str)  
    def __init__(self,parent=None):
        super(AddUser, self).__init__(parent)
        self.setupUi(self)
        self.ms = MSSQL()
        self.limitword()
        self.regiter.clicked.connect(self.postform)
    def postform(self):
        username = (self.username.text()).replace(" ","")
        nickname = (self.nickname.text()).replace(" ","")
        password = self.password.text()
        password2 = self.password2.text()
        root = self.root.currentIndex()
        rootlst = ['9','1','2','3']
        if password==password2:
            password = hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()
            sql = "INSERT INTO users (username,nickname,password,root)values('"+username+"','"+nickname+"','"+password+"',"+rootlst[root]+")"
            msn = self.ms.run(sql)
            if msn==False:
                self.Alert("添加失败")
            else:
                self.Alert("添加成功！")
            
        else:
            self.Alert("两次密码输入不一致")
    
    def limitword(self):
        #限制账户验证
        reg1 = QRegExp("^[a-zA-Z0-9_-]{4,16}$")
        limitUser = QRegExpValidator(self)
        limitUser.setRegExp(reg1)
        #限制密码验证
        reg2 = QRegExp("^.*(?=.{6,})(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*? ]).*$")
        limitPass = QRegExpValidator(self)
        limitPass.setRegExp(reg2)
        self.username.setValidator(limitUser)
        self.password.setValidator(limitPass)
        self.password2.setValidator(limitPass)
       
        
        
class EditUser(QWidget, Ui_EditUser, BoxSing):
    def __init__(self,parent=None):
        super(EditUser, self).__init__(parent)
        self.setupUi(self)
        self.ms = MSSQL()
        self.update.clicked.connect(self.postform)
    def postform(self):
        username = self.username.text()
        nickname = self.nickname.text()
        password = self.password.text()
        password2 = self.password2.text()
        root = self.root.currentIndex()
        rootlst = ['9','1','2','3']
        if password==password2:
            sql = "update users set username='"+username+"',nickname='"+nickname+"',"
            if password!="":
                password = hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()
                sql = sql + "password='"+password+"',"
            sql = sql+"root="+rootlst[root]+" where username = '"+username+"'"
            #print(sql)
            msn = self.ms.run(sql)
            if msn==False:
                self.Alert("更新失败")
            else:
                self.Alert("更新成功！")
            
           
        else:
            self.Alert("两次密码输入不一致")
#加载配置1 外箱条码
class CodeSet1(QWidget, Ui_CodeSet1, BoxSing):
    def __init__(self,parent=None):
        super(CodeSet1, self).__init__(parent)
        self.setupUi(self)
        self.ns = Node()
        self.LimitInput()#限制输入
        self.username=self.ns.get('userinfo','username')
        self.loading()#加载初始化数据
        self.cunchu.clicked.connect(self.Cunchu)#存储按钮事件
        self.mons = ['A','B','C','D', 'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W']
        
    def LimitInput(self):
        reg1 = QRegExp("^[A-Za-z0-9_-]{4,16}$")
        limit1 = QRegExpValidator(self)
        limit1.setRegExp(reg1)
        reg2 = QRegExp("^(([1-9][0-9]*)|(([0]\.\d{1,2}|[1-9][0-9]*\.\d{1,2})))$")
        limit2 = QRegExpValidator(self)
        limit2.setRegExp(reg2)
        
        self.wei.setValidator(limit2)
        self.nowdate.setValidator(limit2)
        self.piname.setValidator(limit1)
        self.count.setValidator(limit2)
        self.machine.setValidator(limit1)
        self.optname.setValidator(limit1)
        
        self.kongid.setValidator(limit1)
        #self.metaid.setValidator(limit1)
        self.mode.setValidator(limit1)
        self.hole.setValidator(limit1)
        self.waterid.setValidator(limit1)

    def loading(self):
        creator = self.username
        ms = MSSQL()
        db = list(ms.get("select * from  outcodeset"))       
        dt = time.localtime()
        ft = '%Y%m%d'
        nt = time.strftime(ft,dt)
        self.nowdate.setText(nt)
        if db!=[]:            
            db = db[0]
            #默认选中                   
            self.head.setText(db[12])
            self.wei.setText(str(db[13]))
            self.piname.setText(db[3])
            self.count.setText(str(db[4]))
            self.machine.setText(str(db[5]))
            self.optname.setText(creator)
            
            
            self.kongid.setText(db[7])
            self.metaid.setText(db[8])
            self.mode.setText(db[9])
            self.hole.setText(db[10])
            self.waterid.setText('000001')
        else:
            print("暂无配置")
        
  
     #存储格式
    def Cunchu(self):
        ms = MSSQL()
        head = self.head.text()
        wei = self.wei.text()
        nowdate = self.nowdate.text()
        piname = self.piname.text()
        count = self.count.text()
        machine = self.machine.text()
        optname = self.optname.text()
            
            
        kongid = self.kongid.text()
        metaid = self.metaid.text()
        mode = self.mode.text()
        hole = self.hole.text()
        waterid = self.waterid.text()
        code =head+"-"+piname[0]+machine+mode+hole+waterid        
        if len(code) == int(wei):
            self.codeshow.setText(code)
            sql = "update outcodeset set code = '"+code+"',dates = '"+nowdate+"', piname='"+piname+"',count='"+count+"',machine='" + machine+"'"
            sql = sql+",optname='"+optname+"',kongid='"+kongid+"',metaid='"+metaid+"',mode='"+mode+"',hole='"+hole+"',waterid='"+waterid+"',head='"+head+"',wei="+wei+""
            isupdate = ms.run(sql)
            if isupdate==True:
                self.close()
                print("保存成功！")
        else:
            self.Alert("条码为"+str(len(code))+"位！")
            
    def Alertc(self,str):
        dialog = QDialog()
        tip =QLabel(str,dialog)
        tip.move(10,10)
        btn = QPushButton("确定",dialog)
        btn.move(50,70)
        dialog.setWindowTitle("温馨提示")
        dialog.setWindowModality(Qt.ApplicationModal)
        btn.clicked.connect(dialog.hide)
        dialog.exec_()
        self.hide()
#加载配置2 条码生成
class CodeSet2(QWidget, Ui_CodeSet2):
    def __init__(self,parent=None):
        super(CodeSet2, self).__init__(parent)
        self.setupUi(self)
        self.ns = Node()
        self.LimitInput()#限制输入
        self.username=self.ns.get('userinfo','username')
        self.loading()#加载初始化数据
        self.cunchu.clicked.connect(self.Cunchu)#存储按钮事件
        self.mons = ['A','B','C','D', 'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W']
        
    def LimitInput(self):
        reg1 = QRegExp("^[A-Z0-9_-]{4,16}$")
        limit1 = QRegExpValidator(self)
        limit1.setRegExp(reg1)
        reg2 = QRegExp("^(([1-9][0-9]*)|(([0]\.\d{1,2}|[1-9][0-9]*\.\d{1,2})))$")
        limit2 = QRegExpValidator(self)
        limit2.setRegExp(reg2)
        self.compy.setValidator(limit1)
        self.product.setValidator(limit1)
        self.froms.setValidator(limit1)
        self.fromid.setValidator(limit1)
        self.dropid.setValidator(limit1)
        self.mode.setValidator(limit1)
        self.hole.setValidator(limit1)
        self.project.setValidator(limit1)
        self.picbate.setValidator(limit1)
        self.machine.setValidator(limit1)
        self.tiefrom.setValidator(limit1)
        self.keyint.setValidator(limit1)
        
    def loading(self):        
        ms = MSSQL()
        db = list(ms.get("select * from codeset"))[0]
        self.compy.setText(db[1])
        self.product.setText(db[2])
        now2 = strftime('%Y/%m/%d',time.localtime(time.time()))
        now = datetime.datetime.strptime(now2,'%Y/%m/%d')
        self.dat.setDate(now)
        #默认选中
        self.comboBox.setCurrentIndex(int(db[4])-1)
        self.froms.setText(db[5])
        self.fromid.setText(db[6])
        self.dropid.setText(db[7])
        self.mode.setText(db[8])
        self.hole.setText(db[9])
        self.project.setText(db[10])
        self.picbate.setText(db[11])
        self.machine.setText(db[12])
        self.tiefrom.setText(db[13])
        self.keyint.setText('JKD2')
    def FormatDates(self,dat):
        dateft = dat.split('/')
        year = dateft[0]
        mon =dateft[1]
        day = dateft[2]
        year = year[-1]
        if int(mon)>=10:
            mon = int(mon) %10
            mon = self.mons[mon]
        if int(day)>=10:
            day = int(day)-10
            day = self.mons[day]
        return year+mon+day   
     #存储格式
    def Cunchu(self):
        compy = self.compy.text()
        product = self.product.text()
        dat1 = self.dat.text()
        dat2 = self.FormatDates(dat1)
        comboBox = str(self.comboBox.currentIndex()+1)
        froms = self.froms.text()
        fromid = self.fromid.text()
        dropid = self.dropid.text()
        mode = self.mode.text()
        hole = self.hole.text()
        project = self.project.text()
        picbate = self.picbate.text()
        machine = self.machine.text()
        tiefrom = self.tiefrom.text()
        keyint = self.keyint.text()
        strs = compy+product+dat2+comboBox+froms+fromid+dropid+mode+hole+project+picbate+machine+tiefrom+keyint
        if len(strs)==34:
            #显示代码
            self.codeshow.setText(strs)
            creator = self.username
            #存储数据库
            ms = MSSQL()
            sql ="update codeset set compy='"+compy+"',product='"+product+"',dat='"+dat2+"',comboBox='"+comboBox+"'"
            sql+=", froms='"+froms+"',fromid='"+fromid+"',dropid='"+dropid+"',mode='"+mode+"',"
            sql+="hole='"+hole+"',project='"+project+"',picbate='"+picbate+"',machine='"+machine+"',"
            sql+="tiefrom='"+tiefrom+"',datetimes='"+dat1+"'"
            ms.run(sql)
            self.Alertc("保存成功！")
        else:
            self.Alert("代码没有34位!")
            
    def Alertc(self,str):
        dialog = QDialog()
        tip =QLabel(str,dialog)
        tip.move(10,10)
        btn = QPushButton("确定",dialog)
        btn.move(50,70)
        dialog.setWindowTitle("温馨提示")
        dialog.setWindowModality(Qt.ApplicationModal)
        btn.clicked.connect(dialog.hide)
        dialog.exec_()
        self.hide()
        
