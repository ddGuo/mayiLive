from resources.ui.danmu_ui import Ui_DanmuWin
from PySide6.QtGui import QAction, QIcon, QShortcut, QKeySequence
from PySide6.QtWidgets import QMainWindow, QSystemTrayIcon, QMenu, QStatusBar, QToolBar, QListWidgetItem
from views.baseView import BaseView
from PySide6.QtCore import Qt

class DanmuView(BaseView, Ui_DanmuWin):
      def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.setFixedSize(300,660)
        self.setGeometry(1000,200,300,660)
      #   self.setWindowOpacity(0.5)

        # self.setWindowFlags(Qt.FramelessWindowHint) # 隐藏边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 背景透明


        
        
        

         
      
