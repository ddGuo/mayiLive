import asyncio
import websockets
from PySide6.QtCore import Slot


class WebSocketServer():
    _instance = None
    
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 8899
        self.server = None
        self.clients = set()
        
    def __new__(cls, *args, **kwargs):
        # 创建类对象时不需要args和kwargs参数
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    async def handle_client(self, websocket):
        self.clients.add(websocket)
        try:
            async for message in websocket:
                await self.process_message(websocket, message)
        finally:
            self.clients.remove(websocket)
        # async for message in websocket:
        #     await self.process_message(websocket, message)

    async def process_message(self, websocket, message):
        # 在这里处理收到的消息，这里只是简单地将消息发送回客户端
        # print("process_message", message)
        # await websocket.send(message)
         for client in self.clients:
            if client != websocket:  # 不发送给消息的发送者
                await client.send(message)

    async def start(self):
        self.server = await websockets.serve(self.handle_client, self.host, self.port)
        print(f"WebSocket server started at ws://{self.host}:{self.port}")
        await self.server.wait_closed()

    def stop(self, dict_param):
        if self.server and dict_param.get("ws_websocker_server") == "stop":
            self.server.close()

    def start_server(self):
        server = WebSocketServer()
        asyncio.run(server.start())
        
