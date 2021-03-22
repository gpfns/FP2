from flask import Flask, jsonify
app=Flask(__name__)

@app.route('/bestcrop')
def best_crop():
    return 'best crop'

@app.route('/add/<int:a>/<int:b>')
def add_nums(a,b):
    return a+b

@app.route('/find_best/<float:temp>/<float:hum>/<float:ph>/<float:rf>')
def find_best(temp,hum,ph,rf):
    return jsonify({'Temparature':temp,
        'Humidity':hum,
                    'pH':ph,
                    'Rainfall':rf})
app1.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
