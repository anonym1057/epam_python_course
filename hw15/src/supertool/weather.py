import requests
import json

URL_LOCATION_REQUEST = 'https://nominatim.openstreetmap.org/search'
URL_WEATHER_FORECAST_REQUEST = 'http://api.openweathermap.org/data/2.5/forecast'
URL_CURRENT_WEATHER_REQUEST = 'http://api.openweathermap.org/data/2.5/weather'
API_KEY_WEATHER_REQUEST = 'b4a9d8e16b916107e741f1e84440c660'


def get_location_coordinates(address, url=URL_LOCATION_REQUEST):
    """
    Returns latitude and longitude from get requests url by address or error code
    Error code 200 - nothing was found

    :param address: address of the place, whose location is required
    :type adress: str
    :param url: url where the weather does  come from
    :type url: str
    :return: (str,str,str) or Error_code --  (latitude and longitude and display name)
    """
    querystring = {
        'q': address,
        'format': 'json',
    }
    # запрос
    response = requests.get(url, params=querystring)
    data = response.json()

    # ничего не нашлось
    if (len(data) == 0):
        return 200,None

    return data[0]['lat'], data[0]['lon'],data[0]['display_name']

def print_weather_forecast(lat, lon,disp_name, url=URL_WEATHER_FORECAST_REQUEST):
    """
    Print the weather forecast for the specified location

    :param lat: latitude of place
    :type lat: float
    :param lon: longitude of place
    :type lon: float
    :param url: url api
    :type url: str
    :return: None
    """
    result = get_weather(lat, lon, url)
    if result == None:
        print("Error request")
        return None
    print(f"Weather forecast in {disp_name}")
    for weather in result['list']:
        print('Date: ', weather["dt_txt"])
        print_weather(weather)
        print('---------------------------------------------')


def print_current_weather(lat, lon,disp_name, url=URL_CURRENT_WEATHER_REQUEST):
    """
    Print the current weather for the specified location

    :param lat: latitude of place
    :type lat: float
    :param lon: longitude of place
    :type lon: float
    :param url: url api
    :type url: str
    :return: None
    """
    result = get_weather(lat, lon, url)
    if result == None:
        print("Error request")
        return None

    print(f"Current weather in {disp_name}")
    print_weather(result)
    print('---------------------------------------------')


def print_weather(data):
    """
    Print the weather from json. Print type,temperature,humidity,wind for one day

    :param lat: latitude of place
    :type lat: float
    :return: None
    """
    try:
        print(
            f"\tType: {data['weather'][0]['description']}\n",
            f"\tTemperature:  {data['main']['temp']}°\n",
            f"\tHumidity: {data['main']['humidity']}\n",
            f"\tWind: {data['wind']['speed']} m/sec",
        )
    except Exception:
        raise TypeError('data invalid format')


def get_weather(lat, lon, url, api_key=API_KEY_WEATHER_REQUEST):
    """
    Get weather for location coordinates  (lan, lon) from api

    :param lat: latgitude of place
    :type lat: float
    :param lon: longitude of place
    :type lon: float
    :param url: url api
    :type url: str
    :param api_key: appid
    :type api_key: str
    :return: json or list(json) or None
    """
    try:
        lat_f = float(lat)
        lon_f = float(lon)
    except Exception as e:
        raise TypeError("Invalid format lat or lon")

    if (lat_f > 90 and lat_f < -90):
        raise ValueError("Invalid value lat. Lat is -90 < lat < 90 ")

    if (lon_f > 180 and lon_f < -180):
        raise ValueError("Invalid value lon. Lon is -180 < lon < 180 ")

    querystring = {"lat": str(lat_f),
                   "lon": str(lon_f),
                   "units": "metric",
                   "appid": api_key}

    response = requests.get(url, params=querystring)
    data = response.json()

    if int(data['cod']) != 200:
        return None

    return data
