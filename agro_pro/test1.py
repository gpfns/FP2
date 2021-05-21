import requests
import json


def get_forecast_by_lat_long(latitude, longitude, no_of_days):
    output = ''
    parameters = {
        'key': '6a95b306f1334a3a87c190139212005',
        'q': str(latitude) + ',' + str(longitude),
        'aqi': 'no',
        'alerts': 'no',
        'days': no_of_days
    }
    url1 = 'http://api.weatherapi.com/v1/forecast.json'
    response = requests.get(url1, params=parameters)
    data = response.json()
    # output += str(data)
    output += '\n'
    # output += jp(data)
    output += '\n'
    output += fun_parse_future_forecast(data)
    return output


def get_climate_by_lat_long(latitude, longitude):
    output = ''
    parameters = {
        'key': '6a95b306f1334a3a87c190139212005',
        'q': str(latitude) + ',' + str(longitude),
        'aqi': 'no'
    }
    url1 = 'http://api.weatherapi.com/v1/current.json'
    response = requests.get(url1, params=parameters)
    data = response.json()
    # output += str(data)
    # output += '\n'
    # output += jp(data)
    output += '\n'
    output += fun_parse_climate(data)
    return output


def fun_parse_climate(data):
    output = ''
    location = data['location']
    output += b_parse_location(location)
    current = data['current']
    output += b_parse_current(current)

    return output


def fun_parse_future_forecast(data):
    output = ''
    location = data['location']
    output += b_parse_location(location)
    output += '\n'

    current = data['current']
    output += b_parse_current(current)
    output += '\n'

    forecast_data = data['forecast']['forecastday']
    output += b_parse_forecast_days(forecast_data)

    # forecast_alerts = data['forecast']['alerts']

    return output


def b_parse_location(data):
    s1 = ""
    s1 += "Selected Place : " + data['name'] + '\n'
    s1 += "Region : " + data['region'] + '\n'
    s1 += "Country : " + data['country'] + '\n'
    s1 += "Latitude : " + str(data['lat']) + '\n'
    s1 += "Longitude : " + str(data['lon']) + '\n'
    s1 += "Local Time : " + data['localtime'] + '\n'

    return s1


def b_parse_current(data):
    s1 = ""
    s1 += "Temperature : " + str(data['temp_c']) + '\n'
    s1 += "Humidity : " + str(data['humidity']) + '\n'
    s1 += "Condition : " + data['condition']['text'] + '\n'
    s1 += "Wind (KPH) : " + str(data['wind_kph']) + '\n'
    s1 += "Wind Direction : " + data['wind_dir'] + '\n'
    s1 += "Cloud : " + str(data['cloud']) + '\n'
    s1 += "Last Updated on : " + data['last_updated'] + '\n'

    return s1


def b_parse_forecast_days(data):
    """Input forecastday in forecast"""
    l = []
    s1 = ''
    s2 = ''
    for i in data:
        s1 += 'Date : ' + i['date']
        s1 += 'Details : ' + '\n'
        s1 += 'Maximum Temperature -' + str(i['day']['maxtemp_c']) + '\n'
        s1 += 'Minimum Temperature -' + str(i['day']['mintemp_c']) + '\n'
        s1 += 'Average Temperature -' + str(i['day']['avgtemp_c']) + '\n'
        s1 += 'Condition -' + i['day']['condition']['text'] + '\n'
        s1+='\n'
        s1 += 'Hourly Climate Details\n\n'
        for j in i['hour']:
            s1 += 'Time - ' + j['time'] + '\n'
            s1 += 'Temperature - ' + str(j['temp_c']) + '\n'
            s1 += 'Condition - ' + j['condition']['text'] + '\n'
            s1 += 'Wind (KPH) - ' + str(j['wind_kph']) + '\n'
            s1 += 'Humidity - ' + str(j['humidity']) + '\n'
            s1 += 'Cloud - ' + str(j['cloud']) + '\n'
            s1 += 'Chance of Rain (%) - ' + j['chance_of_rain'] + '\n'
            s1 += '\n'
        s1 += '\n'

    return s1


# get_climate_by_lat_long(13.6288, 79.4192)


def jp(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text
