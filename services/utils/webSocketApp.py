from time import sleep
import websocket
import threading

class WebSockerApp():
    _instance = None
    
    def __init__(self):
        self.ws = websocket.WebSocketApp("ws://127.0.0.1:8899", on_open = self.on_open, on_message = self.on_message, on_close = self.on_close, on_error = self.on_error)
        
    def __new__(cls, *args, **kwargs):
        # 创建类对象时不需要args和kwargs参数
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def on_open(self, ws):
        print("连接已建立")
        # 发送消息给服务器
        self.ws.send("Hello, server!")


    def on_message(self, ws, message):
        print("收到服务端的消息：", message)


    def on_close(self, ws, close_status_code, close_msg):
        print("on_close ws连接已关闭")


    def on_error(self, ws, error):
        print("发生错误：", error)


    def send_msg(self, msg: str):
        print("对外提供的方法" + msg)


    def ws_send(self, msg):
        if self.ws.keep_running:
            self.ws.send(msg)
        else:
            pass

    def start(self):
        print("websocketapp启动")
        self.ws.run_forever()       
        
    def close(self, dict_param): 
        if self.ws and dict_param.get("ws_websocker_app") == "stop":
            print("ws客户端关闭连接...")
            self.ws.close()
            print("ws客户端连接已关闭")


