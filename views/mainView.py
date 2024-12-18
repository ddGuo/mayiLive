from resources.ui.mainView_ui import Ui_MainWindow
from PySide6.QtGui import QAction, QIcon, QShortcut, QKeySequence
from PySide6.QtWidgets import QMainWindow, QSystemTrayIcon, QMenu, QStatusBar, QToolBar
from views.baseView import BaseView


class MainView(BaseView, Ui_MainWindow):
      def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.setWindow()
        