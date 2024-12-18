# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'danmu.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QFrame, QSizePolicy, QWidget)

class Ui_DanmuWin(object):
    def setupUi(self, DanmuWin):
        if not DanmuWin.objectName():
            DanmuWin.setObjectName(u"DanmuWin")
        DanmuWin.resize(300, 600)
        DanmuWin.setStyleSheet(u"")
        self.frame = QFrame(DanmuWin)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 301, 601))
        self.frame.setStyleSheet(u"background-color: rgba(70, 86, 99, 0.3);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.webEngineView = QWebEngineView(self.frame)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setGeometry(QRect(0, 0, 301, 601))
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.retranslateUi(DanmuWin)

        QMetaObject.connectSlotsByName(DanmuWin)
    # setupUi

    def retranslateUi(self, DanmuWin):
        DanmuWin.setWindowTitle(QCoreApplication.translate("DanmuWin", u"\u5f39\u5e55\u52a9\u624b", None))
    # retranslateUi

