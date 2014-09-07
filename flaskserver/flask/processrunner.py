
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
        

        
        