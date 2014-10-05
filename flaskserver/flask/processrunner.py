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

import hashlib
import os
import os.path
import pexpect
import threading
import time


"""Dictionary containing the output of all run processes.  The keys are the SHA1
hexdigest() of the command that was run plus the time the command is invoked as
returned from the time.time() command.  The values are the string output of the
command being run.
"""
output = {}

""" Dictionary containing keys of ids matching the values of the spawned pexpect
subprocesses.  When the process has finished the id is removed from the
dictionary.
"""
running_processes = {}

def update_output(id):
    """ Worker function expected to be called in a new thread when a command
    line is created.  Watch the child process recorded in running_processes
    against the passed if for output and update the output dictionary
    accordingly.
    """
    child_proc = running_processes[id]
    next_line = child_proc.readline()

    while next_line != '':
        output[id] = output[id] + next_line
        next_line = child_proc.readline()

    del running_processes[id]
    
def wait_to_complete(id):
    """ Blocking function waiting on the passed id to be removed from the 
    running_processes dictionary before returning
    """
    while id in running_processes:
        time.sleep(0.2)
    
def run(commandline, timeout=30):
    child = pexpect.spawn(commandline)
    id = createid(commandline)
    output[id] = ''
    running_processes[id] = child
    output_collector = threading.Thread(target=update_output, args=(id,))
    output_collector.start()
    return id
        
def list_scripts():
    """Return a list of the filenames of all scripts contained in the 'scripts' subdir"""
    
    return [ f for f in os.listdir('scripts') if os.path.isfile(os.path.join('scripts', f)) ]
        
def createid(command, time_ran=None):
    """The createid function takes two strings, the command and optionally the
    time it was invoked and returns a hex identifier which is the SHA1 digest
    of the two strings.
    """
    sha1 = hashlib.sha1()
    sha1.update(command)
    if not time_ran:
        time_ran = str(time.time())
    sha1.update(time_ran)
    return sha1.hexdigest()
