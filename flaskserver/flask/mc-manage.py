"""
Responsible for providing the routing from the web requests over to the
process runner and back again.
"""

from flask import Flask, redirect, render_template, request, url_for
import os.path
import processrunner

app = Flask(__name__)

@app.route('/edit')
def edit():
    to_edit = request.args['script']
    filename = "scripts/" + to_edit
    code = """import mcpi.minecraft as minecraft
import mcpi.block as block
 
world = minecraft.Minecraft.create(address='mc')    
"""
    if os.path.isfile(os.path.join('scripts', to_edit)):
        with open(filename, 'r') as f:
            code = f.read()
   
    return render_template(
        'edit.html',
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
    """
    Handle the management of the available scripts and running processes.
    All the available scripts are shown.
    The parameter showoutput=ID is optional.  If passed then the output is given
    for the pass identifier, if present.
    """
    scripts = processrunner.list_scripts()
    scripts.sort()
    to_run = request.args.get('script', '')
    output = ""
    if to_run:
        command = "python scripts/" + to_run
        output = processrunner.run(command, timeout=300)
    return render_template(
        'run.html', 
        output=output,
        scripts=scripts)

@app.route('/output/<scriptid')
def showoutput(scriptid):
    """
    Return the current contents of the processrunner's output dictionary for
    the passed scriptid.  The contents will be returned as text/plain MIME type.
    
    If the scriptif is not found then provide a user-friendly response, being
    careful to sanitize the scriptid for cross-site scripting attacks.
    """
    pass
        
        
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', processes=20)
