import requests


def api_get_forecast_by_lat_long(latitude, longitude, no_of_days=7):
    parameters = {
        'key': '6a95b306f1334a3a87c190139212005',
        'q': str(latitude) + ',' + str(longitude),
        'aqi': 'no',
        'alerts': 'no',
        'days': no_of_days,
        'lang': 'te',
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
        'aqi': 'no',
        'lang': 'te',
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
    s1 = "<h2> స్థాన వివరాలు </h2><p>"
    s1 += "<b>ఎంచుకున్న ప్రదేశం : </b>" + data['name'] + '<br>'
    s1 += "<b>ప్రాంతం  : </b>" + data['region'] + '<br>'
    s1 += "<b>దేశం  : </b>" + data['country'] + '<br>'
    s1 += "<b>అక్షాంశం ( Latitude ) : </b>" + str(data['lat']) + '<br>'
    s1 += "<b>రేఖాంశం : </b>" + str(data['lon']) + '<br>'
    s1 += "<b>స్థానిక సమయం : </b>" + data['localtime'] + '<br>'
    s1 += '</p>'

    return s1


def b_parse_current(data):
    s1 = "<h2> ప్రస్తుత వాతావరణ వివరాలు </h2><p>"
    s1 += "<b>ఉష్ణోగ్రత : </b>" + str(data['temp_c']) + '<br>'
    s1 += "<b>తేమ : </b>" + str(data['humidity']) + '<br>'
    s1 += "<b>పరిస్థితి : </b>" + data['condition']['text'] + '<br>'
    s1 += "<b>గాలి (KPH) : </b>" + str(data['wind_kph']) + '<br>'
    s1 += "<b>పవన దిశ : </b>" + data['wind_dir'] + '<br>'
    s1 += "<b>మేఘాలు  : </b>" + str(data['cloud']) + '<br>'
    s1 += "<b>చివరిగా నవీకరించబడింది : </b>" + data['last_updated'] + '<br>'
    s1 += '</p>'

    return s1


def b_parse_forecast_days(data):
    """Input forecastday in forecast"""
    # l = []
    s1 = "<h2> వాతావరణ సూచన డేటా </h2><br><p>"
    # s2 = ''
    for i in data:
        s1 += 'తేదీ : ' + i['date'] + '<br>'
        s1 += '<big>వివరాలు : </big>' + '<br>'
        s1 += 'గరిష్ట ఉష్ణోగ్రత: : ' + str(i['day']['maxtemp_c']) + '<br>'
        s1 += 'కనిష్ట ఉష్ణోగ్రత : ' + str(i['day']['mintemp_c']) + '<br>'
        s1 += 'కనిష్ట ఉష్ణోగ్రత : ' + str(i['day']['avgtemp_c']) + '<br>'
        s1 += 'పరిస్థితి -' + i['day']['condition']['text'] + '<br>'
        s1 += '<br>'
        s1 += '<big> ప్రతి గంట వాతావరణ వివరాలు </big><br><br>'
        for j in i['hour']:
            s1 += 'సమయం : ' + j['time'] + '<br>'
            s1 += 'ఉష్ణోగ్రత : ' + str(j['temp_c']) + '<br>'
            s1 += 'పరిస్థితి : ' + j['condition']['text'] + '<br>'
            s1 += 'గాలి (KPH) : ' + str(j['wind_kph']) + '<br>'
            s1 += 'తేమ : ' + str(j['humidity']) + '<br>'
            s1 += 'మేఘాలు : ' + str(j['cloud']) + '<br>'
            s1 += 'వర్షం పడే అవకాశం (%) : ' + j['chance_of_rain'] + '<br>'
            s1 += '<br>'
        s1 += '<br>'

    s1 += '</p>'

    return s1
