import sys
from PySide6.QtWidgets import QApplication
from controllers.mainController import MainController

if __name__ == '__main__':
    # 同步图标
    # windll.shell32.SetCurrentProcessExplicitAppUserModelID('nothing')
    app = QApplication()
    # 关闭窗口时候不退出程序
    # app.setQuitOnLastWindowClosed(False)
    controller = MainController()
    # 事件循环
    sys.exit(app.exec())