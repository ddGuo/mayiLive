from hmac import new
from PySide6.QtCore import QObject, QRunnable, QThreadPool, Signal
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from models.baseModel import AppWorker
from models.baseModel import BaseModel

class BaseController(QObject):
    def __init__(self):
        super().__init__()
        
    def on_close_event(self, event):
        # thread_pool = self.model.thread_pool
        # active_threads = thread_pool.activeThreadCount()
        # print("active_threads", active_threads)

        # 如果是主窗口，关闭ws服务端 ，关闭弹幕ws客户端，关闭ws客户端
        from controllers.mainController import MainController
        if isinstance(self, MainController):
            self.model.emit_signal({"ws_websocker_server" : "stop", "ws_danmu" : "stop", "ws_websocker_app" : "stop"})



        
