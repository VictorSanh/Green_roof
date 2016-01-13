# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Wed Jan 13 00:06:09 2016
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
        MainWindow.resize(800, 637)
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet(_fromUtf8("background-image : url(Image_Background_Green_Roof.jpg);\n"
"background-repeat: no-repeat;"))
        MainWindow.setDocumentMode(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(670, 530, 111, 51))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"Calibri\";\n"
"border-top-color: rgb(121, 255, 229);\n"
"border-radius: 10px;"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(630, 50, 141, 51))
        self.doubleSpinBox.setStyleSheet(_fromUtf8("background-color: rgb(161, 161, 161);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 24pt \"MS Shell Dlg 2\";\n"
"border-radius: 20px;"))
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(380, 40, 411, 61))
        self.textEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"Calibri\";\n"
"border-top-color: rgb(121, 255, 229);\n"
"border-radius: 30px;\n"
""))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(630, 230, 141, 51))
        self.doubleSpinBox_2.setStyleSheet(_fromUtf8("background-color: rgb(161, 161, 161);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 24pt \"MS Shell Dlg 2\";\n"
"border-radius: 20px;"))
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(380, 220, 401, 61))
        self.textEdit_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"Calibri\";\n"
"border-top-color: rgb(121, 255, 229);\n"
"border-radius: 30px;\n"
""))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.textEdit_3 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(380, 130, 411, 61))
        self.textEdit_3.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"Calibri\";\n"
"border-top-color: rgb(121, 255, 229);\n"
"border-radius: 30px;\n"
""))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.doubleSpinBox_3 = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(630, 140, 141, 51))
        self.doubleSpinBox_3.setStyleSheet(_fromUtf8("background-color: rgb(161, 161, 161);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 24pt \"MS Shell Dlg 2\";\n"
"border-radius: 20px;"))
        self.doubleSpinBox_3.setObjectName(_fromUtf8("doubleSpinBox_3"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 360, 671, 111))
        self.lineEdit.setMouseTracking(False)
        self.lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Calibri\";\n"
"border-top-color: rgb(121, 255, 229);\n"
"border-radius: 30px;"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFds = QtGui.QMenu(self.menubar)
        self.menuFds.setObjectName(_fromUtf8("menuFds"))
        self.menuEdition = QtGui.QMenu(self.menubar)
        self.menuEdition.setObjectName(_fromUtf8("menuEdition"))
        self.menuA_propos = QtGui.QMenu(self.menubar)
        self.menuA_propos.setObjectName(_fromUtf8("menuA_propos"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionFichier = QtGui.QAction(MainWindow)
        self.actionFichier.setObjectName(_fromUtf8("actionFichier"))
        self.actionNouveau = QtGui.QAction(MainWindow)
        self.actionNouveau.setObjectName(_fromUtf8("actionNouveau"))
        self.menuFds.addAction(self.actionNouveau)
        self.menubar.addAction(self.menuFds.menuAction())
        self.menubar.addAction(self.menuEdition.menuAction())
        self.menubar.addAction(self.menuA_propos.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Calcul", None))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri\'; font-size:28pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> Données n°1</p></body></html>", None))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri\'; font-size:28pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> Données n°3</p></body></html>", None))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri\'; font-size:28pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> Données n°2</p></body></html>", None))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Entrez votre adresse...", None))
        self.menuFds.setTitle(_translate("MainWindow", "Fichier", None))
        self.menuEdition.setTitle(_translate("MainWindow", "Edition", None))
        self.menuA_propos.setTitle(_translate("MainWindow", "A propos", None))
        self.actionFichier.setText(_translate("MainWindow", "Fichier", None))
        self.actionNouveau.setText(_translate("MainWindow", "Nouveau", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

