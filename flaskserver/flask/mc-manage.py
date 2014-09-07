from flask import Flask, redirect, render_template, request, url_for
import processrunner

app = Flask(__name__)

@app.route('/edit')
def manage():
    to_edit = request.args['script']
    filename = "scripts/" + to_edit
    code = ""
    with open(filename, 'r') as f:
        code = f.read()
   
    return render_template(
        'manage.html',
        code=code,
        script_name=to_edit)

@app.route('/save', methods=['POST'])
def save_file():
    write_script(
        request.form['script'],
        request.form['code'])
    return redirect(url_for('run'))
        
def write_script(name, code):
    with open('scripts/' + name, 'w') as f:
        f.write(code)

@app.route('/')
def root():
    return redirect(url_for('run'))
        
@app.route('/run')
def run():
    scripts = processrunner.list_scripts()
    scripts.sort()
    to_run = request.args.get('script', '')
    output = ""
    if to_run:
        command = "python scripts/" + to_run
        output = processrunner.run(command)
    return render_template(
        'run.html', 
        output=output,
        scripts=scripts)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
