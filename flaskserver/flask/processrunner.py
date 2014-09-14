import os
import os.path
import pexpect
import time


def run(commandline, timeout=30):
    output = pexpect.run(commandline, timeout=timeout)
        
    return output
        
def list_scripts():
    """Return a list of the filenames of all scripts contained in the 'scripts' subdir"""
    
    return [ f for f in os.listdir('scripts') if os.path.isfile(os.path.join('scripts', f)) ]
        
        