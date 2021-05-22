from agro_pro import app
from flask import jsonify, render_template, request, redirect, url_for
from agro_pro.api_tools import *


@app.route('/api_test')
def fun_api_test():
    a1 = request.GET['lat']
    a2 = request.GET['lon']
    return api_test_tool(a1, a2)


@app.route('/api_weather')
def fun_api_weather_forecast():
    pass


@app.route('/api_forecast')
def fun_api_climate_details():
    pass
