import os
from flask import Flask, jsonify,render_template,request
from collections import Counter
from get_models import grab
from statistics import mode
app=Flask(__name__)

@app.route('/bestcrop')
def best_crop():
    return 'best crop'

@app.route('/')
def home_page():
    return render_template("home_page.html")

@app.route('/n/<int:a>/<int:b>')
def game_of_nim(a,b):
    l1=[]
    with open("nim/n.txt") as file:
    	for each in file:
            l1.append(int(each))
    l1[a]-=b
    update_nim_file(l1)
    s1=''
    for j in l1:
        s1+=j*'\t|\t'+'\t'+str(j)
        s1+='<br>'
    return s1    

@app.route('/nv')
def game_of_nim_view():
    l1=[]
    with open("nim/n.txt") as file:
    	for each in file:
            l1.append(int(each))
    s1=''
    for j in l1:
        s1+=j*'\t|\t'+(7-j)*'&nbsp'+str(j)
        s1+='<br>'
    return s1    




def update_nim_file(l1):
    file = open('nim/n.txt','w')
    l1=list(map(str,l1))
    file.write('\n'.join(l1))
    file.close()
    

@app.route('/nr')
def game_of_nim_reset():
    file = open('nim/n.txt','w')
    file.write("1\n3\n5\n7")
    file.close()
    return "you can start your new game , n/row/number_of_matches_to_be_removed"


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
        l2=[]
        for i in d1:
            l2.extend(d1[i])
        d1['Crop']=mode(l2)
        d2=Counter(l2)
        d1.update(d2)
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
        l2=[]
        for i in d1:
            l2.extend(d1[i])
        d1['Crop']=mode(l2)
        d2=Counter(l2)
        d1.update(d2)
        return jsonify(d1)

    
@app.route('/predict1',methods=['GET'])
def predict_best1():
    t,h,r=request.args.get('temp'),request.args.get('hum'),request.args.get('rain') 
    t,h,r=tuple(map(float,[t,h,r]))
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
    s1 = str(d1['NBC'])
    l2=[]
    for i in d1:
        l2.extend(d1[i])
    s1=mode(l2)
    return render_template('home_page.html',best_predicted_crop=s1)
    
pc = grab()    
app.run(debug=True,host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
