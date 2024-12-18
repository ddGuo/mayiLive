from controllers.danmuController import DanmuController
from views.mainView import MainView
from models.mainModel import MainModel
from controllers.baseController import BaseController
from PySide6.QtCore import Slot
from services import douyin_live
from models.baseModel import AppWorker
from services.utils.webSocketServer import WebSocketServer
from services.utils.webSocketApp import WebSockerApp
from functools import partial

class MainController(BaseController):
    def __init__(self):
        super().__init__()
        self.msg = {"1":"直播已结束","2":"直播中"}
        self.view = MainView()
        self.model = MainModel()
        self.view.show()
        self.view.set_controller(self)
        
        self.model.signal.connect(self.all_signal)
        
        # 启动websocket服务端
        worker_webSocket_server = AppWorker(WebSocketServer(), "none")
        self.model.thread_pool.start(worker_webSocket_server)
        webSocket_server = WebSocketServer()
        self.model.signal.connect(partial(webSocket_server.stop))
        
        # 左侧菜单栏
        self.left_menu_button_list = [
            self.view.left_menu_button_1,
            self.view.left_menu_button_2,
            self.view.left_menu_button_3,
            self.view.left_menu_button_4
        ]
        for i, btn in enumerate(self.left_menu_button_list):
            btn.clicked.connect(self.changeLeftMenu)
        self.view.content.setCurrentIndex(0)
        
        # 页面1
        self.platform_check_list = {
            self.view.platform_check_1 : "douyin",
            self.view.platform_check_2 : "kuaishou"
        }
        for k, v in self.platform_check_list.items():
            k.stateChanged.connect(self.checkPlatform)


        # 页面1 连接
        self.view.url_connect.clicked.connect(self.urlConnect)
        self.view.url_disconnect.clicked.connect(self.urlDisconnect)
        
        # 页面1 功能
        self.view.function_1.stateChanged.connect(self.danmuWin)
        self.danmu_win = DanmuController()
        self.danmu_win.view.set_controller(self.danmu_win)
        
    # 切换左侧菜单 
    @Slot()
    def changeLeftMenu(self):
        sender_button = self.sender().objectName()
        for i, btn in enumerate(self.left_menu_button_list):
            if btn.objectName() == sender_button:
                btn.setStyleSheet(f"QPushButton {{ background-color: rgb(40, 58, 78); border: none; color: rgb(255, 255, 255); }}")
            else:
                btn.setStyleSheet(f"QPushButton {{ border: none; color: rgb(193, 174, 153); }}")
            
            if sender_button == "left_menu_button_1":
                self.view.content.setCurrentIndex(0)
            elif sender_button == "left_menu_button_2":
                self.view.content.setCurrentIndex(1)
            elif sender_button == "left_menu_button_3":
                self.view.content.setCurrentIndex(2)
            else:
                self.view.content.setCurrentIndex(3)
    
    # 选择直播平台 
    @Slot()
    def checkPlatform(self, state):
        sender_check_platform = self.sender().objectName()
        if state == 2: # Qt.Checked 的状态值是 2
            for k, v in self.platform_check_list.items():
                if k.objectName() != sender_check_platform:
                    k.setChecked(False)
    
    # 连接弹幕 
    @Slot()
    def urlConnect(self):
        # url = self.view.url_address.text()  do_something(url) 使用，会导致程序卡死
        worker = AppWorker(self.live, self.model.signal)
        self.model.thread_pool.start(worker)
        # self.model.signal.connect(self.threadFinished)
        self.model.signal.connect(douyin_live.wssServerStop)
        
        
    def live(self):
        url = self.view.url_address.text()
        douyin_live.parseLiveRoomUrl(url) 

    # 断开弹幕 
    @Slot()
    def urlDisconnect(self):
        # douyin_live.wssServerStop()  
        self.model.emit_signal({"ws_danmu" : "stop", "ws_websocker_app" : "stop"})
        self.view.url_connect.setEnabled(True)
        # self.view.url_connect.setStyleSheet("background-color: grey; border:none;")
        self.view.url_connect.setStyleSheet(u"QPushButton#url_connect {\n"
        "    border : none;\n"
        "	color:#000000;\n"
        "	background-color: #ffc7a0;\n"
        "	font: 9pt \"Microsoft YaHei\";\n"
        "}\n"
        "QPushButton#url_connect:hover {\n"
        "    border : none;\n"
        "	color: #ffffff;\n"
        "	background-color: #391461;\n"
        "}")

    @Slot(str, dict)
    def threadFinished(self, dict):
        print('thread_finished', dict)
    
    # 弹幕助手  打开弹幕助手窗口
    @Slot()
    def danmuWin(self):
        if self.view.function_1.isChecked():
            self.danmu_win.view.show()
        else:
            self.danmu_win.view.hide()
    
    @Slot()    
    def all_signal(self, dict_param):
        if dict_param.get("msg_code") and dict_param.get("msg_code") == "1":
            self.view.criticalWin(self.msg.get(dict_param.get("msg_code")))
        
        if dict_param.get("msg_code") and dict_param.get("msg_code") == "2":
            self.view.url_connect.setEnabled(False)
            self.view.url_connect.setStyleSheet("background-color: grey; border:none; color: #8492a6")
            
            # 启动websocket客户端
            worker_webSocket_app = AppWorker(WebSockerApp(), "none")
            self.model.thread_pool.start(worker_webSocket_app)
            webSocket_app = WebSockerApp()
            self.model.signal.connect(partial(webSocket_app.close))
            
            self.view.room_nickname.setText(dict_param.get("room_nickname"))
  