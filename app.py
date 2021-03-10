from flask import Flask, render_template, request, redirect, url_for, send_file
import json
import requests
import urllib.request
import sys
from pandas import DataFrame as DF
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from wordcloud import WordCloud
from konlpy.tag import Hannanum
from io import BytesIO
import re
from collections import Counter
import time
import matplotlib.font_manager as fm
from matplotlib import rc
import matplotlib as mpl
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.io as po
from IPython.core.display import Image as image
from PIL import Image


app = Flask(__name__)

    
@app.route('/') #, methods =['GET']

def root():
    url = 'http://chatsvr.run.goorm.io/message/@all'
    response = urllib.request.urlopen(url).read().decode('utf-8')
    json_return = json.loads(response)
    data = DF(json_return)
    
    li = ' '.join(data['text'])
    li = li.split()
    
    file = open("static/stopwords.txt")
    stop = file.readlines()
    for i in range(len(stop)):
        stop[i] = stop[i].strip()
    
    result = []
    for i in li:
        if i not in stop:
            result.append(i)

    li2 = ' '.join(result)
    li3 = re.sub('[!@#$%^&*()-+[]{}♥:;?/]', '',li2)
    li3 = re.sub('[ㄱ-ㅎㅏ-ㅣ0-9a-zA-Z]', '',li3)
    li3 = re.sub('[♥&;#]', '',li3)

    t =Hannanum()
    key = t.nouns(li3)
    for i,v in enumerate(key):
        if len(v)<2:
            key.pop(i)

    count = Counter(key)
    tags = count.most_common(50)

    
    #num = Counter(key)
    
    font_path = 'static/NotoSans-Black.otf'
    wordcloud = WordCloud(font_path=font_path, background_color="white", width=800, height=800).generate_from_frequencies(dict(tags))
    fig = plt.figure(figsize=(6,6))
    plt.imshow(wordcloud)
    plt.axis('off')
    fig.savefig('static/wordcloud.png')
    

    #fig2 = plt.figure(figsize=(6,6))
    data2 = DF(tags)
    data2.columns=['sym','freq']

    trace1 = go.Bar(x=data2['sym'], y=data2['freq'])
    dataset = [trace1]
    layout = go.Layout()
    fig2 = go.Figure(data=dataset, layout=layout)

    #fig2.wirte_image('static/plot2.png')
    #po.write_html(fig2, file="static/plot.html")
    #fig2 = pyo.iplot(fig2)
    #po.write_image(fig2, file='static/plot2.png')
    #plot=Image(po.to_image(fig2, format="png"), width=576, height=576)
    
    fig2.write_image("static/plot.png", width=800, height=800)
    
    return render_template('wordcloud.html', time=time.time())
    

#print('설정파일 위치:', mpl.matplotlib_fname())






if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='8000')