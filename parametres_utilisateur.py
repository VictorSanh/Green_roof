# -*- coding: utf-8 -*-

#Programme générant fenêtre graphique pour récupérer les données utilisateurs

from Roof_model import weather_data
from Roof_model import Environnement, GreenRoof
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

class Ui_Param(object):
    def setupUi(self, ParamWindow, latlng):
        ParamWindow.setObjectName(_fromUtf8("ParamWindow"))
        ParamWindow.resize(824, 500)
        ParamWindow.setMouseTracking(True)
        
        self.latlng = latlng
        
        self.monBackground = QtGui.QLabel(ParamWindow)
        self.monBackground.setGeometry(QtCore.QRect(0, 0, 824, 500))
        self.monBackground.setMinimumSize(QtCore.QSize(824, 500))
        self.monBackground.setMaximumSize(QtCore.QSize(824, 500))
#        self.monBackground.setText(_fromUtf8(""))
        self.monBackground.setPixmap(QtGui.QPixmap(_fromUtf8("donnees.jpg")))
        self.monBackground.setScaledContents(True)
        self.monBackground.setWordWrap(False)
        self.monBackground.setObjectName(_fromUtf8("monBackground"))

        self.pushButton = QtGui.QPushButton(ParamWindow)
        self.pushButton.setGeometry(QtCore.QRect(430, 400, 121, 51))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 204);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"Calibri\";\n"
"border-top-color: rgb(121, 255, 229);\n"
"border-radius: 10px;"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        
        
        
        self.temp_int = QtGui.QPushButton(ParamWindow)
        self.temp_int.setGeometry(QtCore.QRect(60, 10, 540, 51))
        self.temp_int.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 204);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"Calibri\";\n"
"border-top-color: rgb(121, 255, 229);\n"
"border-radius: 10px;"))
        self.temp_int.setObjectName(_fromUtf8("temp_int"))  
        
        
        self.hauteur = QtGui.QPushButton(ParamWindow)
        self.hauteur.setGeometry(QtCore.QRect(60, 70, 400, 51))
        self.hauteur.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 204);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"Calibri\";\n"
"border-top-color: rgb(121, 255, 229);\n"
"border-radius: 10px;"))
        self.hauteur.setObjectName(_fromUtf8("hauteur"))
        
        
        self.mois = QtGui.QPushButton(ParamWindow)
        self.mois.setGeometry(QtCore.QRect(60, 130, 110, 51))
        self.mois.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 204);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"Calibri\";\n"
"border-top-color: rgb(121, 255, 229);\n"
"border-radius: 10px;"))
        self.mois.setObjectName(_fromUtf8("mois"))
        
        
        self.epaiss_toit = QtGui.QPushButton(ParamWindow)
        self.epaiss_toit.setGeometry(QtCore.QRect(60, 190, 425, 51))
        self.epaiss_toit.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 204);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"Calibri\";\n"
"border-top-color: rgb(121, 255, 229);\n"
"border-radius: 10px;"))
        self.epaiss_toit.setObjectName(_fromUtf8("epaiss_toit"))
        
        
        self.touffu = QtGui.QPushButton(ParamWindow)
        self.touffu.setGeometry(QtCore.QRect(60, 250, 200, 51))
        self.touffu.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 204);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"Calibri\";\n"
"border-top-color: rgb(121, 255, 229);\n"
"border-radius: 10px;"))
        self.touffu.setObjectName(_fromUtf8("touffu"))
        
        
        self.surface = QtGui.QPushButton(ParamWindow)
        self.surface.setGeometry(QtCore.QRect(60, 310, 250, 51))
        self.surface.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 204);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"Calibri\";\n"
"border-top-color: rgb(121, 255, 229);\n"
"border-radius: 10px;"))
        self.surface.setObjectName(_fromUtf8("surface"))
        
        
        self.comboBox_mois = QtGui.QComboBox(ParamWindow)
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
        
        
        self.comboBox_touffu = QtGui.QComboBox(ParamWindow)
        self.comboBox_touffu.setGeometry(QtCore.QRect(610, 250, 141, 51))
        self.comboBox_touffu.setObjectName(_fromUtf8("comboBox_touffu"))
        self.comboBox_touffu.addItem(_fromUtf8(""))
        self.comboBox_touffu.addItem(_fromUtf8(""))
        self.comboBox_touffu.addItem(_fromUtf8(""))
        self.comboBox_touffu.addItem(_fromUtf8(""))
        self.comboBox_touffu.addItem(_fromUtf8(""))
        
        
        self.doubleSpinBox_temp = QtGui.QDoubleSpinBox(ParamWindow)
        self.doubleSpinBox_temp.setGeometry(QtCore.QRect(610, 10, 141, 51))
        self.doubleSpinBox_temp.setMaximum(30)
        self.doubleSpinBox_temp.setStyleSheet(_fromUtf8("background-color: rgb(161, 161, 161);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 24pt \"MS Shell Dlg 2\";\n"
"border-radius: 20px;"))
        self.doubleSpinBox_temp.setObjectName(_fromUtf8("doubleSpinBox_temp"))
        
        
        self.doubleSpinBox_haut = QtGui.QDoubleSpinBox(ParamWindow)
        self.doubleSpinBox_haut.setGeometry(QtCore.QRect(610, 70, 141, 51))
        self.doubleSpinBox_haut.setMaximum(10)
        self.doubleSpinBox_haut.setStyleSheet(_fromUtf8("background-color: rgb(161, 161, 161);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 24pt \"MS Shell Dlg 2\";\n"
"border-radius: 20px;"))
        self.doubleSpinBox_haut.setObjectName(_fromUtf8("doubleSpinBox_haut"))
        
        
        self.doubleSpinBox_epaiss = QtGui.QDoubleSpinBox(ParamWindow)
        self.doubleSpinBox_epaiss.setGeometry(QtCore.QRect(610, 190, 161, 51))
        self.doubleSpinBox_epaiss.setMaximum(150)
        self.doubleSpinBox_epaiss.setStyleSheet(_fromUtf8("background-color: rgb(161, 161, 161);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 24pt \"MS Shell Dlg 2\";\n"
"border-radius: 20px;"))
        self.doubleSpinBox_epaiss.setObjectName(_fromUtf8("doubleSpinBox_epaiss"))
        
        
        self.doubleSpinBox_surf = QtGui.QDoubleSpinBox(ParamWindow)
        self.doubleSpinBox_surf.setGeometry(QtCore.QRect(610, 310, 161, 51))
        self.doubleSpinBox_surf.setMaximum(1000)
        self.doubleSpinBox_surf.setStyleSheet(_fromUtf8("background-color: rgb(161, 161, 161);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 24pt \"MS Shell Dlg 2\";\n"
"border-radius: 20px;"))
        self.doubleSpinBox_surf.setObjectName(_fromUtf8("doubleSpinBox_surf"))

        self.retranslateUi(ParamWindow)
        QtCore.QMetaObject.connectSlotsByName(ParamWindow)

    def retranslateUi(self, ParamWindow):
        ParamWindow.setWindowTitle(_translate("ParamWindow", "ParamWindow", None))
        self.pushButton.setText(_translate("ParamWindow", "Calcul", None))
        
        
        self.temp_int.setText(_translate("ParamWindow", "Température intérieure (°C)", None))
        self.hauteur.setText(_translate("ParamWindow", "Hauteur du toit (m)", None))
        self.mois.setText(_translate("ParamWindow", "Mois", None))
        self.epaiss_toit.setText(_translate("ParamWindow", "Epaisseur du toit (cm)", None))
        self.touffu.setText(_translate("ParamWindow", "Hirsuitude", None))
        self.surface.setText(_translate("ParamWindow", "Surface (m²)", None))
        
        
        self.comboBox_mois.setItemText(0, _translate("ParamWindow", "Janvier", None))
        self.comboBox_mois.setItemText(1, _translate("ParamWindow", "Février", None))
        self.comboBox_mois.setItemText(2, _translate("ParamWindow", "Mars", None))
        self.comboBox_mois.setItemText(3, _translate("ParamWindow", "Avril", None))
        self.comboBox_mois.setItemText(4, _translate("ParamWindow", "Mai", None))
        self.comboBox_mois.setItemText(5, _translate("ParamWindow", "Juin", None))
        self.comboBox_mois.setItemText(6, _translate("ParamWindow", "Juillet", None))
        self.comboBox_mois.setItemText(7, _translate("ParamWindow", "Août", None))
        self.comboBox_mois.setItemText(8, _translate("ParamWindow", "Septembre", None))
        self.comboBox_mois.setItemText(9, _translate("ParamWindow", "Octobre", None))
        self.comboBox_mois.setItemText(10, _translate("ParamWindow", "Novembre", None))
        self.comboBox_mois.setItemText(11, _translate("ParamWindow", "Décembre", None))
        
        
        self.comboBox_touffu.setItemText(0, _translate("ParamWindow", "Très peu touffu", None))
        self.comboBox_touffu.setItemText(1, _translate("ParamWindow", "Peu touffu", None))
        self.comboBox_touffu.setItemText(2, _translate("ParamWindow", "Moyen moyen", None))
        self.comboBox_touffu.setItemText(3, _translate("ParamWindow", "Pas mal", None))
        self.comboBox_touffu.setItemText(4, _translate("ParamWindow", "Très Touffu", None))
        
    def requete(self):
        temp_rentree = float(self.temp_int.text()) + 273
        hauteur_rentree = float(self.hauteur.text())
        mois_rentree = int(convert_mois(self.mois.text()))
        epaiss_rentree = float(self.epaiss_toit.text()*10)
        touffu_rentree = int(convert_touffu(self.touffu.text()))
        surface_rentree = float(self.surface.text())
        print("coucou")
        env = Environnement(self.latlng['lng'], self.latlng['lat'], mois_rentree, 15)
        roof = GreenRoof(2/3*epaiss_rentree, 1/3*epaiss_rentree, 0.05, touffu_rentree, temp_rentree)      
        print(roof.calcule_diff_finies_lentes(env))
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ParamWindow = QtGui.QDialog()
    ui = Ui_Param()
    ui.setupUi(ParamWindow, "")
    ParamWindow.show()
    sys.exit(app.exec_())
