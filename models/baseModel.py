from PySide6.QtCore import QObject, QRunnable, QThreadPool, Signal
from collections import defaultdict
from services.utils.webSocketServer import WebSocketServer
from services.utils.webSocketApp import WebSockerApp

class AppWorker(QRunnable):
    def __init__(self, func, signal, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.signal = signal

    def run(self):
        try:
            print("QRunnable 1")    
            # print("self.func", self.func)
            if isinstance(self.func, WebSocketServer):
                self.func.start_server()
            elif isinstance(self.func, WebSockerApp):
                self.func.start()
            else:
                res = self.func(*self.args, **self.kwargs)
                # 任务完成后发出信号
                # self.signal.emit('ws抓取彈幕完成')
        except Exception as e:
            print("QRunnable 2", e)
        finally:
            print("QRunnable 3")
            
class BaseModel(QObject):
    _instance = None
    signal = Signal(dict)
    
    def __new__(cls, *args, **kwargs):
        # 创建类对象时不需要args和kwargs参数
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()
        
        self.thread_pool = QThreadPool.globalInstance()
        self.thread_status_map = defaultdict(bool)
        
    def emit_signal(self, dict_param):
        # data = {"key1": "value1", "key2": "value2"}
        # print("emit_signal 1111", dict_param)
        self.signal.emit(dict_param)
        # print("emit_signal 2222", dict_param)
    