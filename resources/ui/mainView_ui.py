# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainView.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStackedWidget, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 468)
        MainWindow.setAnimated(True)
        self.action_help = QAction(MainWindow)
        self.action_help.setObjectName(u"action_help")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 161, 461))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet(u"background-color: rgb(70, 86, 99);\n"
"border-color: rgb(0, 85, 255);")
        self.left_menu_button_1 = QPushButton(self.widget)
        self.left_menu_button_1.setObjectName(u"left_menu_button_1")
        self.left_menu_button_1.setGeometry(QRect(0, 130, 161, 31))
        self.left_menu_button_1.setStyleSheet(u"border-width : 0px;\n"
"border-color : rgb(170, 0, 255);\n"
"border-style : solid;\n"
"color : rgb(255, 255, 255);\n"
"background-color: rgb(40, 58, 78);")
        self.left_menu_button_2 = QPushButton(self.widget)
        self.left_menu_button_2.setObjectName(u"left_menu_button_2")
        self.left_menu_button_2.setGeometry(QRect(0, 160, 161, 31))
        self.left_menu_button_2.setStyleSheet(u"border-width : 0px;\n"
"border-color : rgb(170, 0, 255);\n"
"border-style : solid;\n"
"color : rgb(193, 174, 153);")
        self.left_menu_button_3 = QPushButton(self.widget)
        self.left_menu_button_3.setObjectName(u"left_menu_button_3")
        self.left_menu_button_3.setGeometry(QRect(0, 190, 161, 31))
        self.left_menu_button_3.setStyleSheet(u"border-width : 0px;\n"
"border-color : rgb(170, 0, 255);\n"
"border-style : solid;\n"
"color : rgb(193, 174, 153);")
        self.left_menu_button_4 = QPushButton(self.widget)
        self.left_menu_button_4.setObjectName(u"left_menu_button_4")
        self.left_menu_button_4.setGeometry(QRect(0, 220, 161, 31))
        self.left_menu_button_4.setStyleSheet(u"border-width : 0px;\n"
"border-color : rgb(170, 0, 255);\n"
"border-style : solid;\n"
"color : rgb(193, 174, 153);")
        self.room_nickname = QLabel(self.widget)
        self.room_nickname.setObjectName(u"room_nickname")
        self.room_nickname.setGeometry(QRect(20, 330, 111, 16))
        self.content = QStackedWidget(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setGeometry(QRect(160, 0, 701, 451))
        self.content.setStyleSheet(u"background-color: rgb(245, 250, 255);")
        self.page_0 = QWidget()
        self.page_0.setObjectName(u"page_0")
        self.page_0.setStyleSheet(u"background-color: rgb(240, 250, 255);\n"
"border-top-color: rgb(20, 20, 20);")
        self.groupBox = QGroupBox(self.page_0)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 581, 131))
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.platform_check_1 = QCheckBox(self.groupBox)
        self.platform_check_1.setObjectName(u"platform_check_1")
        self.platform_check_1.setGeometry(QRect(30, 20, 80, 30))
        self.platform_check_1.setStyleSheet(u"border : 1px solid rgb(70, 86, 99);\n"
"padding : 3px;")
        self.platform_check_2 = QCheckBox(self.groupBox)
        self.platform_check_2.setObjectName(u"platform_check_2")
        self.platform_check_2.setGeometry(QRect(120, 20, 80, 30))
        self.platform_check_2.setStyleSheet(u"border : 1px solid rgb(70, 86, 99);\n"
"padding : 3px;")
        self.url_address = QLineEdit(self.page_0)
        self.url_address.setObjectName(u"url_address")
        self.url_address.setGeometry(QRect(10, 160, 361, 31))
        self.url_address.setStyleSheet(u"border-width : 1px;\n"
"border-color : rgb(70, 86, 99);\n"
"border-style : solid;")
        self.url_save = QPushButton(self.page_0)
        self.url_save.setObjectName(u"url_save")
        self.url_save.setGeometry(QRect(390, 160, 71, 31))
        self.url_save.setStyleSheet(u"QPushButton#url_save {\n"
"    border : none;\n"
"	color:#000000;\n"
"	background-color: #ffc7a0;\n"
"	font: 9pt \"Microsoft YaHei\";\n"
"}\n"
"QPushButton#url_save:hover {\n"
"    border : none;\n"
"	color: #ffffff;\n"
"	background-color: #391461;\n"
"}")
        self.url_connect = QPushButton(self.page_0)
        self.url_connect.setObjectName(u"url_connect")
        self.url_connect.setGeometry(QRect(480, 160, 71, 31))
        self.url_connect.setStyleSheet(u"QPushButton#url_connect {\n"
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
        self.url_disconnect = QPushButton(self.page_0)
        self.url_disconnect.setObjectName(u"url_disconnect")
        self.url_disconnect.setGeometry(QRect(570, 160, 71, 31))
        self.url_disconnect.setStyleSheet(u"QPushButton#url_disconnect {\n"
"    border : none;\n"
"	color:#000000;\n"
"	background-color: #ffc7a0;\n"
"	font: 9pt \"Microsoft YaHei\";\n"
"}\n"
"QPushButton#url_disconnect:hover {\n"
"    border : none;\n"
"	color: #ffffff;\n"
"	background-color: #391461;\n"
"}\n"
"")
        self.groupBox_2 = QGroupBox(self.page_0)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 210, 681, 211))
        self.function_1 = QCheckBox(self.groupBox_2)
        self.function_1.setObjectName(u"function_1")
        self.function_1.setGeometry(QRect(30, 30, 101, 30))
        self.function_1.setStyleSheet(u"border : 1px solid rgb(70, 86, 99);\n"
"padding : 3px;")
        self.content.addWidget(self.page_0)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.label_2 = QLabel(self.page_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(400, 200, 52, 14))
        self.content.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"background-color: rgb(255, 255, 0);")
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 240, 52, 14))
        self.content.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(330, 290, 52, 14))
        self.content.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 850, 20))
        self.menubar.setStyleSheet(u"background-color: rgb(245, 250, 255);\n"
"border-bottom : 1px solid rgb(70, 86, 99);\n"
"")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu_2.addAction(self.action_help)
        self.menu_2.addAction(self.action_about)

        self.retranslateUi(MainWindow)

        self.content.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.action_help.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.left_menu_button_1.setText(QCoreApplication.translate("MainWindow", u"\u9996\u9875\u83dc\u5355", None))
        self.left_menu_button_2.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u7edf\u8ba1", None))
        self.left_menu_button_3.setText(QCoreApplication.translate("MainWindow", u"\u5386\u53f2\u6570\u636e", None))
        self.left_menu_button_4.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9\u4e2d\u5fc3", None))
        self.room_nickname.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u5e73\u53f0\u9009\u62e9", None))
        self.platform_check_1.setText(QCoreApplication.translate("MainWindow", u"\u6296\u97f3", None))
        self.platform_check_2.setText(QCoreApplication.translate("MainWindow", u"\u5feb\u624b", None))
        self.url_address.setText(QCoreApplication.translate("MainWindow", u"https://live.douyin.com/646454278948", None))
        self.url_address.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u76f4\u64ad\u95f4\u5730\u5740", None))
        self.url_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.url_connect.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5", None))
        self.url_disconnect.setText(QCoreApplication.translate("MainWindow", u"\u65ad\u5f00", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u4e3b\u64ad\u529f\u80fd", None))
        self.function_1.setText(QCoreApplication.translate("MainWindow", u"\u5f39\u5e55\u52a9\u624b", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"page1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"page2", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"page3", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

