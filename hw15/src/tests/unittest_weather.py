import unittest
from unittest.mock import patch


class Tests__module_weather__get_location_coordinates(unittest.TestCase):
    def test__correct_args__positive(self):
        pass

    def test__invalid_adress__not_found_location__nonpositive(self):
        pass

    def test__invalid_adress__getiing_many_locations___nonpositive(self):
        pass


class Tests__module_weather__get_weather(unittest.TestCase):
    def test__correct_args__positive(self):
        pass

    def test__invalid_format_args__nonpositive(self):
        pass

    def test__invalid_type_args_lon__nonpositive(self):
        pass

    def test__invalid_type_args_lat__nonpositive(self):
        pass

    def test__error_response__nonpositive(self):
        pass


class Tests__module_weather__print_weather(unittest.TestCase):
    def test__correct_args__positive(self):
        pass

    def test__incorrect_args__nonpositive(self):
        pass


class Tests__module_weather__print_weather_forecast(unittest.TestCase):
    def test__correct_args__positive(self):
        pass

    def test__invalid_format_args__nonpositive(self):
        pass

    def test__invalid_type_args_lon__nonpositive(self):
        pass

    def test__invalid_type_args_lat__nonpositive(self):
        pass

    def test__error_response__nonpositive(self):
        pass


class Tests__module_weather__print_current_weather(unittest.TestCase):
    def test__correct_args__positive(self):
        pass

    def test__invalid_format_args__nonpositive(self):
        pass

    def test__invalid_type_args_lon__nonpositive(self):
        pass

    def test__invalid_type_args_lat__nonpositive(self):
        pass

    def test__error_response__nonpositive(self):
        pass

if __name__=="__main__":
    unittest.main()