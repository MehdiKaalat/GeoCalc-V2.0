from PyQt5 import QtCore, QtGui, QtWidgets
from math import *

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox


class fonction1(object):
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
"border-radius: 10px;\n"
"cuesor: pointer;")
        self.pushButton.setObjectName("pushButton")

        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(300, 410, 140, 50))
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
        self.lineEdit.setGeometry(QtCore.QRect(300, 270, 360, 40))
        self.lineEdit.setStyleSheet("background-color : #19A7CE;\n"
"border: none ;\n"
"border-radius : 10px;\n"
"padding-left : 5px;\n"
"color : white;")
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 270, 251, 40))
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
        self.label_5.setGeometry(QtCore.QRect(40, 550, 150, 21))
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
        self.label_6.setGeometry(QtCore.QRect(300, 540, 360, 40))
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
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(50, 50, 600, 80))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_17.setObjectName("label_17")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect methods :
        self.pushButton1.clicked.connect(self.calculer)
        self.pushButton.clicked.connect(self.pagePr)
        self.pushButton.clicked.connect(MainWindow.close)

    # Fonctions :
    def calculer(self):
        try:
            phi = self.lineEdit.text()
            phi = eval(phi)
            a = 6378249.2
            b = 6356515
            e_2 = 1 - ((b ** 2) / (a ** 2))
            U = log(tan((pi / 4) + (phi / 2))) - (e_2 / 2) * log((1 + sqrt(e_2) + sin(phi)) / (1 - sqrt(e_2) + sin(phi)))
            self.label_6.setText(str(U))
        except:
            QMessageBox.critical(MainWindow, 'Erreur',
                                 'Une erreur s\'est produite entrer de nouveau les valeurs.')
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setWindowTitle("GeoCalc")
        icon = QIcon("background.png")
        MainWindow.setWindowIcon(icon)
        self.pushButton.setText(_translate("MainWindow", "Retour"))
        self.pushButton1.setText(_translate("MainWindow", "Calculer"))
        self.label_4.setText(_translate("MainWindow", "La valeur de φ (rad):"))
        self.label_5.setText(_translate("MainWindow", "La valeur de U : "))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Calcule de la latitude isométrique 𝑈 sur </p><p align=\"center\">un ellipsoïde au point de latitude φ</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = fonction1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
