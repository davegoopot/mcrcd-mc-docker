import os
import processrunner
import unittest

class ProcessRunnerTests(unittest.TestCase):

    def testBasicRunFile(self):
        """The runner should run python against a file and return the stdout contents"""
        command = "python -c 'print(2+3)'"
        (stdout, stderr) = processrunner.run(command)
        self.assertEquals("5\n", stdout)
        
        command = "python -c 'print(5+3)'"
        (stdout, stderr) = processrunner.run(command)
        self.assertEquals("8\n", stdout)
        
    def testBasicScriptsFile(self):
        """Make sure that we can run a python file from the scripts dir"""
        try:
            with file('scripts/test.py','w') as f:
                f.write('print(6*3)')
            
            command = "python scripts/test.py"
            (stdout, stderr) = processrunner.run(command)
            self.assertEquals("18\n", stdout)
        finally:
            try:
                os.remove('scripts/test.py')
            except OSError:
                pass
                
    def testStdError(self):
        """We should make sure the any stderr is also sent to the output"""
        command = "echo test 1>&2"
        (stdout, stderr) = processrunner.run(command)
        self.assertEquals("test\n", stdout)
        
        command = "python -c 'print(12/0)'"
        (stdout, stderr) = processrunner.run(command)
        self.assertTrue("ZeroDivisionError" in stdout)