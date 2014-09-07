from flask import Flask
from flask import render_template
from flask import request

import processrunner

app = Flask(__name__)

@app.route('/')
def manage():
    return render_template('manage.html') 

@app.route('/save-file', methods=['POST'])
def save_file():
   print("got: " + request.form['code'])

@app.route('/run')
def run():
    (stdout, stderr) = processrunner.run("python -c 'print(123/0)'")
    return render_template('run.html', stdout=stdout) 


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
