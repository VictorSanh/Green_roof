# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Sun Jan 17 22:43:30 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

import geolocalisation
import confirmation
import fenetreErreur
from PyQt4 import QtCore, QtGui
from urllib.error import URLError, HTTPError

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
        self.monBackground.setPixmap(QtGui.QPixmap(_fromUtf8("Window/ressources/Image_Background_Green_Roof.jpg")))
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
        self.monAdresse.returnPressed.connect(lambda: self.requete())
        
        
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(780, 460, 111, 51))
        self.pushButton.setStyleSheet(_fromUtf8("background-color:rgb(51,255,51);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"Calibri\";\n"
"border-top-color: rgb(121, 255, 229);\n"
"border-radius: 10px;"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(lambda: self.requete())        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFichier = QtGui.QMenu(self.menubar)
        self.menuFichier.setObjectName(_fromUtf8("menuFichier"))
        self.menuA_propos = QtGui.QMenu(self.menubar)
        self.menuA_propos.setObjectName(_fromUtf8("menuA_propos"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuA_propos.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.monAdresse, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.monAdresse.copy)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton, self.monAdresse)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.monAdresse.setPlaceholderText(_translate("MainWindow", "Entrez votre adresse complète...", None))
        self.pushButton.setText(_translate("MainWindow", "Calcul", None))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier", None))
        self.menuA_propos.setTitle(_translate("MainWindow", "A propos", None))

    def requete(self):
        adresse_rentree=str(self.monAdresse.text())
        
        try:
            Fichier = geolocalisation.geocode(adresse_rentree)
            pos = geolocalisation.trouve_en_france(Fichier)        
            adresseGoogleFormated = geolocalisation.addresse_formatee(Fichier, pos)
        except geolocalisation.ZeroResult:
            #Aucun résultat trouvé par Google Maps, l'adresse semble être incorrecte
            erreurWindow = QtGui.QDialog()
            uierreur = fenetreErreur.Ui_fenetreErreur()
            uierreur.setupUi(erreurWindow, "Adresse non trouvée. Revoir l'adresse.")
            erreurWindow.exec_()
        except geolocalisation.ZeroResultFrance:
            #Aucun résultat trouvé en France
            erreurWindow = QtGui.QDialog()
            uierreur = fenetreErreur.Ui_fenetreErreur()
            uierreur.setupUi(erreurWindow, "Pas d'adresse trouvée en France. Revoir l'adresse.")
            erreurWindow.exec_()
        except HTTPError:
            #Adresse internet non trouvée
            erreurWindow = QtGui.QDialog()
            uierreur = fenetreErreur.Ui_fenetreErreur()
            uierreur.setupUi(erreurWindow, "Adresse internet non trouvée")
            erreurWindow.exec_()
        except URLError:
            #Pas de connexion internet
            erreurWindow = QtGui.QDialog()
            uierreur = fenetreErreur.Ui_fenetreErreur()
            uierreur.setupUi(erreurWindow, "Pas de connexion internet")
            erreurWindow.exec_()
        except:
            erreurWindow = QtGui.QDialog()
            uierreur = fenetreErreur.Ui_fenetreErreur()
            uierreur.setupUi(erreurWindow, "Erreur inconnue")
            erreurWindow.exec_()        
        else:
            latlng = geolocalisation.lat_lng(Fichier, pos)
        
            ConfirmationWindow = QtGui.QDialog()
            ui = confirmation.Ui_Confirmation()
            ui.setupUi(ConfirmationWindow, adresseGoogleFormated, latlng)
            ConfirmationWindow.exec_() 


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

