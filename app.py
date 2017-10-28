from flask import Flask
from flask import render_template, request, jsonify
from flask_bootstrap import Bootstrap
from flask_reggie import Reggie
from libextract.api import extract
from requests import get
app = Flask(__name__)
Bootstrap(app)
Reggie(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result/', methods=['POST'])
def result():
    url = request.form['url']
    r = get(url)
    textnodes = list(extract(r.content))
    text = textnodes[3].text_content()
    print(textnodes)
    api_url = url.replace("?","@").replace("&","%")
    return render_template('result.html', url=url, text=text, api_url=api_url)

@app.route('/api/<regex(".*$"):url>')
def api(url):
    url = url.replace("@","?").replace("%","&")
    r = get(url)
    tree = etv2.extract(url)
    textnodes = list(extract(r.content))
    text = textnodes[3].text_content()
    return jsonify(url=url, text=text)

if __name__ == '__main__':
    app.run()
