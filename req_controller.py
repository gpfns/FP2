import os
from flask import Flask, jsonify
from get_models import grab
app=Flask(__name__)

@app.route('/bestcrop')
def best_crop():
    return 'best crop'

@app.route('/')
def home_page():
    return "<h1>Welcome ,<br> Use predict/t/h/r/ph </h1>"

@app.route('/add/<int:a>/<int:b>')
def add_nums(a,b):
    return jsonify({ 'add_res': a+b})

@app.route('/find_best/<temp>/<hum>/<rf>/<ph>')
def find_best(temp,hum,rf,ph=None):
    if ph is None:
        return jsonify({'Temparature':temp,
                        'Humidity':hum,
                         'Rainfall':rf})
    else:    
        temp,hum,ph,rf = tuple(map(float,[temp,hum,ph,rf]))
        return jsonify({'Temparature':temp,
                        'Humidity':hum,
                        'pH':ph,
                        'Rainfall':rf})
@app.route('/predict/<temp>/<hum>/<rf>/<ph>')
def predict_best(temp,hum,rf,ph=None):
    if ph is None:
        t,h,r=tuple(map(float,[temp,hum,rf]))
        kpc=pc[1]
        d1={}
        k1=1
        for i in kpc[0]:
            d1['DT'+k1]=i.predict([t,h,r])
            k1+=1
        k1=1    
        for i in kpc[2]:
            d1['RFC'+k1]=i.predict([t,h,r])
            k1+=1
        d1['NBC']=kpc[1].predict([t,h,r])    
            
        return jsonify(d1)
    else:    
        t,h,p,r = tuple(map(float,[temp,hum,ph,rf]))
        kpc=pc[0]
        d1={}
        k1=1
        for i in kpc[0]:
            d1['DT'+k1]=i.predict([t,h,p,r])
            k1+=1
        k1=1    
        for i in kpc[2]:
            d1['RFC'+k1]=i.predict([t,h,p,r])
            k1+=1
        d1['NBC']=kpc[1].predict([t,h,p,r])    
            
        return jsonify(d1)
        
pc = grab()    
app.run(debug=True,host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
