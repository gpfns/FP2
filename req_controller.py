import os
from flask import Flask, jsonify,render_template
from get_models import grab
app=Flask(__name__)

@app.route('/bestcrop')
def best_crop():
    return 'best crop'

@app.route('/')
def home_page():
    return render_template("home_page.html")

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
@app.route('/predict/<temp>/<hum>/<rf>')
def predict_best(temp,hum,rf,ph=None):
    if ph is None:
        t,h,r=tuple(map(float,[temp,hum,rf]))
        kpc=pc[1]
        d1={}
        k1=1
        ip=[[t,h,r]]
        for i in kpc[0]:
            d1['DT'+str(k1)]=i.predict(ip).tolist()
            k1+=1
        k1=1    
        for i in kpc[2]:
            d1['RFC'+str(k1)]=i.predict(ip).tolist()
            k1+=1
        d1['NBC']=kpc[1].predict(ip).tolist()
        return jsonify(d1)
    else:    
        t,h,p,r = tuple(map(float,[temp,hum,ph,rf]))
        kpc=pc[0]
        d1={}
        k1=1
        ip=[[t,h,p,r]]
        for i in kpc[0]:
            d1['DT'+str(k1)]=i.predict(ip).tolist()
            k1+=1
        k1=1    
        for i in kpc[2]:
            d1['RFC'+str(k1)]=i.predict(ip).tolist()
            k1+=1
        d1['NBC']=kpc[1].predict(ip).tolist()    
        
        return jsonify(d1)

    
@app.route('/predict1',methods=['GET'])
def predict_best1():
    t,h,r=request.args.get('temp'),request.args.get('hum'),request.args.get('rain') 
    kpc=pc[1]
    d1={}
    k1=1
    ip=[[t,h,r]]
    """
    for i in kpc[0]:
        d1['DT'+str(k1)]=i.predict(ip).tolist()
        k1+=1
    k1=1    
    for i in kpc[2]:
        d1['RFC'+str(k1)]=i.predict(ip).tolist()
        k1+=1
    """    
    d1['NBC']=kpc[1].predict(ip).tolist()
    s1 = str(d1['NBC'])
    return render_template('home_page.html',best_predicted_crop=s1)
    
pc = grab()    
app.run(debug=True,host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
