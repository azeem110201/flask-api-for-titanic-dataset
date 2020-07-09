import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
from flask import Flask,request,jsonify


def predication(Pclass,Age,SibSp,Fare):
    output = {'output_predication':0}

    x_input = np.array([Pclass,Age,SibSp,Fare]).reshape(1,4)
    filename = 'model.pkl'
    pred = pickle.load(open(filename,'rb'))
    output['output_predication'] = pred.predict(x_input)[0]

    some_res = int(output['output_predication'])

    print(some_res)
    return some_res

app = Flask(__name__)    

@app.route('/')
def home():
    return 'In home page'

@app.route('/api',methods=['GET']) 
def predication_of_model():

    body = request.get_data()
    header = request.headers
    try:
        Pclass = int(request.args['Pclass'])
        Age = int(request.args['Age'])
        SibSp = int(request.args['SibSp'])
        Fare = int(request.args['Fare'])

        if Pclass != None and Age != None and SibSp != None and Fare != None:
            res = predication(Pclass,Age,SibSp,Fare)

        else:
            res = {
                'success':False,
                'message':'imputed data is not correct'
            }    
   
    except:
        res = {
                'success':False,
                'message':'imputed data is not correct'
        }

    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True,port=1234)         
        


          