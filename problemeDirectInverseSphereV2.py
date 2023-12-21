from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

import fonctions as fct

class prbDirectEtInverseSphere(object):
    def pagePr(self):
        from pageprincipale import pagePrincipale
        self.window1 = QtWidgets.QMainWindow()
        self.ui = pagePrincipale()
        self.ui.setupUi(self.window1)
        self.window1.show()
    def resoudre(self):
        try:
            if self.probleme_choisi_combobox.currentIndex() == 0:
                rayon_choisi = self.rayon_choisi_combobox.currentText()
                phi1 = float(self.phi1_input.text())
                lambda1 = float(self.lambda1_input.text())
                distance = float(self.distance_input.text())
                A12 = float(self.A12_input.text())
                phi2,lambda2,A21 = fct.probleme_direct_sphere(phi1,lambda1,distance,A12, rayon_choisi)
                self.phi2_output.setText(str(phi2))
                self.lambda2_output.setText(str(lambda2))
                self.A21_output.setText(str(A21))
            elif self.probleme_choisi_combobox.currentIndex() == 1:
                phi1 = float(self.phi1_input.text())
                lambda1 = float(self.lambda1_input.text())
                phi2 = float(self.distance_input.text())
                lambda2 = float(self.A12_input.text())
                A12,A21,sigma = fct.probleme_inverse_sphere(phi1,lambda1,phi2,lambda2)
                self.phi2_output.setText(str(sigma))
                self.lambda2_output.setText(str(A12))
                self.A21_output.setText(str(A21))
        except:
            QMessageBox.critical(MainWindow, 'Erreur',
                                 'Une erreur s\'est produite, vérifier les valeurs que vous avez entré.')
    def update_inputs_widgets_state(self,index):
        self.phi1_input.clear()
        self.lambda1_input.clear()
        self.distance_input.clear()
        self.A12_input.clear()
        self.phi2_output.clear()
        self.lambda2_output.clear()
        self.A21_output.clear()
        if index == 0:
            self.rayon_choisi_combobox.setEnabled(True)
            self.phi1_text.setText("φ1(degré) : ")
            self.lambda1_text.setText("λ1(degré) : ")
            self.distance_text.setText("S(m) : ")
            self.A12_text.setText("A12(degré) : ")

            self.phi2_text.setText("φ2(degré) : ")
            self.lambda2_text.setText("λ2(degré) : ")
            self.A21_text.setText("A21(degré) : ")
        elif index == 1:
            self.rayon_choisi_combobox.setEnabled(False)
            self.phi1_text.setText("φ1(degré) : ")
            self.lambda1_text.setText("λ1(degré) : ")
            self.distance_text.setText("φ2(degré) : ")
            self.A12_text.setText("λ2(degré) : ")

            self.phi2_text.setText("σ12(degré) : ")
            self.lambda2_text.setText("A12(degré) : ")
            self.A21_text.setText("A21(degré) : ")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.retourButton = QtWidgets.QPushButton(self.centralwidget)
        self.retourButton.setGeometry(QtCore.QRect(600, 520, 140, 50))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.retourButton.setFont(font)
        self.retourButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.retourButton.setStyleSheet("background-color : #146C94;\n"
                                        "color : white;\n"
                                        "border : 0;\n"
                                        "border-radius: 10px;\n"
                                        "cursor:pointer;")
        self.retourButton.setObjectName("retourButton")

        self.centralwidget.setObjectName("centralwidget")
        self.phi2_text = QtWidgets.QLabel(self.centralwidget)
        self.phi2_text.setGeometry(QtCore.QRect(10, 410, 201, 31))
        self.phi2_text.setStyleSheet("font-size : 16px;\n"
"font-weight : bold;")
        self.phi2_text.setObjectName("phi2_text")
        self.lambda2_text = QtWidgets.QLabel(self.centralwidget)
        self.lambda2_text.setGeometry(QtCore.QRect(10, 470, 201, 31))
        self.lambda2_text.setStyleSheet("font-size : 16px;\n"
"font-weight : bold;")
        self.lambda2_text.setObjectName("lambda2_text")
        self.titre = QtWidgets.QLabel(self.centralwidget)
        self.titre.setGeometry(QtCore.QRect(240, 20, 401, 41))
        self.titre.setStyleSheet("font-size : 20px;\n"
"font-weight : bold;")
        self.titre.setObjectName("titre")
        self.phi1_text = QtWidgets.QLabel(self.centralwidget)
        self.phi1_text.setGeometry(QtCore.QRect(10, 200, 111, 31))
        self.phi1_text.setStyleSheet("font-size : 16px;\n"
"font-weight : bold;")
        self.phi1_text.setObjectName("phi1_text")
        self.probleme_choisi_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.probleme_choisi_combobox.setGeometry(QtCore.QRect(290, 90, 311, 41))
        self.probleme_choisi_combobox.setStyleSheet("font-size : 16px;\n"
"font-weight:bold;")
        self.probleme_choisi_combobox.setObjectName("probleme_choisi_combobox")
        self.probleme_choisi_combobox.addItem("")
        self.probleme_choisi_combobox.addItem("")
        self.Resoudre_text = QtWidgets.QLabel(self.centralwidget)
        self.Resoudre_text.setGeometry(QtCore.QRect(10, 90, 211, 41))
        self.Resoudre_text.setStyleSheet("font-size : 16px;\n"
"font-weight : bold;")
        self.Resoudre_text.setObjectName("Resoudre_text")
        self.calculer_button = QtWidgets.QPushButton(self.centralwidget)
        self.calculer_button.setGeometry(QtCore.QRect(300, 320, 171, 41))
        self.calculer_button.setStyleSheet("font-size : 16px;\n"
"font-weight : bold;")
        self.calculer_button.setObjectName("calculer_button")
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.calculer_button.setFont(font)
        self.calculer_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculer_button.setStyleSheet("background-color : #19A7CE;\n"
                                           "color : #F6F1F1;\n"
                                           "border : 0;\n"
                                           "border-radius: 10px;\n"
                                           "cuesor: pointer;")
        self.phi1_input = QtWidgets.QLineEdit(self.centralwidget)
        self.phi1_input.setGeometry(QtCore.QRect(130, 190, 221, 41))
        self.phi1_input.setObjectName("phi1_input")
        self.phi2_output = QtWidgets.QLabel(self.centralwidget)
        self.phi2_output.setGeometry(QtCore.QRect(290, 410, 271, 41))
        self.phi2_output.setStyleSheet("font-size : 16px;\n"
"font-weight : bold;")
        self.phi2_output.setText("")
        self.phi2_output.setObjectName("phi2_output")
        self.lambda2_output = QtWidgets.QLabel(self.centralwidget)
        self.lambda2_output.setGeometry(QtCore.QRect(290, 460, 271, 41))
        self.lambda2_output.setStyleSheet("font-size : 16px;\n"
"font-weight : bold;")
        self.lambda2_output.setText("")
        self.lambda2_output.setObjectName("lambda2_output")
        self.lambda1_text = QtWidgets.QLabel(self.centralwidget)
        self.lambda1_text.setGeometry(QtCore.QRect(410, 200, 111, 31))
        self.lambda1_text.setStyleSheet("font-size : 16px;\n"
"font-weight : bold;")
        self.lambda1_text.setObjectName("lambda1_text")
        self.lambda1_input = QtWidgets.QLineEdit(self.centralwidget)
        self.lambda1_input.setGeometry(QtCore.QRect(530, 190, 221, 41))
        self.lambda1_input.setObjectName("lambda1_input")
        self.distance_text = QtWidgets.QLabel(self.centralwidget)
        self.distance_text.setGeometry(QtCore.QRect(10, 260, 111, 31))
        self.distance_text.setStyleSheet("font-size : 16px;\n"
"font-weight : bold;")
        self.distance_text.setObjectName("distance_text")
        self.distance_input = QtWidgets.QLineEdit(self.centralwidget)
        self.distance_input.setGeometry(QtCore.QRect(130, 250, 221, 41))
        self.distance_input.setObjectName("distance_input")
        self.A12_text = QtWidgets.QLabel(self.centralwidget)
        self.A12_text.setGeometry(QtCore.QRect(410, 260, 111, 31))
        self.A12_text.setStyleSheet("font-size : 16px;\n"
"font-weight : bold;")
        self.A12_text.setObjectName("A12_text")
        self.A12_input = QtWidgets.QLineEdit(self.centralwidget)
        self.A12_input.setGeometry(QtCore.QRect(530, 250, 221, 41))
        self.A12_input.setObjectName("A12_input")
        self.rayon_choisi_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.rayon_choisi_combobox.setGeometry(QtCore.QRect(290, 140, 471, 41))
        self.rayon_choisi_combobox.setStyleSheet("font-size : 16px;\n"
"font-weight:bold;")
        self.rayon_choisi_combobox.setObjectName("rayon_choisi_combobox")
        self.rayon_choisi_combobox.addItem("")
        self.rayon_choisi_combobox.addItem("")
        self.rayon_choisi_combobox.addItem("")
        self.rayon_choisi_combobox.addItem("")
        self.rayon_choisi_text = QtWidgets.QLabel(self.centralwidget)
        self.rayon_choisi_text.setGeometry(QtCore.QRect(10, 140, 211, 41))
        self.rayon_choisi_text.setStyleSheet("font-size : 16px;\n"
"font-weight : bold;")
        self.rayon_choisi_text.setObjectName("rayon_choisi_text")
        self.A21_text = QtWidgets.QLabel(self.centralwidget)
        self.A21_text.setGeometry(QtCore.QRect(10, 530, 201, 31))
        self.A21_text.setStyleSheet("font-size : 16px;\n"
"font-weight : bold;")
        self.A21_text.setObjectName("A21_text")
        self.A21_output = QtWidgets.QLabel(self.centralwidget)
        self.A21_output.setGeometry(QtCore.QRect(290, 520, 271, 41))
        self.A21_output.setStyleSheet("font-size : 16px;\n"
"font-weight : bold;")
        self.A21_output.setText("")
        self.A21_output.setObjectName("A21_output")

        self.phi1_input.setStyleSheet("background-color : #19A7CE;\n"
                                      "border: none ;\n"
                                      "border-radius : 10px;\n"
                                      "padding-left : 5px;\n"
                                      "color : white;")
        self.lambda1_input.setStyleSheet("background-color : #19A7CE;\n"
                                         "border: none ;\n"
                                         "border-radius : 10px;\n"
                                         "padding-left : 5px;\n"
                                         "color : white;")
        self.A12_input.setStyleSheet("background-color : #19A7CE;\n"
                                     "border: none ;\n"
                                     "border-radius : 10px;\n"
                                     "padding-left : 5px;\n"
                                     "color : white;")
        self.distance_input.setStyleSheet("background-color : #19A7CE;\n"
                                          "border: none ;\n"
                                          "border-radius : 10px;\n"
                                          "padding-left : 5px;\n"
                                          "color : white;")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.probleme_choisi_combobox.currentIndexChanged.connect(self.update_inputs_widgets_state)
        self.calculer_button.clicked.connect(self.resoudre)
        self.retourButton.clicked.connect(self.pagePr)
        self.retourButton.clicked.connect(MainWindow.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setWindowTitle("GeoCalc V2.0")
        icon = QIcon("background.png")
        MainWindow.setWindowIcon(icon)
        self.phi2_text.setText(_translate("MainWindow", "φ2(degré) : "))
        self.lambda2_text.setText(_translate("MainWindow", "λ2(degré) : "))
        self.titre.setText(_translate("MainWindow", "Problèmes direct et inverse sur sphère"))
        self.phi1_text.setText(_translate("MainWindow", "φ1(degré) : "))
        self.probleme_choisi_combobox.setItemText(0, _translate("MainWindow", "Probléme direct sur sphère"))
        self.probleme_choisi_combobox.setItemText(1, _translate("MainWindow", "Probléme inverse sur sphère"))
        self.Resoudre_text.setText(_translate("MainWindow", "Résoudre :"))
        self.calculer_button.setText(_translate("MainWindow", "Calculer"))
        self.lambda1_text.setText(_translate("MainWindow", "λ1(degré) : "))
        self.distance_text.setText(_translate("MainWindow", "S(m) : "))
        self.A12_text.setText(_translate("MainWindow", "A12(degré) : "))
        self.rayon_choisi_combobox.setItemText(0, _translate("MainWindow", "Rayon moyen des demi-axes"))
        self.rayon_choisi_combobox.setItemText(1, _translate("MainWindow", "Rayon d’une sphère de même superficie que l’ellipsoïde"))
        self.rayon_choisi_combobox.setItemText(2, _translate("MainWindow", "Rayon d’une sphère de même volume que l’ellipsoïde"))
        self.rayon_choisi_combobox.setItemText(3, _translate("MainWindow", "Rayon moyen de Gauss"))
        self.rayon_choisi_text.setText(_translate("MainWindow", "Rayon choisi :"))
        self.A21_text.setText(_translate("MainWindow", "A21(degré) : "))
        self.retourButton.setText(_translate("MainWindow", "Retour"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = prbDirectEtInverseSphere()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
