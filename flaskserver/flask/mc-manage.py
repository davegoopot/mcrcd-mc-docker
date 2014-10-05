"""
Responsible for providing the routing from the web requests over to the
process runner and back again.
"""

from flask import Flask, make_response, redirect, render_template, request, url_for
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
    return redirect(url_for('manage'))
        
def write_script(name, code):
    with open('scripts/' + name, 'w') as f:
        f.write(code)

@app.route('/')
def root():
    return redirect(url_for('manage'))
        
@app.route('/manage')
def manage():
    """
    Handle the management of the available scripts and running processes.
    All the available scripts are shown with options to edit or create new.
    
    The UI flow is:
        1. List the available scripts
        2. User edits and existing script or creates a new one
        3. User clicks to run a script
        4. Running a script opens a new browser window to show the output
    """
    scripts = processrunner.list_scripts()
    scripts.sort()
    return render_template(
        'manage.html', 
        scripts=scripts)

@app.route('/run/<scriptname>')
def run(scriptname):
    """
    Run the passed scriptname and show the output incrementally.
    The page uses javascript to periodically poll for more output.  The control
    relies on two further URIs:
        /output/<pid>  -- returns the text/plain output for the associated pid
        /isrunning/<pid> -- returns 'yes' or 'no' depending on whether the pid
                            is still active or not
    TODO:  write the output method to return the output
    TODO:  write the isrunning method
    TODO:  update the javascript on the runscipt template to periodically update
           the output while the script is still running
           the output while the script is still running
    
    
    """
    command = "python scripts/" + scriptname
    pid = processrunner.run(command, timeout=300)
    return render_template(
        'run.html', 
        pid=pid,
        scriptname=scriptname)

@app.route('/output/<pid>')
def output(pid):
    """returns the text/plain output for the associated pid"""
    output = processrunner.output[pid]
    resp = make_response(output, 200)
    resp.mimetype = 'text/plain'
    return resp
        
        
@app.route('/isrunning/<pid>')
def isrunning(scriptname):
    """
    returns 'yes' or 'no' depending on whether the pid is still active or not
    
    TODO
    """
    return "yes" # hard coded for testing only
        
        
if __name__ == '__main__':
    app.debug = True
    # Because the processor uses a shared dictionary to store the output,
    # we must ensure that there is only one webserver process run
    app.run(host='0.0.0.0', processes=1)
