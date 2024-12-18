from models.danmuModel import DanmuModel
from views.danmuView import DanmuView
# from models.mainModel import MainModel
from controllers.baseController import BaseController
from PySide6.QtCore import Slot, QStringListModel
from PySide6.QtWidgets import QListWidgetItem
from services import douyin_live
from models.baseModel import AppWorker
import os

class DanmuController(BaseController):
    def __init__(self):
        super().__init__()
        self.view = DanmuView()
        self.model = DanmuModel()

        # self.view.show()
        
        # model = QStringListModel()
        # model = model.setStringList(['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6', 'Item 7', 'Item 8', 'Item 9', 'Item 10'])
        # self.view.danmu_list.setModel(model)
        # # for i in range(100):
        #     item = QListWidgetItem(f"Item {i + 1}")
        #     self.view.danmu_list.setModel(item)
        custom_js = """
        function customFunction() {
            alert("123123")
        }
        window.onload = customFunction;
        """

        self.view.setStyleSheet("background: transparent;")  # 设置样式表
        html = self.load_html("../resources/html/danmu.html")
        self.view.webEngineView.setHtml(html) 
        self.view.webEngineView.setStyleSheet("background: transparent;")
        # self.view.webEngineView.loadStarted.connect(self.on_load_started)
        

    def load_html(self, js_file):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        # print("dir_path", dir_path)
        js_path = os.path.join(dir_path, js_file)
        with open(js_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def on_load_started(self):
        custom_js = """
            function customFunction() {
                alert("123123");
            }
            customFunction();
        """
        self.view.webEngineView.page().runJavaScript(custom_js)