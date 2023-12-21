from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

import fonctions as fct

class MatplotlibCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=100):
        fig, self.ax = plt.subplots(subplot_kw={'projection': ccrs.Orthographic()},
                                    figsize=(width, height), dpi=dpi)
        super(MatplotlibCanvas, self).__init__(fig)
        self.setParent(parent)

        self.ax.add_feature(cfeature.COASTLINE)
        self.ax.add_feature(cfeature.BORDERS, linestyle=':')
        self.ax.gridlines()
        self.ax.set_global()
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
    def clear_function(self):
        self.ax.clear()
        self.ax.add_feature(cfeature.COASTLINE)
        self.ax.add_feature(cfeature.BORDERS, linestyle=':')
        self.ax.gridlines()
        self.ax.set_global()
    def representation_surface(self, phi1, lam1, phi2, lam2):
        self.clear_function()
        self.central_longitude = (lam1 + lam2) / 2
        self.central_latitude = (phi1 + phi2) / 2
        self.ax.projection = ccrs.Orthographic(central_longitude=self.central_longitude, central_latitude=self.central_latitude)

        lons = [lam1, lam2, lam2, lam1, lam1]
        lats = [phi1, phi1, phi2, phi2, phi1]

        self.ax.fill(lons, lats, color='red', alpha=0.5, transform=ccrs.PlateCarree())
        self.ax.plot(lam1, phi1, 'bo', markersize=2, transform=ccrs.PlateCarree(), label='Point 1')
        self.ax.plot(lam2, phi2, 'bo', markersize=2, transform=ccrs.PlateCarree(), label='Point 2')

        self.draw()
    def representation_arc_meridien(self,phi1, phi2):
        self.clear_function()
        self.central_longitude = (phi1 + phi2) / 2
        self.ax.projection = ccrs.Orthographic(central_longitude=self.central_longitude)

        lons = [0, 0]  # Longitudes centrées autour de 0
        lats = [phi1, phi2]

        self.ax.plot(lons, lats, color='red', linewidth=2, linestyle='-', transform=ccrs.PlateCarree())
        self.draw()
    def representation_arc_parallele(self,lambda1, lambda2):
        self.clear_function()
        self.central_latitudes = (lambda1 + lambda2) / 2
        self.ax.projection = ccrs.Orthographic(central_latitude=self.central_latitudes)

        # Tracer l'arc entre lambda1 et lambda2
        lons = [lambda1, lambda2]
        lats = [0, 0] # Latitudes centrées autour de 0

        self.ax.plot(lons, lats, color='red', linewidth=2, linestyle='-', transform=ccrs.PlateCarree())
        self.draw()
class LongueurArcSurface(object):
    def pagePr(self):
        from pageprincipale import pagePrincipale
        self.window1 = QtWidgets.QMainWindow()
        self.ui = pagePrincipale()
        self.ui.setupUi(self.window1)
        self.window1.show()
    def calculer_longueur_arc(self):
        try:
            if self.meridienParallele_combobox.currentIndex() == 0:
                phi1 = float(self.phi1_input.text())
                phi2 = float(self.phi2_input.text())
                resultat = fct.longueur_arc_meridien(phi1,phi2)
                self.resultat.setText(str(resultat))
                self.matplotlib_widget.representation_arc_meridien(phi1,phi2)

            elif self.meridienParallele_combobox.currentIndex() == 1:
                lambda1 = float(self.lambda1_input.text())
                lambda2 = float(self.lambda2_input.text())
                phi = float(self.phi_input.text())
                resultat = fct.LongueurArcParallele(phi, lambda1, lambda2)
                self.resultat.setText(str(resultat))
                self.matplotlib_widget.representation_arc_parallele(lambda1, lambda2)
            elif self.meridienParallele_combobox.currentIndex() == 2:
                phi1 = float(self.phi1_input.text())
                phi2 = float(self.phi2_input.text())
                lambda1 = float(self.lambda1_input.text())
                lambda2 = float(self.lambda2_input.text())
                resultat = fct.surfaceSurEllipsoide(phi1, phi2, lambda1, lambda2)
                self.resultat.setText(str(resultat))
                self.matplotlib_widget.representation_surface(phi1, lambda1, phi2, lambda2)
        except:
            QMessageBox.critical(MainWindow, 'Erreur',
                                 'Une erreur s\'est produite, vérifier les valeurs que vous avez entré.')
    def update_inputs_widgets_state(self, index):
        self.resultat.clear()
        self.phi1_input.clear()
        self.phi2_input.clear()
        self.lambda1_input.clear()
        self.lambda2_input.clear()
        self.phi_input.clear()
        if index == 0:
            self.resultat_text.setText("Longueur d'arc du Méridien(Km) : ")
            self.phi1_text.setEnabled(True)
            self.phi1_input.setEnabled(True)
            self.phi2_text.setEnabled(True)
            self.phi2_input.setEnabled(True)

            self.lambda1_text.setEnabled(False)
            self.lambda1_input.setEnabled(False)
            self.lambda2_text.setEnabled(False)
            self.lambda2_input.setEnabled(False)
            self.phi.setEnabled(False)
            self.phi_input.setEnabled(False)

            self.phi1_input.setStyleSheet("background-color : #19A7CE;\n"
                                          "border: none ;\n"
                                          "border-radius : 10px;\n"
                                          "padding-left : 5px;\n"
                                          "color : white;")
            self.phi2_input.setStyleSheet("background-color : #19A7CE;\n"
                                          "border: none ;\n"
                                          "border-radius : 10px;\n"
                                          "padding-left : 5px;\n"
                                          "color : white;")
            self.lambda1_input.setStyleSheet("background-color : gray;\n"
                                             "border: none ;\n"
                                             "border-radius : 10px;\n"
                                             "padding-left : 5px;\n"
                                             "color : white;")
            self.lambda2_input.setStyleSheet("background-color : gray;\n"
                                             "border: none ;\n"
                                             "border-radius : 10px;\n"
                                             "padding-left : 5px;\n"
                                             "color : white;")
            self.phi_input.setStyleSheet("background-color : gray;\n"
                                         "border: none ;\n"
                                         "border-radius : 10px;\n"
                                         "padding-left : 5px;\n"
                                         "color : white;")

        elif self.meridienParallele_combobox.currentIndex() == 1:
            self.resultat_text.setText("Longueur d'arc du premier vertical(Km) : ")
            self.lambda1_text.setEnabled(True)
            self.lambda1_input.setEnabled(True)
            self.lambda2_text.setEnabled(True)
            self.lambda2_input.setEnabled(True)
            self.phi.setEnabled(True)
            self.phi_input.setEnabled(True)

            self.phi1_text.setEnabled(False)
            self.phi1_input.setEnabled(False)
            self.phi2_text.setEnabled(False)
            self.phi2_input.setEnabled(False)

            self.phi1_input.setStyleSheet("background-color : gray;\n"
                                             "border: none ;\n"
                                             "border-radius : 10px;\n"
                                             "padding-left : 5px;\n"
                                             "color : white;")
            self.phi2_input.setStyleSheet("background-color : gray;\n"
                                             "border: none ;\n"
                                             "border-radius : 10px;\n"
                                             "padding-left : 5px;\n"
                                             "color : white;")
            self.lambda1_input.setStyleSheet("background-color : #19A7CE;\n"
                                             "border: none ;\n"
                                             "border-radius : 10px;\n"
                                             "padding-left : 5px;\n"
                                             "color : white;")
            self.lambda2_input.setStyleSheet("background-color : #19A7CE;\n"
                                             "border: none ;\n"
                                             "border-radius : 10px;\n"
                                             "padding-left : 5px;\n"
                                             "color : white;")
            self.phi_input.setStyleSheet("background-color : #19A7CE;\n"
                                         "border: none ;\n"
                                         "border-radius : 10px;\n"
                                         "padding-left : 5px;\n"
                                         "color : white;")

        elif self.meridienParallele_combobox.currentIndex() ==  2:
            self.resultat_text.setText("La superficie délimitée(Km²) :")
            self.lambda1_text.setEnabled(True)
            self.lambda1_input.setEnabled(True)
            self.lambda2_text.setEnabled(True)
            self.lambda2_input.setEnabled(True)
            self.phi.setEnabled(False)
            self.phi_input.setEnabled(False)
            self.phi1_text.setEnabled(True)
            self.phi1_input.setEnabled(True)
            self.phi2_text.setEnabled(True)
            self.phi2_input.setEnabled(True)

            self.phi1_input.setStyleSheet("background-color : #19A7CE;\n"
                                          "border: none ;\n"
                                          "border-radius : 10px;\n"
                                          "padding-left : 5px;\n"
                                          "color : white;")
            self.phi2_input.setStyleSheet("background-color : #19A7CE;\n"
                                          "border: none ;\n"
                                          "border-radius : 10px;\n"
                                          "padding-left : 5px;\n"
                                          "color : white;")
            self.lambda1_input.setStyleSheet("background-color : #19A7CE;\n"
                                             "border: none ;\n"
                                             "border-radius : 10px;\n"
                                             "padding-left : 5px;\n"
                                             "color : white;")
            self.lambda2_input.setStyleSheet("background-color : #19A7CE;\n"
                                             "border: none ;\n"
                                             "border-radius : 10px;\n"
                                             "padding-left : 5px;\n"
                                             "color : white;")
            self.phi_input.setStyleSheet("background-color : gray;\n"
                                         "border: none ;\n"
                                         "border-radius : 10px;\n"
                                         "padding-left : 5px;\n"
                                         "color : white;")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Calcul du longueur d'arc d'un ellipsoide")
        MainWindow.resize(1300, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.retourButton = QtWidgets.QPushButton(self.centralwidget)
        self.retourButton.setGeometry(QtCore.QRect(290, 520, 140, 50))
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

        self.lambda1_text = QtWidgets.QLabel(self.centralwidget)
        self.lambda1_text.setGeometry(QtCore.QRect(10, 220, 51, 31))
        self.lambda1_text.setStyleSheet("font-size : 16px;\n"
"font-weight : bold;")
        self.lambda1_text.setObjectName("lambda1_text")
        self.phi_input = QtWidgets.QLineEdit(self.centralwidget)
        self.phi_input.setGeometry(QtCore.QRect(300, 290, 211, 41))
        self.phi_input.setObjectName("phi_input")
        self.phi_input.setStyleSheet("background-color : #19A7CE;\n"
                                      "border: none ;\n"
                                      "border-radius : 10px;\n"
                                      "color : white;\n"
                                      "padding-left : 5px;\n"
                                      "")
        self.phi2_input = QtWidgets.QLineEdit(self.centralwidget)
        self.phi2_input.setGeometry(QtCore.QRect(430, 150, 261, 41))
        self.phi2_input.setObjectName("phi2_input")
        self.phi2_input.setStyleSheet("background-color : #19A7CE;\n"
                                                 "border: none ;\n"
                                                 "border-radius : 10px;\n"
                                                 "color : white;\n"
                                                 "padding-left : 5px;\n"
                                                 "")
        self.phi2_text = QtWidgets.QLabel(self.centralwidget)
        self.phi2_text.setGeometry(QtCore.QRect(380, 160, 51, 31))
        self.phi2_text.setStyleSheet("font-size : 16px;\n"
"font-weight : bold;")
        self.phi2_text.setObjectName("phi2_text")
        self.lambda1_input = QtWidgets.QLineEdit(self.centralwidget)
        self.lambda1_input.setGeometry(QtCore.QRect(60, 210, 261, 41))
        self.lambda1_input.setObjectName("lambda1_input")
        self.lambda1_input.setStyleSheet("background-color : #19A7CE;\n"
                                      "border: none ;\n"
                                      "border-radius : 10px;\n"
                                      "color : white;\n"
                                      "padding-left : 5px;\n"
                                      "")
        self.lambda2_input = QtWidgets.QLineEdit(self.centralwidget)
        self.lambda2_input.setGeometry(QtCore.QRect(430, 210, 261, 41))
        self.lambda2_input.setObjectName("lambda2_input")
        self.lambda2_input.setStyleSheet("background-color : #19A7CE;\n"
                                      "border: none ;\n"
                                      "border-radius : 10px;\n"
                                      "color : white;\n"
                                      "padding-left : 5px;\n"
                                      "")
        self.lambda2_text = QtWidgets.QLabel(self.centralwidget)
        self.lambda2_text.setGeometry(QtCore.QRect(380, 220, 51, 31))
        self.lambda2_text.setStyleSheet("font-size : 16px;\n"
"font-weight : bold;")
        self.lambda2_text.setObjectName("lambda2_text")
        self.phi = QtWidgets.QLabel(self.centralwidget)
        self.phi.setGeometry(QtCore.QRect(260, 300, 51, 31))
        self.phi.setStyleSheet("font-size : 16px;\n"
"font-weight : bold;")
        self.phi.setObjectName("phi")
        self.titre = QtWidgets.QLabel(self.centralwidget)
        self.titre.setGeometry(QtCore.QRect(65, 20, 601, 41))
        self.titre.setStyleSheet("font-size : 20px;\n"
"font-weight : bold;")
        self.titre.setObjectName("titre")
        self.resultat_text = QtWidgets.QLabel(self.centralwidget)
        self.resultat_text.setGeometry(QtCore.QRect(40, 460, 320, 41))
        self.resultat_text.setStyleSheet("font-size : 16px;\n"
"font-weight : bold;")
        self.resultat_text.setObjectName("resultat_text")
        self.phi1_text = QtWidgets.QLabel(self.centralwidget)
        self.phi1_text.setGeometry(QtCore.QRect(10, 160, 51, 31))
        self.phi1_text.setStyleSheet("font-size : 16px;\n"
"font-weight : bold;")
        self.phi1_text.setObjectName("phi1_text")
        self.meridienParallele_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.meridienParallele_combobox.setGeometry(QtCore.QRect(290, 90, 351, 51))
        self.meridienParallele_combobox.setStyleSheet("font-size : 16px;\n"
"font-weight:bold;")
        self.meridienParallele_combobox.setObjectName("meridienParallele_combobox")
        self.meridienParallele_combobox.addItem("")
        self.meridienParallele_combobox.addItem("")
        self.meridienParallele_combobox.addItem("")
        self.longueur_ar_text = QtWidgets.QLabel(self.centralwidget)
        self.longueur_ar_text.setGeometry(QtCore.QRect(10, 90, 211, 41))
        self.longueur_ar_text.setStyleSheet("font-size : 16px;\n"
"font-weight : bold;")
        self.longueur_ar_text.setObjectName("longueur_ar_text")
        self.calculer_button = QtWidgets.QPushButton(self.centralwidget)
        self.calculer_button.setGeometry(QtCore.QRect(290, 380, 171, 41))
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
        self.resultat = QtWidgets.QLabel(self.centralwidget)
        self.resultat.setGeometry(QtCore.QRect(390, 460, 271, 41))
        self.resultat.setStyleSheet("font-size : 16px;\n"
"font-weight : bold;")

        self.resultat.setObjectName("resultat")
        self.phi1_input = QtWidgets.QLineEdit(self.centralwidget)
        self.phi1_input.setGeometry(QtCore.QRect(60, 150, 261, 41))
        self.phi1_input.setObjectName("phi1_input")
        self.phi1_input.setStyleSheet("background-color : #19A7CE;\n"
                                                 "border: none ;\n"
                                                 "border-radius : 10px;\n"
                                                 "color : white;\n"
                                                 "padding-left : 5px;\n"
                                                 "")
        self.lambda1_input.setStyleSheet("background-color : gray;\n"
                                         "border: none ;\n"
                                         "border-radius : 10px;\n"
                                         "padding-left : 5px;\n"
                                         "color : white;")
        self.lambda2_input.setStyleSheet("background-color : gray;\n"
                                         "border: none ;\n"
                                         "border-radius : 10px;\n"
                                         "padding-left : 5px;\n"
                                         "color : white;")
        self.phi_input.setStyleSheet("background-color : gray;\n"
                                     "border: none ;\n"
                                     "border-radius : 10px;\n"
                                     "padding-left : 5px;\n"
                                     "color : white;")
        MainWindow.setCentralWidget(self.centralwidget)

        # Add a widget to display the matplotlib figure
        self.matplotlib_widget = MatplotlibCanvas(self.centralwidget)
        self.matplotlib_widget.setGeometry(QtCore.QRect(700, 0, 600, 600))

        # Remove the "Configure subplots" button from the toolbar
        NavigationToolbar.toolitems = NavigationToolbar.toolitems[:6] + NavigationToolbar.toolitems[8:]
        # Create the navigation toolbar using MainWindow (QMainWindow)
        navigation_toolbar = NavigationToolbar(self.matplotlib_widget, MainWindow)
        # Create a custom CSS style sheet
        style_sheet = """
        QToolBar {
            text-align: center;
            padding: 0;
            margin: 0 ;
            
        }

        QToolButton {
            padding: 0 6px;
        }
        """

        # Apply the CSS style sheet to the navigation toolbar
        navigation_toolbar.setStyleSheet(style_sheet)


        # Set the desired size for the toolbar
        navigation_toolbar.setFixedHeight(40)  # Set the height (adjust as needed)
        navigation_toolbar.setFixedWidth(400)  # Set the width (adjust as needed)

        # Set the initial position of the toolbar
        navigation_toolbar.move(800, 0)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        self.lambda1_text.setEnabled(False)
        self.lambda1_input.setEnabled(False)
        self.lambda2_text.setEnabled(False)
        self.lambda2_input.setEnabled(False)
        self.phi.setEnabled(False)
        self.phi_input.setEnabled(False)
        self.meridienParallele_combobox.currentIndexChanged.connect(self.update_inputs_widgets_state)
        self.calculer_button.clicked.connect(self.calculer_longueur_arc)

        self.retourButton.clicked.connect(self.pagePr)
        self.retourButton.clicked.connect(MainWindow.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setWindowTitle("GeoCalc V2.0")
        icon = QIcon("background.png")
        MainWindow.setWindowIcon(icon)
        self.lambda1_text.setText(_translate("MainWindow", "λ1 : "))
        self.phi2_text.setText(_translate("MainWindow", "φ2 : "))
        self.lambda2_text.setText(_translate("MainWindow", "λ2  : "))
        self.phi.setText(_translate("MainWindow", "φ : "))
        self.titre.setText(_translate("MainWindow", "Calcul du longueur d\'arc sur ellipsoide/ Calcul du surface"))
        self.resultat_text.setText(_translate("MainWindow", "Longueur d'arc du Méridien(Km) : "))
        self.phi1_text.setText(_translate("MainWindow", "φ1 : "))
        self.meridienParallele_combobox.setItemText(0, _translate("MainWindow", "Longueur d'arc du Méridien"))
        self.meridienParallele_combobox.setItemText(1, _translate("MainWindow", "Longueur d'arc du Premier Vertical"))
        self.meridienParallele_combobox.setItemText(2, _translate("MainWindow", "Calcul de surface sur l’ellipsoïde "))
        self.longueur_ar_text.setText(_translate("MainWindow", "Calculer : "))
        self.calculer_button.setText(_translate("MainWindow", "Calculer"))
        self.retourButton.setText(_translate("MainWindow", "Retour"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LongueurArcSurface()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
