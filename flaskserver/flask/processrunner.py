"""
Responsible for running a command line specified and returning the results.
The results are a string that is a contatentaion of both STDOUT and STDERR.

The class must handle long running processes.   These processes may produce
their output over a long period, e.g. counting from 1 to 100 in 1 second
increments.  The client code may wish to see the intermediate state of the 
output at any time before the process has completed.  To handle this running
a process returns an identifier to the caller.  The running process stores
updates to its output in a dictionary keyed on the identifier.  Clients may
request the current contents of the output dictionary at any time.

TODO:  Make sure updates to the dictionary are atomic


"""

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
        
        