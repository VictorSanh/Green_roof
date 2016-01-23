# -*- coding: utf-8 -*-

#Fenêtre final affuchant le résultat
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

class Ui_Result(object):
    def setupUi(self, ResultWindow, Res):
        ResultWindow.setObjectName(_fromUtf8("ResultWindow"))
        ResultWindow.resize(824, 500)
        ResultWindow.setMouseTracking(True)
        self.printResult = QtGui.QTextEdit(ResultWindow)
        self.printResult.setEnabled(False)
        self.printResult.setGeometry(QtCore.QRect(150, 150, 600, 200))
        self.printResult.setStyleSheet(_fromUtf8("background-color:rgba(81,255,51,1);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 20pt \"Calibri\";\n"
""))
        self.printResult.setReadOnly(True)
        self.printResult.setObjectName(_fromUtf8("printResult"))

        self.retranslateUi(ResultWindow, 235)
        QtCore.QMetaObject.connectSlotsByName(ResultWindow)

    def retranslateUi(self, ResultWindow, Res):
        ResultWindow.setWindowTitle(_translate("ResultWindow", "Résultats", None))        
        self.printResult.setText(_translate("ResultWindow", "La consommation \
énergétique totale de votre domicile est {} kWh. Cela correspond à \
une dépense de l'ordre de {} Euros.".format(Res, round(Res*0.15030)), None))
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ResultWindow = QtGui.QDialog()
    ui = Ui_Result()
    ui.setupUi(ResultWindow, "")
    ResultWindow.show()
    sys.exit(app.exec_())
