import os
import os.path
import subprocess


def run(commandline):
    stdout = ''
    try:
        output = subprocess.check_output(
            commandline,
            shell=True,
            stderr=subprocess.STDOUT
            )
    except subprocess.CalledProcessError, ex:
        output = ex.output
        
    return output
        
def list_scripts():
    """Return a list of the filenames of all scripts contained in the 'scripts' subdir"""
    
    return [ f for f in os.listdir('scripts') if os.path.isfile(os.path.join('scripts', f)) ]
        
        