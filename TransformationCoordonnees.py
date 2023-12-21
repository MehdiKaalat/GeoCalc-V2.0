from PyQt5 import QtCore, QtGui, QtWidgets
import math
from math import *
import fonctions as fct

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox


class fonction4(object):
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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(300, 680, 140, 50))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("background-color : #146C94;\n"
"color : white;\n"
"border : 0;\n"
"border-radius: 10px;\n"
"cursor:pointer;")
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(300, 390, 140, 50))
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
        self.lineEdit.setGeometry(QtCore.QRect(100, 230, 340, 40))
        self.lineEdit.setStyleSheet("background-color : #19A7CE;\n"
"border: none ;\n"
"border-radius : 10px;\n"
"color :white;\n"
"padding-left : 3px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 280, 340, 40))
        self.lineEdit_2.setStyleSheet("background-color : #19A7CE;\n"
                                    "border: none ;\n"
                                    "border-radius : 10px;\n"
                                    "color :white;\n"
                                    "padding-left : 3px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 530, 150, 21))
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
        self.label_5.setGeometry(QtCore.QRect(40, 600, 150, 21))
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
        self.label_6.setGeometry(QtCore.QRect(405, 600, 60, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("text-alignement : center;\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(405, 530, 60, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("text-alignement : center;\n"
"")
        self.label_11.setObjectName("label_11")

        self.label_66 = QtWidgets.QLabel(self.centralwidget)
        self.label_66.setGeometry(QtCore.QRect(450, 235, 60, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_66.setFont(font)
        self.label_66.setStyleSheet("text-alignement : center;\n"
                                   "")
        self.label_66.setObjectName("label_6")
        self.label_111 = QtWidgets.QLabel(self.centralwidget)
        self.label_111.setGeometry(QtCore.QRect(450, 285, 60, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_111.setFont(font)
        self.label_111.setStyleSheet("text-alignement : center;\n"
                                    "")
        self.label_111.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(40, 340, 550, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("text-alignement : center;\n"
                                    "")
        self.label_12.setObjectName("label_12")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(300, 330, 90, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(9)
        self.comboBox.setFont(font)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setStyleSheet("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(300, 20, 300, 80))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(40, 170, 550, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(40, 470, 550, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_19.setObjectName("label_19")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(40, 240, 50, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("text-alignement : center;\n"
"")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(40, 290, 550, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("text-alignement : center;\n"
"")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(100, 523, 300, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("text-alignement : left;\n"
"")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(100, 592, 300, 40))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("text-alignement : left;\n"
"")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")

        self.choix_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.choix_combobox.setGeometry(QtCore.QRect(70, 100, 586, 41))
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
        self.pushButton_7.clicked.connect(self.pagePr)
        self.pushButton_7.clicked.connect(MainWindow.close)
        self.choix_combobox.currentIndexChanged.connect(self.update_inputs_widgets_state)

    # Fonctions :
    def calculer(self):
        try:
            if self.choix_combobox.currentIndex() == 0:
                X = float(self.lineEdit.text())
                Y = float(self.lineEdit_2.text())
                zone = self.comboBox.currentText()
                L, fi = fct.lambert2Geo(X, Y, zone)
                self.label_15.setText(str(fi))
                self.label_16.setText(str(L))
            elif self.choix_combobox.currentIndex() == 1:
                phi = float(self.lineEdit.text())
                L = float(self.lineEdit_2.text())
                zone = self.comboBox.currentText()
                X, Y = fct.coordGeo2Lambert(L, phi, zone)
                self.label_15.setText(str(X))
                self.label_16.setText(str(Y))
        except:
            QMessageBox.critical(MainWindow, 'Erreur',
                                 'Une erreur s\'est produite entrer de  nouveau les coordonnées.')
    def update_inputs_widgets_state(self, index):
     self.lineEdit.clear()
     self.lineEdit_2.clear()
     if index == 0:
         self.label_13.setText("X : ")
         self.label_14.setText("Y : ")
         self.label_4.setText("φ :")
         self.label_5.setText("λ :")
         self.label_6.setText("deg")
         self.label_11.setText("deg")
         self.label_66.setText("m")
         self.label_111.setText("m")
     if index == 1:
         self.label_6.setText("m")
         self.label_11.setText("m")
         self.label_66.setText("deg")
         self.label_111.setText("deg")
         self.label_13.setText("φ :")
         self.label_14.setText("λ :")
         self.label_4.setText("X : ")
         self.label_5.setText("Y :")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setWindowTitle("GeoCalc")
        icon = QIcon("background.png")
        MainWindow.setWindowIcon(icon)
        self.pushButton_7.setText(_translate("MainWindow", "Retour"))
        self.pushButton1.setText(_translate("MainWindow", "Calculer"))
        self.label_4.setText(_translate("MainWindow", "φ :"))
        self.label_5.setText(_translate("MainWindow", "λ :"))
        self.label_6.setText(_translate("MainWindow", "deg"))
        self.label_11.setText(_translate("MainWindow", "deg"))

        self.label_66.setText(_translate("MainWindow", "m"))
        self.label_111.setText(_translate("MainWindow", "m"))

        self.label_12.setText(_translate("MainWindow", "Choisir la zone :"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Zone 1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Zone 2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Zone 3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Zone 4"))
        self.label_17.setText(_translate("MainWindow", "Transformer :"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Ecrire les coordonnées de projection Lambert  : </span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Les coordonnées géographiques :</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "X :"))
        self.label_14.setText(_translate("MainWindow", "Y :"))

        self.choix_combobox.setItemText(0, _translate("MainWindow", "Les coordonnées Lambert en coordonnées géographique"))
        self.choix_combobox.setItemText(1, _translate("MainWindow", "Les coordonnées géographique en coordonnées Lambert"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = fonction4()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
