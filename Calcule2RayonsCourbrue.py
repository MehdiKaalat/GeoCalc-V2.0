from PyQt5 import QtCore, QtGui, QtWidgets
from math import *

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox


class fonction6(object):
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
        self.pushButton1.setGeometry(QtCore.QRect(300, 325, 140, 50))
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

        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(50, 50, 600, 80))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_17.setObjectName("label_17")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(30, 210, 200, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("text-alignement : center;\n"
"")
        self.label_13.setObjectName("label_13")

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(30, 160, 200, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("text-alignement : center;\n"
                                    "")
        self.label_1.setObjectName("label_1")

        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(250, 200, 300, 40))
        self.lineEdit_7.setStyleSheet("background-color : #19A7CE;\n"
"border: none ;\n"
"border-radius : 10px;\n"
"color : white;\n"
"padding-left : 5px;\n"
"")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(250, 150, 300, 40))
        self.lineEdit_1.setStyleSheet("background-color : #19A7CE;\n"
                                      "border: none ;\n"
                                      "border-radius : 10px;\n"
                                      "color : white;\n"
                                      "padding-left : 5px;\n"
                                      "")
        self.lineEdit_1.setText("")
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(30, 280, 200, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("text-alignement : center;\n"
"")
        self.label_18.setObjectName("label_18")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(250, 270, 300, 40))
        self.lineEdit_9.setStyleSheet("background-color : #19A7CE;\n"
"border: none ;\n"
"border-radius : 10px;\n"
"color : white;\n"
"padding-left : 5px;\n"
"")
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(560, 210, 50, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("text-alignement : center;\n"
"")
        self.label_24.setObjectName("label_24")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(560, 155, 50, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("text-alignement : center;\n"
                                    "")
        self.label_2.setObjectName("label_2")

        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(560, 280, 50, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("text-alignement : center;\n"
"")
        self.label_25.setObjectName("label_25")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(30, 450, 40, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("text-alignement : center;\n"
"")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(70, 450, 300, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("text-alignement : center;\n"
"color : #146C94")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(70, 550, 300, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("text-alignement : center;\n"
"color : #146C94")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(30, 550, 40, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("text-alignement : center;\n"
"")
        self.label_21.setObjectName("label_21")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(400, 550, 16, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("text-alignement : center;\n"
"")
        self.label_27.setObjectName("label_27")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(400, 450, 16, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("text-alignement : center;\n"
"")
        self.label_29.setObjectName("label_29")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(30, 400, 400, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("text-alignement : center;\n"
"")
        self.label_23.setObjectName("label_23")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(30, 500, 400, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("text-alignement : center;\n"
"")
        self.label_26.setObjectName("label_26")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # Connect methods :
        self.pushButton1.clicked.connect(self.calculer)
        self.pushButton_7.clicked.connect(self.pagePr)
        self.pushButton_7.clicked.connect(MainWindow.close)
    # Fonction
    def calculer(self):
        try:
            phi = radians(float(self.lineEdit_1.text()))
            a = float(self.lineEdit_7.text())
            b = float(self.lineEdit_9.text())
            e2 = float(1 - (b**2/(a**2)))
            W = sqrt(1 - (e2) * (sin(phi) ** 2))
            N = a / W
            M = (a*(1-e2)) / W ** 3
            self.label_20.setText(str(round(M, 10)))
            self.label_22.setText(str(round(N, 10)))
        except:
            QMessageBox.critical(MainWindow, 'Erreur',
                                 'Une erreur s\'est produite, vérifier les valeurs que vous avez entré.')
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setWindowTitle("GeoCalc V2.0")
        icon = QIcon("background.png")
        MainWindow.setWindowIcon(icon)
        self.pushButton_7.setText(_translate("MainWindow", "Retour"))
        self.pushButton1.setText(_translate("MainWindow", "Calculer"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Calcule des 2 rayons de courbure</p><p align=\"center\">𝑹<span style=\" vertical-align:sub;\">𝑴 </span>et 𝑹<span style=\" vertical-align:sub;\">𝑵</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "Demi grand axe a :"))
        self.label_1.setText(_translate("MainWindow", "φ :"))
        self.label_18.setText(_translate("MainWindow", "Demi petit axe b :"))
        self.label_24.setText(_translate("MainWindow", "m"))
        self.label_2.setText(_translate("MainWindow", "deg"))
        self.label_25.setText(_translate("MainWindow", "m"))
        self.label_19.setText(_translate("MainWindow", "M :"))
        self.label_21.setText(_translate("MainWindow", "N :"))
        self.label_27.setText(_translate("MainWindow", "m"))
        self.label_29.setText(_translate("MainWindow", "m"))
        self.label_23.setText(_translate("MainWindow", "Rayon de courbure du méridien :"))
        self.label_26.setText(_translate("MainWindow", "Rayon de courbure du premier vertical :"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = fonction6()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
