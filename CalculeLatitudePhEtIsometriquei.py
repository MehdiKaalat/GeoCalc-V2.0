from PyQt5 import QtCore, QtGui, QtWidgets
from math import *

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
import fonctions as fct

class fonction2(object):
    def pagePr(self):
        from pageprincipale import pagePrincipale
        self.window1 = QtWidgets.QMainWindow()
        self.ui = pagePrincipale()
        self.ui.setupUi(self.window1)
        self.window1.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(711, 755)
        MainWindow.setMinimumSize(QtCore.QSize(711, 755))
        MainWindow.setMaximumSize(QtCore.QSize(711, 755))
        MainWindow.setStyleSheet("")
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 680, 140, 50))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color : #146C94;\n"
"color : #F6F1F1;\n"
"border : 0;\n"
"border-radius: 10px;")
        self.pushButton.setObjectName("pushButton")

        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(300, 420, 140, 50))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton1.setFont(font)
        self.pushButton1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton1.setStyleSheet("background-color : #19A7CE;\n"
                                       "color : #F6F1F1;\n"
                                       "border : 0;\n"
                                       "border-radius: 10px;\n"
                                       "cuesor: pointer;")
        self.pushButton1.setObjectName("pushButton1")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(300, 230, 360, 40))
        self.lineEdit.setStyleSheet("background-color : #19A7CE;\n"
"border: none ;\n"
"border-radius : 10px;\n"
"padding-left : 5px;\n"
"color : white;")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 230, 251, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("text-alignement : center;\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 550, 251, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("text-alignement : center;\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(300, 550, 360, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("text-alignement : center;\n"
"")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 320, 360, 40))
        self.lineEdit_2.setStyleSheet("background-color : #19A7CE;\n"
"border: none ;\n"
"border-radius : 10px;\n"
"padding-left : 5px;\n"
"color : white;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 320, 251, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("text-alignement : center;\n"
"")
        self.label_7.setObjectName("label_7")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(50, 50, 600, 80))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_17.setObjectName("label_17")

        self.choix_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.choix_combobox.setGeometry(QtCore.QRect(120, 160, 500, 41))
        self.choix_combobox.setObjectName("latitudes_combobox")
        self.choix_combobox.setFont(font)
        self.choix_combobox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.choix_combobox.addItem("")
        self.choix_combobox.addItem("")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect methods :
        self.pushButton1.clicked.connect(self.calculer)
        self.pushButton.clicked.connect(self.pagePr)
        self.pushButton.clicked.connect(MainWindow.close)
        self.choix_combobox.currentIndexChanged.connect(self.update_inputs_widgets_state)

    # Fonctions :

    def calculer(self):
        try:
            if self.choix_combobox.currentIndex() == 0 :
                U = self.lineEdit.text()
                U = eval(U)
                erreur_donnee = self.lineEdit_2.text()
                erreur_donnee = eval(erreur_donnee)
                phi_1 = fct.deIsometriqueAPhi(U,erreur_donnee)
                self.label_6.setText(str(phi_1))
            elif self.choix_combobox.currentIndex() == 1:
                phi = self.lineEdit.text()
                phi = eval(phi)
                U = fct.dePhiAisometrique(phi)
                self.label_6.setText(str(U))
        except:
            QMessageBox.critical(MainWindow, 'Erreur',
                                 'Une erreur s\'est produite, vérifier les valeurs que vous avez entré.')
    def update_inputs_widgets_state(self, index):
     self.lineEdit.clear()
     self.lineEdit_2.clear()
     self.label_6.clear()
     if index == 0:
         self.label_4.setText("La valeur de U :")
         self.label_5.setText("La valeur de φ : ")
         self.label_7.setEnabled(True)
         self.lineEdit_2.setEnabled(True)
         self.lineEdit_2.setStyleSheet("background-color : #19A7CE;\n"
                                       "border: none ;\n"
                                       "border-radius : 10px;\n"
                                       "padding-left : 5px;\n"
                                       "color : white;")
     elif index == 1:
         self.label_4.setText("La valeur de φ :")
         self.label_5.setText("La valeur de U : ")
         self.label_7.setEnabled(False)
         self.lineEdit_2.setEnabled(False)
         self.lineEdit_2.setStyleSheet("background-color : gray;\n"
                                       "border: none ;\n"
                                       "border-radius : 10px;\n"
                                       "padding-left : 5px;\n"
                                       "color : white;")
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setWindowTitle("GeoCalc V2.0")
        icon = QIcon("background.png")
        MainWindow.setWindowIcon(icon)
        self.pushButton.setText(_translate("MainWindow", "Retour"))
        self.pushButton1.setText(_translate("MainWindow", "Calculer"))
        self.label_4.setText(_translate("MainWindow", "La valeur de U :"))
        self.label_5.setText(_translate("MainWindow", "La valeur de φ : "))
        self.label_7.setText(_translate("MainWindow", "L\'erreur :"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Calcule de latitude isométrique 𝑈/latitude φ </p><p align=\"center\">sur un ellipsoïde</p></body></html>"))

        self.choix_combobox.setItemText(0, _translate("MainWindow", "Calcule de latitude φ à partir de latitude 𝑈"))
        self.choix_combobox.setItemText(1, _translate("MainWindow", "Calcule de latitude 𝑈 à partir de latitude φ"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = fonction2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
