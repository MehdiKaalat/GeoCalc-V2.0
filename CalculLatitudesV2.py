from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

import fonctions as fct
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import numpy as np


class MatplotlibCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=100):
        self.fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super(MatplotlibCanvas, self).__init__(self.fig)
        self.setParent(parent)
        self.draw_ellipsoid_and_circle()
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def draw_ellipsoid_and_circle(self):
        # Default ellipse parameters
        a_ellipse = 1
        b_ellipse = 0.8

        # Circle parameters
        radius_circle = 1

        # Coordinates for ellipse
        phi = np.linspace(0, 2 * np.pi, 100)
        x_ellipse = a_ellipse * np.cos(phi)
        y_ellipse = b_ellipse * np.sin(phi)

        # Coordinates for circle
        theta_circle = np.linspace(0, 2 * np.pi, 100)
        x_circle = radius_circle * np.cos(theta_circle)
        y_circle = radius_circle * np.sin(theta_circle)

        # Plot ellipse and circle
        self.ax.plot(x_ellipse, y_ellipse, color='red', label='Ellipse')
        self.ax.plot(x_circle, y_circle, color='blue', label='Circle')


        # Add grid
        self.ax.grid(True)

        # Draw the ellipse and circle axes
        self.ax.axhline(0, color='black', linewidth=2, linestyle='-', label='Equator')
        self.ax.axvline(0, color='black', linewidth=2, linestyle='-', label='Prime Meridian')

    def draw_angles(self, angles):
        self.ax.clear()
        self.draw_ellipsoid_and_circle()
        a_ellipse = 1
        b_ellipse = 0.8
        labels = ['$\\phi$', '$\\beta$', '$\\psi$']

        # Draw the angles at the corresponding positions on the polar plot
        for i in range(len(angles)):
            angle = angles[i]
            label = labels[i]
            if i == 0:
                x = (a_ellipse ** 2 * np.cos(angle)) / np.sqrt(
                    a_ellipse ** 2 * (np.cos(angle)) ** 2 + b_ellipse ** 2 * (np.sin(angle)) ** 2)
                y = (b_ellipse ** 2 * np.sin(angle)) / np.sqrt(
                    a_ellipse ** 2 * (np.cos(angle)) ** 2 + b_ellipse ** 2 * (np.sin(angle)) ** 2)
                distance_A = np.arcsin(np.cos(angles[1]) * np.sin(a_ellipse))
                distance_C = np.arcsin((np.sin(distance_A)*np.sin(angles[2]))/np.cos(angles[2]))
                distance_D = np.arcsin((np.cos(angle)*np.sin(distance_C))/np.sin(angle))
                distance_phi = distance_A - distance_D

                self.ax.plot([distance_phi, x], [0, y], color='red', linestyle='--')
                # Draw the angle marker
                self.ax.plot(x, y, marker='o', color='red', linestyle='None', markersize=7, label=label)
            elif i == 1:
                # Calculate the coordinates for the angle and label
                x = a_ellipse*np.cos(angle)
                y = a_ellipse*np.sin(angle)
                # Draw lines from the center to each angle
                self.ax.plot([0, x], [0, y], color='blue', linestyle='--')
                # Draw the angle marker
                self.ax.plot(x, y, marker='o', color='blue', linestyle='None', markersize=7, label=label)
            elif i == 2 :
                # OP = (a_ellipse/np.sqrt(1-e2*(np.sin(angle))**2)) * np.sqrt(1+(e2-2)*e2*(np.sin(angle))**2)
                E = np.sqrt(a_ellipse**2 - b_ellipse**2)
                OP = (a_ellipse/np.sqrt(1+(np.sin(angle))**2 * ((E**2) / (b_ellipse**2))))
                x = OP * np.cos(angle)
                y = OP * np.sin(angle)
                # Draw lines from the center to each angle
                self.ax.plot([0, x], [0, y], color='black', linestyle='--')
                # Draw the angle marker
                self.ax.plot(x, y, marker='x',color='black', linestyle='None', markersize=7, label=label)

            self.ax.legend(labels, loc='lower right')

        # Show the plot
        self.draw()


class calculLatitudes(object):
    def pagePr(self):
        from pageprincipale import pagePrincipale
        self.window1 = QtWidgets.QMainWindow()
        self.ui = pagePrincipale()
        self.ui.setupUi(self.window1)
        self.window1.show()
    def calcul_latitudes(self):
        a_ellipse = 1
        b_ellipse = 0.8
        try :
            if self.latitudes_combobox.currentIndex() == 0:
                phi = float(self.latitude_donnee_input.text())
                beta = fct.dePhiABeta(phi)
                psi = fct.dePhiAPsi(phi)
                self.latitude1_result.setText(str(beta))
                self.latitude2_result.setText(str(psi))

                # Visualization: Draw angles on a polar plot
                beta_affichage = fct.dePhiABeta_affichage(phi,a_ellipse, b_ellipse)
                psi_affichage = fct.dePhiAPsi_affichage(phi,a_ellipse, b_ellipse)
                angles = np.radians([phi, beta_affichage, psi_affichage])
                self.matplotlib_widget.draw_angles(angles)
            elif self.latitudes_combobox.currentIndex() == 1:
                psi = float(self.latitude_donnee_input.text())
                beta = fct.dePsiABeta(psi)
                phi = fct.dePsiAPhi(psi)
                self.latitude1_result.setText(str(beta))
                self.latitude2_result.setText(str(phi))

                # Visualization: Draw angles on a polar plot
                beta_affichage = fct.dePsiABeta_affichage(psi, a_ellipse, b_ellipse)
                phi_affichage = fct.dePsiAPhi_affichage(psi, a_ellipse, b_ellipse)

                angles = np.radians([phi_affichage, beta_affichage, psi])
                self.matplotlib_widget.draw_angles(angles)
            elif self.latitudes_combobox.currentIndex() == 2:
                beta = float(self.latitude_donnee_input.text())
                phi = fct.deBetaAPhi(beta)
                psi = fct.deBetaAPsi(beta)
                self.latitude1_result.setText(str(phi))
                self.latitude2_result.setText(str(psi))

                # Visualization: Draw angles on a polar plot
                psi_affichage = fct.deBetaAPsi_affichage(psi, a_ellipse, b_ellipse)
                phi_affichage = fct.deBetaAPhi_affichage(psi, a_ellipse, b_ellipse)
                angles = np.radians([phi_affichage, beta, psi_affichage])
                self.matplotlib_widget.draw_angles(angles)
        except:
            QMessageBox.critical(MainWindow, 'Erreur',
                                 'Une erreur s\'est produite, vérifier les valeurs que vous avez entré.')
    def update_inputs_widgets_state(self, index):
        self.latitude_donnee_input.clear()
        self.latitude1_result.clear()
        self.latitude2_result.clear()
        if index == 0:
            self.latitude_donnee.setText("Latitude géodésique φ(deg) : ")
            self.latitude1_text.setText("Latitude réduite β(deg)  : ")
            self.latitude2_text.setText("Latitude géocentrique Ψ(deg) : ")
        if index == 1:
            self.latitude_donnee.setText("Latitude géocentrique Ψ(deg) : ")
            self.latitude1_text.setText("Latitude réduite β(deg)  : ")
            self.latitude2_text.setText("Latitude géodésique φ(deg) : ")
        if index == 2:
            self.latitude_donnee.setText("Latitude réduite β(deg)  : ")
            self.latitude2_text.setText("Latitude géocentrique Ψ(deg) : ")
            self.latitude1_text.setText("Latitude géodésique φ(deg) : ")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
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

        self.latitude1_text = QtWidgets.QLabel(self.centralwidget)
        self.latitude1_text.setGeometry(QtCore.QRect(10, 300, 251, 31))
        self.latitude1_text.setStyleSheet("font-size : 16px;\n"
"font-weight : bold;")
        self.latitude1_text.setObjectName("latitude1_text")
        self.latitude2_text = QtWidgets.QLabel(self.centralwidget)
        self.latitude2_text.setGeometry(QtCore.QRect(10, 360, 251, 31))
        self.latitude2_text.setStyleSheet("font-size : 16px;\n"
"font-weight : bold;")
        self.latitude2_text.setObjectName("latitude2_text")
        self.titre = QtWidgets.QLabel(self.centralwidget)
        self.titre.setGeometry(QtCore.QRect(240, 20, 401, 41))
        self.titre.setStyleSheet("font-size : 20px;\n"
"font-weight : bold;")
        self.titre.setObjectName("titre")
        self.latitude_donnee = QtWidgets.QLabel(self.centralwidget)
        self.latitude_donnee.setGeometry(QtCore.QRect(10, 160, 271, 31))
        self.latitude_donnee.setStyleSheet("font-size : 16px;\n"
"font-weight : bold;")
        self.latitude_donnee.setObjectName("latitude_donnee")
        self.latitudes_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.latitudes_combobox.setGeometry(QtCore.QRect(290, 90, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(9)
        self.latitudes_combobox.setFont(font)
        self.latitudes_combobox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.latitudes_combobox.setStyleSheet("font-size : 16px;\n"
"font-weight:bold;")
        self.latitudes_combobox.setObjectName("latitudes_combobox")
        self.latitudes_combobox.addItem("")
        self.latitudes_combobox.addItem("")
        self.latitudes_combobox.addItem("")
        self.calculer_text = QtWidgets.QLabel(self.centralwidget)
        self.calculer_text.setGeometry(QtCore.QRect(10, 90, 211, 41))
        self.calculer_text.setStyleSheet("font-size : 16px;\n"
"font-weight : bold;")
        self.calculer_text.setObjectName("calculer_text")
        self.calculer_button = QtWidgets.QPushButton(self.centralwidget)
        self.calculer_button.setGeometry(QtCore.QRect(300, 230, 171, 41))
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
        self.calculer_button.setObjectName("calculer_button")
        self.latitude_donnee_input = QtWidgets.QLineEdit(self.centralwidget)
        self.latitude_donnee_input.setGeometry(QtCore.QRect(320, 150, 301, 41))
        self.latitude_donnee_input.setObjectName("latitude_donnee_input")
        self.latitude_donnee_input.setStyleSheet("background-color : #19A7CE;\n"
                                      "border: none ;\n"
                                      "border-radius : 10px;\n"
                                      "color : white;\n"
                                      "padding-left : 5px;\n"
                                      "")
        self.latitude1_result = QtWidgets.QLabel(self.centralwidget)
        self.latitude1_result.setGeometry(QtCore.QRect(320, 300, 271, 41))
        self.latitude1_result.setStyleSheet("font-size : 16px;\n"
"font-weight : bold;")
        self.latitude1_result.setText("")
        self.latitude1_result.setObjectName("latitude1_result")
        self.latitude2_result = QtWidgets.QLabel(self.centralwidget)
        self.latitude2_result.setGeometry(QtCore.QRect(320, 350, 271, 41))
        self.latitude2_result.setStyleSheet("font-size : 16px;\n"
"font-weight : bold;")
        self.latitude2_result.setText("")
        self.latitude2_result.setObjectName("latitude2_result")
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

        self.latitudes_combobox.currentIndexChanged.connect(self.update_inputs_widgets_state)
        self.calculer_button.clicked.connect(self.calcul_latitudes)
        self.retourButton.clicked.connect(self.pagePr)
        self.retourButton.clicked.connect(MainWindow.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setWindowTitle("GeoCalc V2.0")

        icon = QIcon("background.png")
        MainWindow.setWindowIcon(icon)
        self.latitude1_text.setText(_translate("MainWindow", "Latitude réduite β(deg)  : "))
        self.latitude2_text.setText(_translate("MainWindow", "Latitude géocentrique Ψ(deg) : "))
        self.titre.setText(_translate("MainWindow", "Calcul des latitudes φ, β, Ψ"))
        self.latitude_donnee.setText(_translate("MainWindow", "Latitude géodésique φ(deg) : "))
        self.latitudes_combobox.setItemText(0, _translate("MainWindow", "Ψ et β à partir de φ"))
        self.latitudes_combobox.setItemText(1, _translate("MainWindow", "φ et β à partir de Ψ"))
        self.latitudes_combobox.setItemText(2, _translate("MainWindow", "φ et Ψ à partir de β "))
        self.calculer_text.setText(_translate("MainWindow", "Calculer :"))
        self.calculer_button.setText(_translate("MainWindow", "Calculer"))
        self.retourButton.setText(_translate("MainWindow", "Retour"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = calculLatitudes()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
