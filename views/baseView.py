from PySide6.QtGui import QAction, QIcon, QShortcut, QKeySequence
from PySide6.QtWidgets import QMainWindow, QSystemTrayIcon, QMenu,QMessageBox
from PySide6.QtCore import Qt, QThread
from models.baseModel import BaseModel
import os
import signal

class BaseView(QMainWindow):
    _instance = None
    def __init__(self):
        super().__init__()
        self.controller = None  # 初始化控制器为 None
    
    def __new__(cls, *args, **kwargs):
        # 创建类对象时不需要args和kwargs参数
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
        
    def setWindow(self):
        self.setWindowTitle('蚂蚁直播助手 GPT4在线地址  aixiaoxin.com')
        self.setFixedSize(860,460)
        self.statusBar().hide()
    
    def set_controller(self, controller):
        self.controller = controller
            
    def closeEvent(self, event):
        # pid = os.getpid()  # 获取当前进程的PID
        # os.kill(pid, signal.SIGTERM)
        
        if self.controller:
            self.controller.on_close_event(event)
            # 这里可以选择不调用 super().closeEvent(event) 来阻止关闭
            # 但如果用户选择关闭，则需要调用
            # event.accept()  # 或者 event.ignore() 根据需要决定

        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()


    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_position)
            event.accept()
    
    def criticalWin(self, msg):
         QMessageBox.critical(self, "错误", msg)
