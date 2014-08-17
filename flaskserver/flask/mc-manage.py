from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('manage.html') 

@app.route('/save-file', methods=['POST'])
def save_file():
   print("got: " + request.form['code'])


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
