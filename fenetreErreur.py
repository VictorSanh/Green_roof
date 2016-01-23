# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fenetreErreur.ui'
#
# Created: Sat Jan 23 15:00:49 2016
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

class Ui_fenetreErreur(object):
    def setupUi(self, fenetreErreur, nomErreur):
        fenetreErreur.setObjectName(_fromUtf8("fenetreErreur"))
        fenetreErreur.setEnabled(True)
        fenetreErreur.resize(500, 500)
        fenetreErreur.setMinimumSize(QtCore.QSize(500, 500))
        fenetreErreur.setMaximumSize(QtCore.QSize(500, 500))
        self.monBackground = QtGui.QLabel(fenetreErreur)
        self.monBackground.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.monBackground.setMinimumSize(QtCore.QSize(500, 500))
        self.monBackground.setMaximumSize(QtCore.QSize(500, 500))
        self.monBackground.setText(_fromUtf8(""))
        self.monBackground.setPixmap(QtGui.QPixmap(_fromUtf8("Erreur.jpg")))
        self.monBackground.setScaledContents(True)
        self.monBackground.setWordWrap(False)
        self.monBackground.setObjectName(_fromUtf8("monBackground"))
        
        self.jeVaisVoirCela = QtGui.QPushButton(fenetreErreur)
        self.jeVaisVoirCela.setGeometry(QtCore.QRect(150, 420, 221, 41))
        self.jeVaisVoirCela.setStyleSheet(_fromUtf8("background-color:rgb(51,255,51);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Calibri\";\n"
"border-top-color: rgb(121, 255, 229);\n"
"border-radius: 10px;"))
        self.jeVaisVoirCela.clicked.connect(fenetreErreur.close)
        self.jeVaisVoirCela.setObjectName(_fromUtf8("jeVaisVoirCela"))
        
        self.printErreur = QtGui.QTextEdit(fenetreErreur)
        self.printErreur.setEnabled(False)
        self.printErreur.setGeometry(QtCore.QRect(80, 50, 361, 231))
        self.printErreur.setStyleSheet(_fromUtf8("background-color:rgba(51,255,51,0);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 30pt \"Calibri\";\n"
""))
        self.printErreur.setReadOnly(True)
        self.printErreur.setObjectName(_fromUtf8("printErreur"))

        self.retranslateUi(fenetreErreur, nomErreur)
        QtCore.QMetaObject.connectSlotsByName(fenetreErreur)

    def retranslateUi(self, fenetreErreur, nomErreur):
        fenetreErreur.setWindowTitle(_translate("fenetreErreur", "Dialog", None))
        self.jeVaisVoirCela.setText(_translate("fenetreErreur", "OK, je vais voir cela !", None))
        self.printErreur.setText(_translate("fenetreErreur", nomErreur, None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    fenetreErreur = QtGui.QDialog()
    ui = Ui_fenetreErreur()
    ui.setupUi(fenetreErreur, "fds")
    fenetreErreur.show()
    sys.exit(app.exec_())

