import requests


def api_test_tool(lat, lon):
    return """<html>
    <body>
    <h3> Latitude : {0} </h3>
    <h3> Longitude :{1}   </h3>
    <h2> Formatted Text </h2>
    <br>
    <b> Amma baboi </b>
    <i> Italics mari </i>
    </body>""".format(lat, lon)


def api_get_forecast_by_lat_long(latitude, longitude, no_of_days=7):
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
    output = api_fun_parse_future_forecast(data)
    return output


def api_get_climate_by_lat_long(latitude, longitude):
    parameters = {
        'key': '6a95b306f1334a3a87c190139212005',
        'q': str(latitude) + ',' + str(longitude),
        'aqi': 'no'
    }
    url1 = 'http://api.weatherapi.com/v1/current.json'
    response = requests.get(url1, params=parameters)
    data = response.json()
    output = api_fun_parse_climate(data)
    return output


def api_fun_parse_climate(data):
    output = ''
    location = data['location']
    output += b_parse_location(location)
    current = data['current']
    output += b_parse_current(current)

    return output


def api_fun_parse_future_forecast(data):
    output = ''
    location = data['location']
    output += b_parse_location(location)
    output += '<br>'

    current = data['current']
    output += b_parse_current(current)
    output += '<br>'

    forecast_data = data['forecast']['forecastday']
    output += b_parse_forecast_days(forecast_data)

    # forecast_alerts = data['forecast']['alerts']

    return output


def b_parse_location(data):
    s1 = "<h2> Location Details </h2><p>"
    s1 += "<b>Selected Place : </b>" + data['name'] + '<br>'
    s1 += "<b>Region : </b>" + data['region'] + '<br>'
    s1 += "<b>Country : </b>" + data['country'] + '<br>'
    s1 += "<b>Latitude : </b>" + str(data['lat']) + '<br>'
    s1 += "<b>Longitude : </b>" + str(data['lon']) + '<br>'
    s1 += "<b>Local Time : </b>" + data['localtime'] + '<br>'
    s1 += '</p>'

    return s1


def b_parse_current(data):
    s1 = "<h2> Current Climate Details </h2><p>"
    s1 += "<b>Temperature : </b>" + str(data['temp_c']) + '<br>'
    s1 += "<b>Humidity : </b>" + str(data['humidity']) + '<br>'
    s1 += "<b>Condition : </b>" + data['condition']['text'] + '<br>'
    s1 += "<b>Wind (KPH) : </b>" + str(data['wind_kph']) + '<br>'
    s1 += "<b>Wind Direction : </b>" + data['wind_dir'] + '<br>'
    s1 += "<b>Cloud : </b>" + str(data['cloud']) + '<br>'
    s1 += "<b>Last Updated on : </b>" + data['last_updated'] + '<br>'
    s1 += '</p>'

    return s1


def b_parse_forecast_days(data):
    """Input forecastday in forecast"""
    # l = []
    s1 = "<h2> Weather Forecast Data </h2><br><p>"
    # s2 = ''
    for i in data:
        s1 += 'Date : ' + i['date'] + '<br>'
        s1 += '<big>Details : </big>' + '<br>'
        s1 += 'Maximum Temperature : ' + str(i['day']['maxtemp_c']) + '<br>'
        s1 += 'Minimum Temperature : ' + str(i['day']['mintemp_c']) + '<br>'
        s1 += 'Average Temperature : ' + str(i['day']['avgtemp_c']) + '<br>'
        s1 += 'Condition -' + i['day']['condition']['text'] + '<br>'
        s1 += '<br>'
        s1 += '<big>Hourly Climate Details</big><br><br>'
        for j in i['hour']:
            s1 += 'Time : ' + j['time'] + '<br>'
            s1 += 'Temperature : ' + str(j['temp_c']) + '<br>'
            s1 += 'Condition : ' + j['condition']['text'] + '<br>'
            s1 += 'Wind (KPH) : ' + str(j['wind_kph']) + '<br>'
            s1 += 'Humidity : ' + str(j['humidity']) + '<br>'
            s1 += 'Cloud : ' + str(j['cloud']) + '<br>'
            s1 += 'Chance of Rain (%) : ' + j['chance_of_rain'] + '<br>'
            s1 += '<br>'
        s1 += '<br>'

    s1 += '</p>'

    return s1
