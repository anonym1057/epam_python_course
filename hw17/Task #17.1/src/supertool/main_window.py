import sys
from PyQt5 import QtWidgets
import supertool.main_window_form as main_form
import supertool.calculate_ui as calc_ui
import supertool.weather_ui as weat_ui
import supertool.similar_files_ui as files_ui


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

        self.ui.buttom_weather.clicked.connect(self.button_weather_pressed)
        self.ui.buttom_calc.clicked.connect(self.button_calculate_pressed)
        self.ui.buttom_similar_file.clicked.connect(self.button_similar_files_pressed)

        self.w = weat_ui.WeatherWidget1()
        self.c = calc_ui.CalculateWidget()
        self.s=files_ui.SimilarFilesWidget()


    def button_calculate_pressed(self):
        """
        Connected func for ui.bottom_calc.
        Opens a calculator window.

        :return: None
        """
        self.c.show()

    def button_weather_pressed(self):
        """
        Connected func for ui.bottom_calc.
        Opens a weather window.

        :return: None
        """
        #w= weat_ui.WeatherWidget1()
        self.w.show()

    def button_similar_files_pressed(self):
        """
        Connected func for ui.bottom_calc.
        Opens a fimilar_files window.

        :return: None
        """
        self.s.show()

def run():
    """
    Open main window.
    :return:
    """
    app = QtWidgets.QApplication(sys.argv)
    window = MainApplication()
    window.show()
    sys.exit(app.exec_())

