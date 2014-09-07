
import subprocess


def run(commandline):
    stdout = ''
    try:
        stdout = subprocess.check_output(
            commandline,
            shell=True,
            stderr=subprocess.STDOUT
            )
    except subprocess.CalledProcessError, ex:
        stdout = ex.output
        
    stderr = ''
    return [stdout, stderr]
        

        
        