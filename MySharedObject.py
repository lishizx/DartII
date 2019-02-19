# -*- coding: utf-8 -*-
import win32print,win32api
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtWidgets import QWidget,QMessageBox
import datetime
import os


class MySharedObject(QWidget):
        
    def __init__( self):
        super( MySharedObject, self).__init__()
                    
    def _getStrValue( self):
        btwlst = ''
        path = r'C:\btw'
        pathlist = os.listdir(path)
        for filename in pathlist:
            if filename.endswith('btw'):
                print(filename)
                btwlst+=filename+','
        return btwlst        

    def _setStrValue( self,  str ):
        if str=="":
            print("isnobtw")
        else:
            currentprinter = win32print.GetDefaultPrinter()
            isok =  win32api.ShellExecute(0, "print", str, '/d:"%s"' % currentprinter, ".", 0);
            print('获得页面参数 ：%s'% str )
            if isok!="":
                nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(nowTime)

        
    #需要定义对外发布的方法    
    strValue = pyqtProperty(str, fget=_getStrValue, fset=_setStrValue)     
    
    
    
    
    
