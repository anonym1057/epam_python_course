from PyQt5 import QtCore, QtWidgets, QtGui
import supertool.weather_form as wform
import supertool.table_weather_form as twform
import supertool.weather as ww



class WeatherWidget1(QtWidgets.QWidget):
    """
    Class of weather widget.
    """

    def __init__(self):
        self.curr_widget = None

        super(WeatherWidget1, self).__init__()
        self.ui = wform.Ui_WeatherWidget()
        self.ui.setupUi(self)

        self.ui.button_submit.clicked.connect(self.button_submit_pressed)

        self.clear_data_in_window()

    def button_submit_pressed(self):
        """
        Function connected with button_submin_pressed.
        Print weather
        """
        self.ui.text_weather.setReadOnly(True)
        self.setEnabled(False)

        self.print_weather(self.ui.text_weather.text())

        self.setEnabled(True)
        self.ui.text_weather.setReadOnly(False)

    def print_weather(self, address):
        """
        Print on window current weather and weather forecast
        :param address: address for witch we need to show weather
        :return: None
        """
        self.clear_data_in_window()

        # получение координат
        coordinates = ww.get_location_coordinates(address)
        # если ошибка
        if (coordinates[0] == 200):
            self.ui.label_not_foud.setVisible(True)
        else:
            # выводим место
            self.ui.label_place.setVisible(True)
            self.ui.lineEdit_place.setText(coordinates[2])
            self.ui.lineEdit_place.setVisible(True)
            # если получили, то выводим инфу
            self.print_current_weather(coordinates[0], coordinates[1])
            self.print_weather_forecast(coordinates[0], coordinates[1])

    def print_current_weather(self, lat, lon):
        """
        Print the current weather for the specified location

        :param lat: latitude of place
        :type lat: float
        :param lon: longitude of place
        :type lon: float
        :return: None
        """
        data = ww.get_weather(lat, lon, ww.URL_CURRENT_WEATHER_REQUEST)
        if data == None:
            self.ui.label_not_foud.setVisible(True)
            return

        self.ui.label_cur.setVisible(True)

        table = TableWeatherWidget("Сейчас", data['weather'][0]['description'], data['main']['temp'],
                                   data['main']['humidity'], data['wind']['speed'])
        self.ui.layout_current.addWidget(table)

    def print_weather_forecast(self, lat, lon):
        """
        Print the weather forecast for the specified location

        :param lat: latitude of place
        :type lat: float
        :param lon: longitude of place
        :type lon: float
        :return: Nonev
        """
        res = ww.get_weather(lat, lon, ww.URL_WEATHER_FORECAST_REQUEST)
        if res == None:
            self.ui.label_not_foud.setVisible(True)
            return
        self.ui.line.setVisible(True)
        self.ui.label_for.setVisible(True)
        for data in res['list']:
            table = TableWeatherWidget(data["dt_txt"], data['weather'][0]['description'], data['main']['temp'],
                                       data['main']['humidity'], data['wind']['speed'])
            current_height = self.ui.scrollAreaWidgetContents.height()
            self.ui.scrollAreaWidgetContents.setFixedHeight(current_height + table.height() + 6)
            self.ui.verticalLayout.addWidget(table)

    def clear_data_in_window(self):
        """
        Clear window to initial state

        :return:
        """
        self.ui.label_cur.setVisible(False)
        self.ui.label_for.setVisible(False)
        self.ui.label_not_foud.setVisible(False)
        self.ui.label_place.setVisible(False)
        self.ui.lineEdit_place.setVisible(False)
        self.ui.line.setVisible(False)

        # удаление всей инфы
        while self.ui.layout_current.itemAt(0):
            a = self.ui.layout_current.itemAt(0)
            a.widget().close()
            self.ui.layout_current.removeItem(a)

        while self.ui.verticalLayout.itemAt(0):
            a = self.ui.verticalLayout.itemAt(0)
            a.widget().close()
            self.ui.verticalLayout.removeItem(a)

        self.ui.scrollArea.setWidgetResizable(False)
        self.ui.scrollAreaWidgetContents.setFixedHeight(20)


class TableWeatherWidget(QtWidgets.QFrame):
    """
    Class of weather widget for a one date.
    """

    def __init__(self, date, descr='', temp='', hum='', wing=''):
        super(TableWeatherWidget, self).__init__()
        self.ui = twform.Ui_TableWeather()
        self.ui.setupUi(self)

        self.ui.text_name.setText(str(date))
        self.ui.text_descr.setText(str(descr))
        self.ui.label_2.setText(str(temp))
        self.ui.text_hum.setText(str(hum))
        self.ui.text_wing.setText(str(wing))
