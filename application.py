from flask import Flask, render_template, request, redirect, url_for
import json
import requests
import urllib.request
import sys
from pandas import DataFrame as DF
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#import dash
#import dash_table
#import dash_core_components as dcc
#import dash_html_components as html
app = Flask(__name__)

#url = 'http://airsvr.run.goorm.io/api/users'
#response = urllib.request.urlopen(url).read().decode('utf-8')
#json_return = json.loads(response)
#data = DF(json_return)



@app.route('/', methods =['GET'])

#def get():
#    url = 'http://jsonsvr.run.goorm.io/api/users'
#    response = requests.get(url)
#    response.status_code
#    response.text
    
#    params = {'school': 'value1', 'class': 'value2', 'num': 'value3'}
#    res = requests.get(url, params=params)
#    return params
#    return render_template("index.html")

def root():
    parameter_dict = request.args.to_dict()
    if len(parameter_dict) == 0:
        return 'No parameter'

    parameters = ''
    for key in parameter_dict.keys():
        parameters += '{}'.format(request.args[key])
        
    #return parameters
    #return render_template("index.html", value=parameters)


    #input2 = request.form['input2']
    #print(input2)
    url = 'http://airsvr.run.goorm.io/api/users'
    response = urllib.request.urlopen(url).read().decode('utf-8')
    json_return = json.loads(response)
    data = DF(json_return)
    
    data = data.replace('매우 잘돼요', 1)
    data = data.replace('잘돼요', 1)
    data = data.replace('그저 그래요', 0)
    data = data.replace('집중이 안돼요', 0)
    
    data = data.replace('스트레스 많이 받아요', 1)
    data = data.replace('스트레스 받아요', 1)
    data = data.replace('스트레스 안 받아요', 0)
    
    
    #다중응답 카운트
    q11 = data['answer11'].str.split(', ')
    
  
    data['answer11_1']= q11.str.get(0)
    data['answer11_2']= q11.str.get(1)
    data['answer11_3']= q11.str.get(2)
    data['answer11_4']= q11.str.get(3)
    data['answer11_5']= q11.str.get(4)
    data['answer11_6']= q11.str.get(5)
    data['answer11_7']= q11.str.get(6)
    data['answer11_8']= q11.str.get(7)
    data['answer11_9']= q11.str.get(8)
    data['answer11_10']= q11.str.get(9)
    data['answer11_11']= q11.str.get(10)
    data['answer11_12']= q11.str.get(11)
    
    data = data.replace('눈이 따갑고 가려움', 1)
    data = data.replace('목이 따갑고 가려움', 1)
    data = data.replace('두통이나 어지러움', 1)
    data = data.replace('비염증상(코막힘/콧물/재채기 등)', 1)
    data = data.replace('감기', 1)
    data = data.replace('증상없음', 0)

    
    data['answer11_1']= pd.to_numeric(data['answer11_1'], errors='ignore').fillna(0)
    data['answer11_2']= pd.to_numeric(data['answer11_2'], errors='ignore').fillna(0)
    data['answer11_3']= pd.to_numeric(data['answer11_3'], errors='ignore').fillna(0)
    data['answer11_4']= pd.to_numeric(data['answer11_4'], errors='ignore').fillna(0)
    data['answer11_5']= pd.to_numeric(data['answer11_5'], errors='ignore').fillna(0)
    data['answer11_6']= pd.to_numeric(data['answer11_6'], errors='ignore').fillna(0)
    data['answer11_7']= pd.to_numeric(data['answer11_7'], errors='ignore').fillna(0)
    data['answer11_8']= pd.to_numeric(data['answer11_8'], errors='ignore').fillna(0)
    data['answer11_9']= pd.to_numeric(data['answer11_9'], errors='ignore').fillna(0)
    data['answer11_10']= pd.to_numeric(data['answer11_10'], errors='ignore').fillna(0)
    data['answer11_11']= pd.to_numeric(data['answer11_11'], errors='ignore').fillna(0)
    data['answer11_12']= pd.to_numeric(data['answer11_12'], errors='ignore').fillna(0)

    data['answer11_1']= pd.to_numeric(data['answer11_1'], errors='coerce').fillna(1)
    data['answer11_2']= pd.to_numeric(data['answer11_2'], errors='coerce').fillna(1)
    data['answer11_3']= pd.to_numeric(data['answer11_3'], errors='coerce').fillna(1)
    data['answer11_4']= pd.to_numeric(data['answer11_4'], errors='coerce').fillna(1)
    data['answer11_5']= pd.to_numeric(data['answer11_5'], errors='coerce').fillna(1)
    data['answer11_6']= pd.to_numeric(data['answer11_6'], errors='coerce').fillna(1)
    data['answer11_7']= pd.to_numeric(data['answer11_7'], errors='coerce').fillna(1)
    data['answer11_8']= pd.to_numeric(data['answer11_8'], errors='coerce').fillna(1)
    data['answer11_9']= pd.to_numeric(data['answer11_9'], errors='coerce').fillna(1)
    data['answer11_10']= pd.to_numeric(data['answer11_10'], errors='coerce').fillna(1)
    data['answer11_11']= pd.to_numeric(data['answer11_11'], errors='coerce').fillna(1)
    data['answer11_12']= pd.to_numeric(data['answer11_12'], errors='coerce').fillna(1)
    
    data['answer11_1']= data['answer11_1'].astype(int)
    data['answer11_2']= data['answer11_2'].astype(int)
    data['answer11_3']= data['answer11_3'].astype(int)
    data['answer11_4']= data['answer11_4'].astype(int)
    data['answer11_5']= data['answer11_5'].astype(int)
    data['answer11_6']= data['answer11_6'].astype(int)
    data['answer11_7']= data['answer11_7'].astype(int)
    data['answer11_8']= data['answer11_8'].astype(int)
    data['answer11_9']= data['answer11_9'].astype(int)
    data['answer11_10']= data['answer11_10'].astype(int)
    data['answer11_11']= data['answer11_11'].astype(int)
    data['answer11_12']= data['answer11_12'].astype(int)
    
    data['answer11_sum'] = data['answer11_1'] + data['answer11_2'] + data['answer11_3'] + data['answer11_4'] + data['answer11_5'] + data['answer11_6'] + data['answer11_7'] + data['answer11_8'] + data['answer11_9'] + data['answer11_10'] + data['answer11_11'] + data['answer11_12']
    
    
    #상세요청주소 값을 기준으로 ROW를 추출하여 select2에 담기
    select2 = data[data['answer15'].str.contains(parameters)]
    
    classify = select2['answer4'].iloc[0]
    classify2 = select2['answer5'].iloc[0]
    classify3 = select2['answer11_sum'].iloc[0]
    
    return render_template('plot.html', value = classify, value2 = classify2, value3 = classify3, id=parameters)
    
    
    
    






@app.route('/result', methods=['POST'])
def result():
    input1 = request.form['input1']
#    input2 = request.form['input2']
#    input3 = request.form['input3']
#    result = input1+input2+"반"+input3+"번"
    print(input1)
    
    url = 'http://airsvr.run.goorm.io/api/users'
    response = urllib.request.urlopen(url).read().decode('utf-8')
    json_return = json.loads(response)
    data = DF(json_return)
    data = data.replace('매우 잘돼요', 1)
    data = data.replace('잘돼요', 1)
    data = data.replace('그저 그래요', 0)
    data = data.replace('집중이 안돼요', 0)
    
    data = data.replace('스트레스 많이 받아요', 1)
    data = data.replace('스트레스 받아요', 1)
    data = data.replace('스트레스 안 받아요', 0)
    
    
  
    #다중응답 카운트
    q13 = data['answer13'].str.split(', ')
    
  
    data['answer13_1']= q13.str.get(0)
    data['answer13_2']= q13.str.get(1)
    data['answer13_3']= q13.str.get(2)
    data['answer13_4']= q13.str.get(3)
    data['answer13_5']= q13.str.get(4)
    data['answer13_6']= q13.str.get(5)
    data['answer13_7']= q13.str.get(6)
    data['answer13_8']= q13.str.get(7)
    data['answer13_9']= q13.str.get(8)
    data['answer13_10']= q13.str.get(9)
    data['answer13_11']= q13.str.get(10)
    data['answer13_12']= q13.str.get(11)
    
    data = data.replace('눈이 따갑고 가려움', 1)
    data = data.replace('목이 따갑고 가려움', 1)
    data = data.replace('두통이나 어지러움', 1)
    data = data.replace('비염증상(코막힘/콧물/재채기 등)', 1)
    data = data.replace('감기', 1)
    data = data.replace('증상없음', 0)

    
    data['answer13_1']= pd.to_numeric(data['answer13_1'], errors='ignore').fillna(0)
    data['answer13_2']= pd.to_numeric(data['answer13_2'], errors='ignore').fillna(0)
    data['answer13_3']= pd.to_numeric(data['answer13_3'], errors='ignore').fillna(0)
    data['answer13_4']= pd.to_numeric(data['answer13_4'], errors='ignore').fillna(0)
    data['answer13_5']= pd.to_numeric(data['answer13_5'], errors='ignore').fillna(0)
    data['answer13_6']= pd.to_numeric(data['answer13_6'], errors='ignore').fillna(0)
    data['answer13_7']= pd.to_numeric(data['answer13_7'], errors='ignore').fillna(0)
    data['answer13_8']= pd.to_numeric(data['answer13_8'], errors='ignore').fillna(0)
    data['answer13_9']= pd.to_numeric(data['answer13_9'], errors='ignore').fillna(0)
    data['answer13_10']= pd.to_numeric(data['answer13_10'], errors='ignore').fillna(0)
    data['answer13_11']= pd.to_numeric(data['answer13_11'], errors='ignore').fillna(0)
    data['answer13_12']= pd.to_numeric(data['answer13_12'], errors='ignore').fillna(0)

    data['answer13_1']= pd.to_numeric(data['answer13_1'], errors='coerce').fillna(1)
    data['answer13_2']= pd.to_numeric(data['answer13_2'], errors='coerce').fillna(1)
    data['answer13_3']= pd.to_numeric(data['answer13_3'], errors='coerce').fillna(1)
    data['answer13_4']= pd.to_numeric(data['answer13_4'], errors='coerce').fillna(1)
    data['answer13_5']= pd.to_numeric(data['answer13_5'], errors='coerce').fillna(1)
    data['answer13_6']= pd.to_numeric(data['answer13_6'], errors='coerce').fillna(1)
    data['answer13_7']= pd.to_numeric(data['answer13_7'], errors='coerce').fillna(1)
    data['answer13_8']= pd.to_numeric(data['answer13_8'], errors='coerce').fillna(1)
    data['answer13_9']= pd.to_numeric(data['answer13_9'], errors='coerce').fillna(1)
    data['answer13_10']= pd.to_numeric(data['answer13_10'], errors='coerce').fillna(1)
    data['answer13_11']= pd.to_numeric(data['answer13_11'], errors='coerce').fillna(1)
    data['answer13_12']= pd.to_numeric(data['answer13_12'], errors='coerce').fillna(1)
    
    data['answer13_1']= data['answer13_1'].astype(int)
    data['answer13_2']= data['answer13_2'].astype(int)
    data['answer13_3']= data['answer13_3'].astype(int)
    data['answer13_4']= data['answer13_4'].astype(int)
    data['answer13_5']= data['answer13_5'].astype(int)
    data['answer13_6']= data['answer13_6'].astype(int)
    data['answer13_7']= data['answer13_7'].astype(int)
    data['answer13_8']= data['answer13_8'].astype(int)
    data['answer13_9']= data['answer13_9'].astype(int)
    data['answer13_10']= data['answer13_10'].astype(int)
    data['answer13_11']= data['answer13_11'].astype(int)
    data['answer13_12']= data['answer13_12'].astype(int)
    
    data['answer13_sum'] = data['answer13_1'] + data['answer13_2'] + data['answer13_3'] + data['answer13_4'] + data['answer13_5'] + data['answer13_6'] + data['answer13_7'] + data['answer13_8'] + data['answer13_9'] + data['answer13_10'] + data['answer13_11'] + data['answer13_12']
    
    select = data[data['answer18'].str.contains(input1)]
    

    
    html = select.to_html()
    
    return render_template('result.html', tables=[select.to_html(classes='select', header="true")], value = input1)




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
