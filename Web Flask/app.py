from flask import Flask
from flask import render_template
from flask import request
from models import dbMgr
import pandas as pd

app = Flask(__name__)

# 특정 url을 실행하겠다!
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page1')
def page():
    return render_template('page1.html')

@app.route('/modeling', methods = ['POST'])
def predict_data():
    name = request.form['name']
    gender = request.form['gender']
    age = request.form['age']
    weight = request.form['weight']
    runtime = request.form['runtime']
    runpulse = request.form['runpulse']
    rstpulse = request.form['rstpulse']
    maxpulse = request.form['max_pulse']

    data1 = [[age,weight,runtime,runpulse,rstpulse,maxpulse]]
    result = dbMgr.load_model_lasso()
    df = pd.DataFrame(data1)
    predict01 = result.predict(df)
    print(predict01)

    return render_template('page1.html', predict = predict01)

if __name__ == '__main__':
    app.run()

