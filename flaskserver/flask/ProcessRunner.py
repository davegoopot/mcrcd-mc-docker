
import subprocess

class ProcessRunner(object):
    
    @staticmethod
    def run(commandline):
        stdout = subprocess.check_output(commandline, shell=True)
        stderr = ''
        return [stdout, stderr]
        

        
        