from flask import Flask
from flask import render_template, request, jsonify
from flask_bootstrap import Bootstrap
import eatiht.etv2 as etv2
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result/', methods=['GET','POST'])
def result():
    if request.form:
        url = request.form['url']
    else:
        url = request.args.get('url')
    tree = etv2.extract(url)
    text = tree.get_text()
    return jsonify(url=url, text=text)

if __name__ == '__main__':
    app.run()
