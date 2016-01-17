# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Sun Jan 17 22:43:30 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QtCore.QSize(900, 600))
        MainWindow.setMaximumSize(QtCore.QSize(900, 600))
        MainWindow.setStyleSheet(_fromUtf8("backgound-color:green;\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.monBackground = QtGui.QLabel(self.centralwidget)
        self.monBackground.setGeometry(QtCore.QRect(0, 0, 901, 551))
        self.monBackground.setText(_fromUtf8(""))
        self.monBackground.setPixmap(QtGui.QPixmap(_fromUtf8("Image_Background_Green_Roof.jpg")))
        self.monBackground.setScaledContents(True)
        self.monBackground.setWordWrap(False)
        self.monBackground.setObjectName(_fromUtf8("monBackground"))
        self.monAdresse = QtGui.QLineEdit(self.centralwidget)
        self.monAdresse.setGeometry(QtCore.QRect(90, 440, 671, 91))
        self.monAdresse.setMaximumSize(QtCore.QSize(700, 200))
        self.monAdresse.setMouseTracking(True)
        self.monAdresse.setStyleSheet(_fromUtf8("background-color:rgb(51,255,51);\n"
"color: white;\n"
"font: 75 28pt \"Calibri\";\n"
"border-top-color: rgb(121, 255, 229);\n"
"border-radius: 30px;"))
        self.monAdresse.setEchoMode(QtGui.QLineEdit.Normal)
        self.monAdresse.setReadOnly(False)
        self.monAdresse.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.monAdresse.setObjectName(_fromUtf8("monAdresse"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(780, 460, 111, 51))
        self.pushButton.setStyleSheet(_fromUtf8("background-color:rgb(51,255,51);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"Calibri\";\n"
"border-top-color: rgb(121, 255, 229);\n"
"border-radius: 10px;"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFIchier = QtGui.QMenu(self.menubar)
        self.menuFIchier.setObjectName(_fromUtf8("menuFIchier"))
        self.menuA_propos = QtGui.QMenu(self.menubar)
        self.menuA_propos.setObjectName(_fromUtf8("menuA_propos"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFIchier.menuAction())
        self.menubar.addAction(self.menuA_propos.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.monAdresse, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.monAdresse.copy)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton, self.monAdresse)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.monAdresse.setPlaceholderText(_translate("MainWindow", "Entrez votre adresse complète...", None))
        self.pushButton.setText(_translate("MainWindow", "Calcul", None))
        self.menuFIchier.setTitle(_translate("MainWindow", "FIchier", None))
        self.menuA_propos.setTitle(_translate("MainWindow", "A propos", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

