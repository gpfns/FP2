from flask import jsonify, render_template, request, redirect, url_for
from collections import Counter
from agro_pro.get_models import grab
from statistics import mode
from agro_pro import app
import requests
import json
from agro_pro.test1 import get_climate_by_lat_long
from agro_pro.test1 import get_forecast_by_lat_long


@app.route('/')
def home_page():
    return render_template("home_page.html")


@app.route('/get_crop_lat_long/<float:latitude>/<float:longitude>', methods=['GET', 'POST'])
def get_climate_by_lat_long_org(latitude, longitude):
    sample = get_climate_by_lat_long(latitude, longitude)
    return render_template('simple_data_display.html', display_text=sample)


@app.route('/forecast/<float:latitude>/<float:longitude>', methods=['GET', 'POST'])
@app.route('/forecast/<float:latitude>/<float:longitude>/<int:days>', methods=['GET', 'POST'])
def get_forecast_data(latitude, longitude, days=7):
    sample = 'Tirupati - 13.6288° N, 79.4192° E'
    sample += 'Guntur - 16.3067° N, 80.4365° E'
    sample += 'Banglore - 12.9716° N, 77.5946° E'
    sample += '\n'
    sample += get_forecast_by_lat_long(latitude, longitude, days)
    return render_template('simple_data_display.html', display_text=sample)


@app.route('/add/<int:a>/<int:b>')
def add_nums(a, b):
    return jsonify({'add_res': a + b})


@app.route('/find_best/<temp>/<hum>/<rf>/<ph>')
def find_best(temp, hum, rf, ph=None):
    if ph is None:
        return jsonify({'Temparature': temp,
                        'Humidity': hum,
                        'Rainfall': rf})
    else:
        temp, hum, ph, rf = tuple(map(float, [temp, hum, ph, rf]))
        return jsonify({'Temparature': temp,
                        'Humidity': hum,
                        'pH': ph,
                        'Rainfall': rf})


@app.route('/predict/<temp>/<hum>/<rf>/<ph>')
@app.route('/predict/<temp>/<hum>/<rf>')
def predict_best(temp, hum, rf, ph=None):
    if ph is None:
        t, h, r = tuple(map(float, [temp, hum, rf]))
        kpc = pc[1]
        d1 = {}
        k1 = 1
        ip = [[t, h, r]]
        for i in kpc[0]:
            d1['DT' + str(k1)] = i.predict(ip).tolist()
            k1 += 1
        k1 = 1
        for i in kpc[2]:
            d1['RFC' + str(k1)] = i.predict(ip).tolist()
            k1 += 1
        d1['NBC'] = kpc[1].predict(ip).tolist()
        l2 = []
        for i in d1:
            l2.extend(d1[i])
        d1['Crop'] = mode(l2)
        d2 = Counter(l2)
        d1.update(d2)
        return jsonify(d1)
    else:
        t, h, p, r = tuple(map(float, [temp, hum, ph, rf]))
        kpc = pc[0]
        d1 = {}
        k1 = 1
        ip = [[t, h, p, r]]
        for i in kpc[0]:
            d1['DT' + str(k1)] = i.predict(ip).tolist()
            k1 += 1
        k1 = 1
        for i in kpc[2]:
            d1['RFC' + str(k1)] = i.predict(ip).tolist()
            k1 += 1
        d1['NBC'] = kpc[1].predict(ip).tolist()
        l2 = []
        for i in d1:
            l2.extend(d1[i])
        d1['Crop'] = mode(l2)
        d2 = Counter(l2)
        d1.update(d2)
        return jsonify(d1)


@app.route('/predict1', methods=['GET'])
def predict_best1():
    t, h, r = request.args.get('temp'), request.args.get('hum'), request.args.get('rain')
    t, h, r = tuple(map(float, [t, h, r]))
    kpc = pc[1]
    d1 = {}
    k1 = 1
    ip = [[t, h, r]]
    for i in kpc[0]:
        d1['DT' + str(k1)] = i.predict(ip).tolist()
        k1 += 1
    k1 = 1
    for i in kpc[2]:
        d1['RFC' + str(k1)] = i.predict(ip).tolist()
        k1 += 1
    d1['NBC'] = kpc[1].predict(ip).tolist()
    s1 = str(d1['NBC'])
    l2 = []
    for i in d1:
        l2.extend(d1[i])
    s1 = mode(l2)
    return render_template('home_page.html', best_predicted_crop=s1)


pc = grab()
# pc = ['m1']

# app.run(debug=True,host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

@app.route('/bestcrop')
def best_crop():
    return 'best crop'
