from wordcloud import WordCloud
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from flask import Flask, request, render_template, session, url_for, abort, redirect
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def new():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        baseUrl = "https://www.tagsfinder.com/ko-kr/related/"
        inputUrl = request.form['name']
        url = baseUrl + inputUrl + '/'
        source = requests.get(url).text
        bsObject = BeautifulSoup(source, "html.parser")
        hotKey = bsObject.find_all(attrs={'rel':'nofollow'})
        index = 31
        index1 = 0
        cache = {}
        key1 = []
        value1 = []
        for key in hotKey:
            index -= 1
            index1 += 1
            cache[key.text[1:]] = index
            key1.append([key.text[1:], index1])
            value1.append(index)
            if index <= 0:
                break
        return render_template("list.html", data = key1)
@app.route('/list')
def lis():
    return render_template('list.html')
@app.route('/wordcloud')
def wordcloud():
    return render_template('wordcloud.html')
@app.route('/bargraph')
def bargraph():
    return render_template('bargraph.html')
@app.route('/piegraph')
def piegraph():
    return render_template('piegraph.html')
if __name__ == '__main__':
    app.run(debug=True)