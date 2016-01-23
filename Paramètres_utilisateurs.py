# -*- coding: utf-8 -*-

#Programme générant fenêtre graphique pour récupérer les données utilisateurs

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

def convert_mois(mois):
    switcher = {
        "Janvier": 1,
        "Février": 2,
        "Mars": 3,
        "Avril": 4,
        "Mai": 5,
        "Juin": 6,
        "Juillet": 7,
        "Août": 8,
        "Septembre": 9,
        "Octobre": 10,
        "Novembre": 11,
        "Décembre": 12,
    }
    return switcher.get(mois)
        
def convert_touffu(hirsuitude):
    switcher = {
        "Très peu touffu": 1,
        "Peu touffu": 2,
        "Moyen moyen": 3,
        "Pas mal": 4,
        "Très touffu": 5,
    }
    return switcher.get(hirsuitude)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(824, 500)
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet(_fromUtf8("background-image : url(Image_Background_Green_Roof.jpg);\n"
"background-repeat: no-repeat;\n"
"background-size: cover;\n"
""))
        MainWindow.setDocumentMode(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 400, 121, 51))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"Calibri\";\n"
"border-top-color: rgb(121, 255, 229);\n"
"border-radius: 10px;"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        
        
        
        self.temp_int = QtGui.QPushButton(self.centralwidget)
        self.temp_int.setGeometry(QtCore.QRect(60, 10, 540, 51))
        self.temp_int.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"Calibri\";\n"
"border-top-color: rgb(121, 255, 229);\n"
"border-radius: 10px;"))
        self.temp_int.setObjectName(_fromUtf8("temp_int"))  
        
        
        self.hauteur = QtGui.QPushButton(self.centralwidget)
        self.hauteur.setGeometry(QtCore.QRect(60, 70, 400, 51))
        self.hauteur.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"Calibri\";\n"
"border-top-color: rgb(121, 255, 229);\n"
"border-radius: 10px;"))
        self.hauteur.setObjectName(_fromUtf8("hauteur"))
        
        
        self.mois = QtGui.QPushButton(self.centralwidget)
        self.mois.setGeometry(QtCore.QRect(60, 130, 110, 51))
        self.mois.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"Calibri\";\n"
"border-top-color: rgb(121, 255, 229);\n"
"border-radius: 10px;"))
        self.mois.setObjectName(_fromUtf8("mois"))
        
        
        self.epaiss_toit = QtGui.QPushButton(self.centralwidget)
        self.epaiss_toit.setGeometry(QtCore.QRect(60, 190, 425, 51))
        self.epaiss_toit.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"Calibri\";\n"
"border-top-color: rgb(121, 255, 229);\n"
"border-radius: 10px;"))
        self.epaiss_toit.setObjectName(_fromUtf8("epaiss_toit"))
        
        
        self.touffu = QtGui.QPushButton(self.centralwidget)
        self.touffu.setGeometry(QtCore.QRect(60, 250, 200, 51))
        self.touffu.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"Calibri\";\n"
"border-top-color: rgb(121, 255, 229);\n"
"border-radius: 10px;"))
        self.touffu.setObjectName(_fromUtf8("touffu"))
        
        
        self.surface = QtGui.QPushButton(self.centralwidget)
        self.surface.setGeometry(QtCore.QRect(60, 310, 250, 51))
        self.surface.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"Calibri\";\n"
"border-top-color: rgb(121, 255, 229);\n"
"border-radius: 10px;"))
        self.surface.setObjectName(_fromUtf8("surface"))
        
        
        self.comboBox_mois = QtGui.QComboBox(self.centralwidget)
        self.comboBox_mois.setGeometry(QtCore.QRect(610, 130, 141, 51))
        self.comboBox_mois.setObjectName(_fromUtf8("comboBox_mois"))
        self.comboBox_mois.addItem(_fromUtf8(""))
        self.comboBox_mois.addItem(_fromUtf8(""))
        self.comboBox_mois.addItem(_fromUtf8(""))
        self.comboBox_mois.addItem(_fromUtf8(""))
        self.comboBox_mois.addItem(_fromUtf8(""))
        self.comboBox_mois.addItem(_fromUtf8(""))
        self.comboBox_mois.addItem(_fromUtf8(""))
        self.comboBox_mois.addItem(_fromUtf8(""))
        self.comboBox_mois.addItem(_fromUtf8(""))
        self.comboBox_mois.addItem(_fromUtf8(""))
        self.comboBox_mois.addItem(_fromUtf8(""))
        self.comboBox_mois.addItem(_fromUtf8(""))
        
        
        self.comboBox_touffu = QtGui.QComboBox(self.centralwidget)
        self.comboBox_touffu.setGeometry(QtCore.QRect(610, 250, 141, 51))
        self.comboBox_touffu.setObjectName(_fromUtf8("comboBox_touffu"))
        self.comboBox_touffu.addItem(_fromUtf8(""))
        self.comboBox_touffu.addItem(_fromUtf8(""))
        self.comboBox_touffu.addItem(_fromUtf8(""))
        self.comboBox_touffu.addItem(_fromUtf8(""))
        self.comboBox_touffu.addItem(_fromUtf8(""))
        
        
        self.doubleSpinBox_temp = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_temp.setGeometry(QtCore.QRect(610, 10, 141, 51))
        self.doubleSpinBox_temp.setMaximum(30)
        self.doubleSpinBox_temp.setStyleSheet(_fromUtf8("background-color: rgb(161, 161, 161);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 24pt \"MS Shell Dlg 2\";\n"
"border-radius: 20px;"))
        self.doubleSpinBox_temp.setObjectName(_fromUtf8("doubleSpinBox_temp"))
        
        
        self.doubleSpinBox_haut = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_haut.setGeometry(QtCore.QRect(610, 70, 141, 51))
        self.doubleSpinBox_haut.setMaximum(10)
        self.doubleSpinBox_haut.setStyleSheet(_fromUtf8("background-color: rgb(161, 161, 161);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 24pt \"MS Shell Dlg 2\";\n"
"border-radius: 20px;"))
        self.doubleSpinBox_haut.setObjectName(_fromUtf8("doubleSpinBox_haut"))
        
        
        self.doubleSpinBox_epaiss = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_epaiss.setGeometry(QtCore.QRect(610, 190, 161, 51))
        self.doubleSpinBox_epaiss.setMaximum(150)
        self.doubleSpinBox_epaiss.setStyleSheet(_fromUtf8("background-color: rgb(161, 161, 161);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 24pt \"MS Shell Dlg 2\";\n"
"border-radius: 20px;"))
        self.doubleSpinBox_epaiss.setObjectName(_fromUtf8("doubleSpinBox_epaiss"))
        
        
        self.doubleSpinBox_surf = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_surf.setGeometry(QtCore.QRect(610, 310, 161, 51))
        self.doubleSpinBox_surf.setMaximum(1000)
        self.doubleSpinBox_surf.setStyleSheet(_fromUtf8("background-color: rgb(161, 161, 161);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 24pt \"MS Shell Dlg 2\";\n"
"border-radius: 20px;"))
        self.doubleSpinBox_surf.setObjectName(_fromUtf8("doubleSpinBox_surf"))
        

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 824, 21))
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
        
        
        self.temp_int.setText(_translate("MainWindow", "Température intérieure (°C)", None))
        self.hauteur.setText(_translate("MainWindow", "Hauteur du toit (m)", None))
        self.mois.setText(_translate("MainWindow", "Mois", None))
        self.epaiss_toit.setText(_translate("MainWindow", "Epaisseur du toit (cm)", None))
        self.touffu.setText(_translate("MainWindow", "Hirsuitude", None))
        self.surface.setText(_translate("MainWindow", "Surface (m²)", None))
        
        
        self.comboBox_mois.setItemText(0, _translate("MainWondow", "Janvier", None))
        self.comboBox_mois.setItemText(1, _translate("MainWondow", "Février", None))
        self.comboBox_mois.setItemText(2, _translate("MainWondow", "Mars", None))
        self.comboBox_mois.setItemText(3, _translate("MainWondow", "Avril", None))
        self.comboBox_mois.setItemText(4, _translate("MainWondow", "Mai", None))
        self.comboBox_mois.setItemText(5, _translate("MainWondow", "Juin", None))
        self.comboBox_mois.setItemText(6, _translate("MainWondow", "Juillet", None))
        self.comboBox_mois.setItemText(7, _translate("MainWondow", "Août", None))
        self.comboBox_mois.setItemText(8, _translate("MainWondow", "Septembre", None))
        self.comboBox_mois.setItemText(9, _translate("MainWondow", "Octobre", None))
        self.comboBox_mois.setItemText(10, _translate("MainWondow", "Novembre", None))
        self.comboBox_mois.setItemText(11, _translate("MainWondow", "Décembre", None))
        
        
        self.comboBox_touffu.setItemText(0, _translate("MainWondow", "Très peu touffu", None))
        self.comboBox_touffu.setItemText(1, _translate("MainWondow", "Peu touffu", None))
        self.comboBox_touffu.setItemText(2, _translate("MainWondow", "Moyen moyen", None))
        self.comboBox_touffu.setItemText(3, _translate("MainWondow", "Pas mal", None))
        self.comboBox_touffu.setItemText(4, _translate("MainWondow", "Très Touffu", None))
        
        
        self.menuFds.setTitle(_translate("MainWindow", "Fichier", None))
        self.menuEdition.setTitle(_translate("MainWindow", "Edition", None))
        self.menuA_propos.setTitle(_translate("MainWindow", "A propos", None))
        self.actionFichier.setText(_translate("MainWindow", "Fichier", None))
        self.actionNouveau.setText(_translate("MainWindow", "Nouveau", None))
        
    def requete(self):
        self.temp_rentree = float(self.temp_int.text()) + 273
        self.hauteur_rentree = float(self.hauteur.text())
        self.mois_rentree = int(convert_mois(self.mois.text()))
        self.epaiss_rentree = float(self.epaiss_toit.text()*10)
        self.touffu_rentree = int(convert_touffu(self.touffu.text()))
        self.surface_rentree = float(self.surface.text())


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
