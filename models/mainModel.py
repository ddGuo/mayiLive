from PySide6.QtCore import QObject, QRunnable, QThreadPool, Signal
from models.baseModel import BaseModel

class MainModel(BaseModel):
    def __init__(self):
        super().__init__()
        print("MainModel")