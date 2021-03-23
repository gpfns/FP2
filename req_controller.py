import os
from flask import Flask, jsonify
app=Flask(__name__)

@app.route('/bestcrop')
def best_crop():
    return 'best crop'

@app.route('/add/<int:a>/<int:b>')
def add_nums(a,b):
    return jsonify({ 'add_res': a+b})

@app.route('/find_best/<temp>/<hum>/<ph>/<rf>')
def find_best(temp,hum,ph,rf):
    temp,hum,ph,rf = tuple(map(float,[temp,hum,ph,rf]))
    return jsonify({'Temparature':temp,
        'Humidity':hum,
                    'pH':ph,
                    'Rainfall':rf})
app.run(debug=True,host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
