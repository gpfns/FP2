from agro_pro import app
from flask import jsonify, render_template, request, redirect, url_for
from agro_pro.api_tools import api_test_tool, api_get_climate_by_lat_long, api_get_forecast_by_lat_long


@app.route('/api_test')
def cont_fun_api_test():
    a1 = request.args['lat']
    a2 = request.args['lon']
    return api_test_tool(a1, a2)


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
