import pickle
import requests
from agro_pro.utility_classes import Current


def fun_market_price_data():
    l1 = ['Rice', 'Wheat', 'Atta(Wheat)', 'Gram Dal', 'Tur / Arhar Dal', 'Urad Dal', 'Moong Dal', 'Masoor Dal',
          'Sugar', 'Milk', 'Groundnut Oil(Packed)', 'Mustard Oil(Packed)', 'Vanaspati(Packed)', 'Soya Oil(Packed)',
          'Sunflower Oil(Packed)', 'Palm Oil(Packed)', 'Gur', 'Tea Loose', 'Salt Pack(Iodised)', 'Potato', 'Onion',
          'Tomato']


def api_h_crop_prediction_b_w(l1, l2, ph, rf, land):
    temp, hum = get_th_w_ll(l1, l2)
    inp = [list(map(float, [temp, hum, ph, rf]))]
    op = huf_basic_predict_w_ph(inp)
    return """<html>
      <body>
      <h3> Optimal Crop to Grow is <b> {0} </b> </h3>
      <h3> Estimated Profit is : {1}   </h3>
      <h2> Government Minimum Support Price is Available @ {2}/quintal </h2>
      <br>
      </body>""".format(op, "62000", "7300")


def api_h_crop_prediction_b_wo(l1, l2, rf, land):
    temp, hum = get_th_w_ll(l1, l2)
    inp = [list(map(float, [temp, hum, rf]))]
    op = huf_basic_predict_wo_ph(inp)
    return """<html>
      <body>
      <h3> Optimal Crop to Grow is <b> {0} </b> </h3>
      <h3> Estimated Profit is : {1}   </h3>
      <h2> Government Minimum Support Price is Available @ {2}/quintal </h2>
      <br>
      </body>""".format(op, "62000", "7300")


def api_h_crop_prediction_a(l1, l2, ph, rf, land, nitro, pho, pot):
    return """<html>
      <body>
      <h3> Optimal Crop to Grow is <b> {0} </b> </h3>
      <h3> Estimated Profit is : {1}   </h3>
      <h2> Government Minimum Support Price is Available @ {2}/quintal </h2>
      <br>
      </body>""".format("Wheat", "62000", "7300")


def huf_basic_predict_w_ph(inp):
    op = '\n'
    for i in range(1, 9):
        j = pickle.load(open('ml2/w_ph/file' + str(i) + '.pkl', 'rb'))
        op += str(j.predict(inp).tolist()) + '\n'
    return op


def huf_basic_predict_wo_ph(inp):
    op = '\n'
    for i in range(1, 8):
        j = pickle.load(open('ml2/wo_ph/file' + str(i) + '.pkl', 'rb'))
        op += str(j.predict(inp).tolist()) + '\n'
    return op


def get_th_w_ll(lat, lon):
    parameters = {
        'key': '6a95b306f1334a3a87c190139212005',
        'q': str(lat) + ',' + str(lon),
        'aqi': 'no'
    }
    url1 = 'http://api.weatherapi.com/v1/current.json'
    response = requests.get(url1, params=parameters)
    data = response.json()
    current = data['current']
    current = Current(current_data=current)
    return current.get_temp(), current.get_humid()
