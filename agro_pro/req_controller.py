from flask import jsonify, render_template, request, redirect, url_for
from collections import Counter
from agro_pro.get_models import grab
from statistics import mode
from agro_pro import app
import requests
import json
import pickle
from agro_pro.api_tools2 import huf_basic_predict_w_ph as b1, huf_basic_predict_wo_ph as b2
from agro_pro.test1 import get_climate_by_lat_long
from agro_pro.test1 import get_forecast_by_lat_long
from agro_pro.forms import GetForecastForm, GetClimateForm


@app.route('/')
def home_page():
    return render_template("home_page.html")


@app.route('/get_crop_lat_long', methods=['GET', 'POST'])
def get_climate_by_lat_long_org():
    form = GetClimateForm()
    sample = 'Tirupati - 13.6288° N, 79.4192° E\n'
    sample += 'Guntur - 16.3067° N, 80.4365° E\n'
    sample += 'Bangalore - 12.9716° N, 77.5946° E\n\n'

    if form.validate_on_submit():
        latitude = form.lat.data
        longitude = form.lon.data
        sample += get_climate_by_lat_long(latitude, longitude)
    elif request.method == "GET":
        if request.args.get('lat', ''):
            latitude = request.args.get('lat')
            longitude = request.args.get('lon')
            sample += get_climate_by_lat_long(latitude, longitude)

    return render_template('simple_data_display.html', display_text=sample, form=form)


@app.route('/forecast', methods=['GET', 'POST'])
def get_forecast_data():
    form = GetForecastForm()
    sample = 'Tirupati - 13.6288° N, 79.4192° E\n'
    sample += 'Guntur - 16.3067° N, 80.4365° E\n'
    sample += 'Bangalore - 12.9716° N, 77.5946° E\n\n'

    if form.validate_on_submit():
        latitude = form.lat.data
        longitude = form.lon.data
        sample += get_forecast_by_lat_long(latitude, longitude)
    elif request.method == "GET":
        if request.args.get('lat', ''):
            latitude = request.args.get('lat')
            longitude = request.args.get('lon')
            sample += get_forecast_by_lat_long(latitude, longitude)

    return render_template('simple_data_display.html', display_text=sample, form=form)


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
        ip1 = [[t, h, r]]
        return b2(ip1)
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
        ip1 = [[t, h, p, r]]
        return b1(ip1)
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
    lat = request.args.get('lat',1)
    lon = request.args.get('lon',1)
    ph = request.args.get('ph_soil',1)
    rainfall = request.args.get('rainfall',1)
    land = request.args.get('area_sq',1)
    nitro = request.args.get('N',1)
    pho = request.args.get('P',1)
    pot = request.args.get('K',1)
    inp = [list(map(float, [nitro, pho, pot, lat,lon, ph, rainfall]))]

    op = list()
    for i in range(11, 22):
        j = pickle.load(open('ml2/op_npk/file' + str(i) + '.pkl', 'rb'))
        op.append(j.predict(inp).tolist()[0])
    op=str(op)
    return op+"<br> <br>"+'/bestcrop?lat=&lon=&ph_soil&rainfall=&area_sq=&N=&P=&K='
