from agro_pro import app
from flask import jsonify, render_template, request, redirect, url_for
from agro_pro.api_tools import api_test_tool, api_get_climate_by_lat_long, api_get_forecast_by_lat_long
from agro_pro.api_tools2 import api_h_crop_prediction_a as adv1, api_h_crop_prediction_b as basic


@app.route('/api_test')
def cont_fun_api_test():
    a1 = request.args['lat']
    a2 = request.args['lon']
    return api_test_tool(a1, a2)


@app.route('/api_how_to_use')
def cont_fun_api_how_to_use():
    return render_template('sub_1/how_to_use.html')


@app.route('/api_crop_prediction_basic')
def cont_api_crop_prediction_b():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    ph = request.args.get('ph_soil')
    rainfall = request.args.get('rainfall')
    land = request.args.get('area_sq')
    return basic(lat, lon, ph, rainfall, land)


@app.route('/api_crop_prediction_advanced')
def cont_api_crop_prediction_a():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    ph = request.args.get('ph_soil')
    rainfall = request.args.get('rainfall')
    land = request.args.get('area_sq')
    nitro = request.args.get('N')
    pho = request.args.get('P')
    pot = request.args.get('K')
    return adv1(lat, lon, ph, rainfall, land, nitro, pho, pot)


@app.route('/api_experimental')
def cont_fun_api_experimental():
    code = request.args['code']
    code = int(code)
    if code == 1:
        return render_template('sub_1/table_msp.html')
    elif code == 2:
        return render_template('sub_1/test_1.html')

    return "Hi"


@app.route('/api_weather_forecast')
def cont_fun_api_weather_forecast():
    a1 = request.args['lat']
    a2 = request.args['lon']
    return api_get_forecast_by_lat_long(a1, a2)


@app.route('/api_climate')
def cont_fun_api_climate_details():
    a1 = request.args['lat']
    a2 = request.args['lon']
    return api_get_climate_by_lat_long(a1, a2)
