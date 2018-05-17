import sys
from PyQt5 import QtCore, QtWidgets, QtGui
import supertool.main_window_form as main_form
import supertool.calculate_ui as calc_ui
import functools

#C:\Users\nosov\venv\qtt\Scripts\pyuic5.exe my_form.ui -o my_form.py

class MainApplication(QtWidgets.QMainWindow):
    """
    Class of main window
    """
    def __init__(self):
        #инициализируем
        super(MainApplication, self).__init__()
        self.ui = main_form.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.buttom_calc.clicked.connect(self.buttom_calculate_pressed)
        self.ui.buttom_similar_file.clicked.connect(self.buttom_similar_files_pressed)
        self.ui.buttom_weather.clicked.connect(self.buttom_weather_pressed())



    def buttom_calculate_pressed(self):
        """
        Connected func for ui.bottom_calc.
        Opens a calculator window.

        :return: None
        """
        c=calc_ui.CalculateWidget()
        c.show()

    def buttom_weather_pressed(self):
        """
        Connected func for ui.bottom_calc.
        Opens a weather window.

        :return: None
        """



    def buttom_similar_files_pressed(self):
        """
        Connected func for ui.bottom_calc.
        Opens a fimilar_files window.

        :return: None
        """

def run():
    """
    Open main window.
    :return:
    """
    app = QtWidgets.QApplication(sys.argv)
    window = MainApplication()
    window.show()
    sys.exit(app.exec_())
