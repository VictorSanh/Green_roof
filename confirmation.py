# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirmation.ui'
#
# Created: Tue Jan 19 16:47:32 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

import parametres_utilisateur
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

class Ui_Confirmation(object):
    def setupUi(self, Confirmation, adresseGoogleFormated, latlng):
        Confirmation.setObjectName(_fromUtf8("Confirmation"))
        Confirmation.setEnabled(True)
        Confirmation.resize(500, 300)
        Confirmation.setMinimumSize(QtCore.QSize(500, 300))
        Confirmation.setMaximumSize(QtCore.QSize(500, 300))
        self.monBackground = QtGui.QLabel(Confirmation)
        self.monBackground.setGeometry(QtCore.QRect(0, 0, 500, 300))
        self.monBackground.setMinimumSize(QtCore.QSize(500, 300))
        self.monBackground.setMaximumSize(QtCore.QSize(500, 300))
        self.monBackground.setText(_fromUtf8(""))
        self.monBackground.setPixmap(QtGui.QPixmap(_fromUtf8("Window/ressources/point_d_interrogation.png")))
        self.monBackground.setScaledContents(True)
        self.monBackground.setWordWrap(False)
        self.monBackground.setObjectName(_fromUtf8("monBackground"))
        
        self.bonneAdresse = QtGui.QPushButton(Confirmation)
        self.bonneAdresse.setGeometry(QtCore.QRect(10, 240, 211, 51))
        self.bonneAdresse.setStyleSheet(_fromUtf8("background-color:rgb(51,255,51);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Calibri\";\n"
"border-top-color: rgb(121, 255, 229);\n"
"border-radius: 10px;"))
        self.bonneAdresse.setObjectName(_fromUtf8("bonneAdresse"))
        self.bonneAdresse.clicked.connect(Confirmation.close)
        self.bonneAdresse.clicked.connect(lambda: self.paramUtilisateur(latlng))
        
        self.preciserAdresse = QtGui.QPushButton(Confirmation)
        self.preciserAdresse.setGeometry(QtCore.QRect(290, 240, 201, 51))
        self.preciserAdresse.setStyleSheet(_fromUtf8("background-color:rgb(51,255,51);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Calibri\";\n"
"border-top-color: rgb(121, 255, 229);\n"
"border-radius: 10px;"))
        self.preciserAdresse.setObjectName(_fromUtf8("preciserAdresse"))
        self.preciserAdresse.clicked.connect(Confirmation.close)        
        
        self.printAdresse = QtGui.QTextEdit(Confirmation)
        self.printAdresse.setEnabled(False)
        self.printAdresse.setGeometry(QtCore.QRect(50, 20, 400, 200))
        self.printAdresse.setStyleSheet(_fromUtf8("background-color:rgba(51,255,51,1);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Calibri\";\n"
""))
        self.printAdresse.setReadOnly(True)
        self.printAdresse.setObjectName(_fromUtf8("printAdresse"))

        self.retranslateUi(Confirmation, adresseGoogleFormated)
        QtCore.QMetaObject.connectSlotsByName(Confirmation)

    def retranslateUi(self, Confirmation, adresseGoogleFormated):
        Confirmation.setWindowTitle(_translate("Confirmation", "Dialog", None))
        self.bonneAdresse.setText(_translate("Confirmation", "C\'est la bonne adresse !", None))
        self.preciserAdresse.setText(_translate("Confirmation", "Préciser mon adresse...", None))
        self.printAdresse.setText(_translate("Confirmation", adresseGoogleFormated, None))
        
    def paramUtilisateur(self, latlng):        
        paramWindow = QtGui.QDialog()
        ui = parametres_utilisateur.Ui_Param()
        ui.setupUi(paramWindow, latlng)
        paramWindow.exec_() 

#if __name__ == "__main__":
#    import sys
#    app = QtGui.QApplication(sys.argv)
#    Confirmation = QtGui.QDialog()
#    ui = Ui_Confirmation()
#    ui.setupUi(Confirmation,"Ceci est un test.")
#    Confirmation.show()
#    sys.exit(app.exec_())

