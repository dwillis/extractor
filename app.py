from flask import Flask
from flask import render_template, request, jsonify
from flask_bootstrap import Bootstrap
from flask_reggie import Reggie
import eatiht.etv2 as etv2
app = Flask(__name__)
Bootstrap(app)
Reggie(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result/', methods=['POST'])
def result():
    url = request.form['url']
    tree = etv2.extract(url)
    text = tree.get_text()
    api_url = url.replace("?","@").replace("&","%")
    return render_template('result.html', url=unicode(url), text=text, api_url=api_url)

@app.route('/api/<regex(".*$"):url>')
def api(url):
    url = url.replace("@","?").replace("%","&")
    print url
    tree = etv2.extract(url)
    text = tree.get_text()
    return jsonify(url=unicode(url), text=text)

if __name__ == '__main__':
    app.run()
