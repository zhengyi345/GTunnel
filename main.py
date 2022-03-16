# -*- coding: utf-8 -*-

from gtunnel import Ui_GTunnel
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from PySide2 import QtWidgets
import subprocess, sys



class MainWindow(QtWidgets.QMainWindow, Ui_GTunnel):

    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        global profilename
        profilename = None
        
    def LoadFile(self):
        global profilename
        profilename, _ = QFileDialog.getOpenFileName(self,'选择配置文件', './','Json Files (*.json);;All Files (*)')
        if not profilename:
            print('未加载配置文件')
            self.label_2.setText('未加载')
        else:
            print('已加载配置文件:%s' %profilename)
            self.label_2.setText(profilename)
            

    def RunSer(self):
        
        if  profilename:
            command = 'gost.exe -C %s' %profilename
            subprocess.Popen(command)
            print('服务即将启动...')
            self.label_3.setText('running...')
        else:
            print('启动失败，请先加载配置文件')

           
            
    def StopSer(self):
        command = 'taskkill /f /im gost.exe'
        subprocess.Popen(command)
        print('服务已停止.')
        self.label_3.setText('stopped')



app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

