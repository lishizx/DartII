# -*- coding:utf-8 -*-
import configparser
import pymssql,datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
class MSSQL:
    def __init__(self):
        self.host = ""
        self.user = ""
        self.pwd = ""
        self.db = ""
        n = Node()
        self.host  = n.get('sqlserver','db_host')
        self.user  = n.get('sqlserver','db_user')
        self.pwd  = n.get('sqlserver','db_pass')
        self.db  = n.get('sqlserver','db_name')
        
    def test(self):
        try:  #尝试执行缩进下面的报错
            if not self.db:
               raise(NameError,'没有设置数据库信息')
            self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset='utf8')
            cur = self.conn.cursor()
            return True
        except:  
            return False

    def GetConnect(self):
        if not self.db:
            raise(NameError,'没有设置数据库信息')
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset='utf8')
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,'连接数据库失败')
        else:
            return cur
 
    def get(self,sql):
        cur = self.GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()
        self.conn.close()
        return resList
 
    def run(self,sql):
        try:  #尝试执行缩进下面的报错
            cur = self.GetConnect()
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
            return True
        except:  
            return False
       
    def Alert(self,str):
        dialog = QDialog()
        tip =QLabel(str,dialog)
        tip.move(10,10)
        btn = QPushButton("确定",dialog)
        btn.move(50,70)
        dialog.setWindowTitle("温馨提示")
        dialog.setWindowModality(Qt.ApplicationModal)
        btn.clicked.connect(dialog.hide)
        dialog.exec_()

class Node:
    def __init__(self):
        self.config_path = 'config.ini'
        self.cf = configparser.ConfigParser()
        self.cf.read(self.config_path )
    def set(self,parent,node,value):
        self.cf.set(parent,node,value)
        self.cf.write(open(self.config_path ,'w'))
    def get(self,parent,node):
        config = configparser.ConfigParser()
        config.readfp(open('config.ini'))
        a = config.get(parent,node)
       # print(a)
        return a
        
    def creat(self):
        config_path = 'config.ini'
        cf = configparser.ConfigParser()
        f=open(config_path,'w')
        #创建数据库连接
        f.write('[sqlserver]'+'\n')
        f.write('db_host = '+'\n')
        f.write('db_name = '+'\n')
        f.write('db_user = '+'\n')
        f.write('db_pass = '+'\n')
        f.write('[userinfo]'+'\n')
        f.write('username = '+'\n')
        f.write('root = '+'\n')
        f.write('[product]'+'\n')
        f.write('gudingno = '+'\n')
        f.write('pihaono = '+'\n')
        f.write('yuanchanno = '+'\n')
        f.write('[fileurl]'+'\n')
        f.write('urloutside = '+'\n')#外箱条码路径
        f.write('urlcode = '+'\n')#生成条码路径
        f.write('urlprod = '+'\n')#出货条码路径
        f.close()
        
class BoxSing:
    def Alert(self,str):
        dialog = QDialog()
        tip =QLabel(str,dialog)
        tip.move(10,10)
        btn = QPushButton("确定",dialog)
        btn.move(50,70)
        dialog.setWindowTitle("温馨提示")
        dialog.setWindowModality(Qt.ApplicationModal)
        btn.clicked.connect(dialog.hide)
        dialog.exec_()
    
        
    def Alertm(self,str):
        dialog = QDialog()
        tip =QLabel(str,dialog)
        tip.move(10,10)
        dialog.resize(350,100)
        #btn = QPushButton("确定",dialog)
        #btn.move(50,70)
        dialog.setWindowTitle("温馨提示")
        dialog.setWindowModality(Qt.ApplicationModal)
        #btn.clicked.connect(dialog.hide)
        dialog.exec_()
    def Comfirm(self,str):
        comfirm = QMessageBox.information(self,"提示",str,QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        return comfirm
    #进制转换
    def ChangeNum(self,num):
        mons = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D', 'E','F','G','H','I','J','K','L','M','N','O','P','Q']
        backnum = ''
        if num == 0:
            backnum = mons[0]
        
        while num>0:
            sm =int( num % 26)
            backnum = mons[sm] + backnum
            num = (num-sm) / 26
        return backnum