from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

from CalculeLatitudePhEtIsometriquei import fonction2
from TransformationCoordonnees import fonction4
from CalculeParametresEllipsoide import fonction5
from Calcule2RayonsCourbrue import fonction6
from LongueurArcSurfaceV2 import LongueurArcSurface
from CalculLatitudesV2 import calculLatitudes
from problemeDirectInverseSphereV2 import prbDirectEtInverseSphere
from problemeDirectInverseEllipsoideV2 import prbDirectEtInverseEllipsoide


class pagePrincipale(object):
    def commencer(self):
        from commencer import Ui_MainWindow
        self.window1 = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window1)
        self.window1.show()
    def LongueurArcSurface(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = LongueurArcSurface()
        self.ui.setupUi(self.window2)
        self.window2.show()
    def calculLatitudes(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = calculLatitudes()
        self.ui.setupUi(self.window2)
        self.window2.show()
    def prbDirectEtInverseSphere(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = prbDirectEtInverseSphere()
        self.ui.setupUi(self.window2)
        self.window2.show()
    def prbDirectEtInverseEllipsoide(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = prbDirectEtInverseEllipsoide()
        self.ui.setupUi(self.window2)
        self.window2.show()
    def Fct2(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = fonction2()
        self.ui.setupUi(self.window2)
        self.window2.show()
    def Fct4(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = fonction4()
        self.ui.setupUi(self.window2)
        self.window2.show()
    def Fct5(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = fonction5()
        self.ui.setupUi(self.window2)
        self.window2.show()
    def Fct6(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = fonction6()
        self.ui.setupUi(self.window2)
        self.window2.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(711, 755)
        MainWindow.setMinimumSize(QtCore.QSize(711, 755))
        MainWindow.setMaximumSize(QtCore.QSize(711, 755))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 70, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setGeometry(QtCore.QRect(290, 670, 140, 50))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color : #146C94;\n"
"color : white;\n"
"border : 0;\n"
"border-radius: 10px;\n"
"cursor:pointer;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(65, 130, 580, 500))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color : #19A7CE;\n"
                                        "color : #F6F1F1;\n"
                                        "border : 0;\n"
                                        "border-radius : 10px;\n"
                                        "display : block;\n"
                                        "height : 40px;\n"
                                        "cursor:pointer;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.latitudesButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.latitudesButton.setFont(font)
        self.latitudesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.latitudesButton.setStyleSheet("background-color : #19A7CE;\n"
                                      "color : #F6F1F1;\n"
                                      "border : 0;\n"
                                      "border-radius : 10px;\n"
                                      "display : block;\n"
                                      "height : 40px;\n"
                                      "cursor:pointer;")
        self.latitudesButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.latitudesButton)

        self.prbSphereButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.prbSphereButton.setFont(font)
        self.prbSphereButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prbSphereButton.setStyleSheet("background-color : #19A7CE;\n"
                                           "color : #F6F1F1;\n"
                                           "border : 0;\n"
                                           "border-radius : 10px;\n"
                                           "display : block;\n"
                                           "height : 40px;\n"
                                           "cursor:pointer;")
        self.prbSphereButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.prbSphereButton)

        self.prbEllipsoideButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.prbEllipsoideButton.setFont(font)
        self.prbEllipsoideButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prbEllipsoideButton.setStyleSheet("background-color : #19A7CE;\n"
                                           "color : #F6F1F1;\n"
                                           "border : 0;\n"
                                           "border-radius : 10px;\n"
                                           "display : block;\n"
                                           "height : 40px;\n"
                                           "cursor:pointer;")
        self.prbEllipsoideButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.prbEllipsoideButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color : #19A7CE;\n"
"color : #F6F1F1;\n"
"border : 0;\n"
"border-radius : 10px;\n"
"display : block;\n"
"height : 40px;\n"
"cursor:pointer;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("background-color : #19A7CE;\n"
"color : #F6F1F1;\n"
"border : 0;\n"
"border-radius : 10px;\n"
"display : block;\n"
"height : 40px;\n"
"cursor:pointer;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("background-color : #19A7CE;\n"
"color : #F6F1F1;\n"
"border : 0;\n"
"border-radius : 10px;\n"
"display : block;\n"
"height : 40px;\n"
"cursor:pointer;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("background-color : #19A7CE;\n"
"color : #F6F1F1;\n"
"border : 0;\n"
"border-radius : 10px;\n"
"display : block;\n"
"height : 40px;\n"
"cursor:pointer;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton_7.clicked.connect(self.commencer)
        self.pushButton_7.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.Fct2)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.LongueurArcSurface)
        self.pushButton.clicked.connect(MainWindow.close)
        self.latitudesButton.clicked.connect(self.calculLatitudes)
        self.latitudesButton.clicked.connect(MainWindow.close)

        self.prbSphereButton.clicked.connect(self.prbDirectEtInverseSphere)
        self.prbSphereButton.clicked.connect(MainWindow.close)
        self.prbEllipsoideButton.clicked.connect(self.prbDirectEtInverseEllipsoide)
        self.prbEllipsoideButton.clicked.connect(MainWindow.close)

        self.pushButton_4.clicked.connect(self.Fct4)
        self.pushButton_4.clicked.connect(MainWindow.close)
        self.pushButton_5.clicked.connect(self.Fct5)
        self.pushButton_5.clicked.connect(MainWindow.close)
        self.pushButton_6.clicked.connect(self.Fct6)
        self.pushButton_6.clicked.connect(MainWindow.close)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setWindowTitle("GeoCalc V2.0")
        icon = QIcon("background.png")
        MainWindow.setWindowIcon(icon)
        self.label_2.setText(_translate("MainWindow", "Choisir une opération : "))
        self.pushButton_7.setText(_translate("MainWindow", "Retour"))
        self.pushButton.setText(_translate("MainWindow", "Calcul des longueurs d'arc et surface sur ellipsoide"))
        self.latitudesButton.setText(_translate("MainWindow", "Calcul des latitudes géodésique φ, géocentrique Ψ, réduite β"))
        self.prbSphereButton.setText(_translate("MainWindow", "Résolution du problème direct et inverse sur Sphère"))
        self.prbEllipsoideButton.setText(_translate("MainWindow", "Résolution du problème direct et inverse sur Ellipsoide"))
        self.pushButton_2.setText(_translate("MainWindow", "Calcul des latitudes géodésique φ et isométrique U"))
        self.pushButton_4.setText(_translate("MainWindow", "Transformation des coordonnées"))
        self.pushButton_5.setText(_translate("MainWindow", "Calcul des paramètres d\'un ellipsoide"))
        self.pushButton_6.setText(_translate("MainWindow", "Calcul des 2 rayons de courbure"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = pagePrincipale()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
