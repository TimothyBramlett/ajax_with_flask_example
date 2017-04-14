

from flask import Flask, render_template, request, url_for
import datetime


app = Flask(__name__)
PORT = 5000


@app.route('/', methods=['GET', 'POST'])
def index():


    if not request.script_root:
        # this assumes that the 'index' view function handles the path '/'
        request.script_root = url_for('index', _external=True)

    return render_template('main.html')


@app.route('/ajaxtest', methods=['GET'])
def ajaxtest():

    return '{"result": "Hello AJAX World!"}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=PORT)