import os
import processrunner
import time
import unittest

class ProcessRunnerTests(unittest.TestCase):

    def testBasicRunFile(self):
        """The runner should run python against a file and return the stdout contents"""
        command = "python -c 'print(2+3)'"
        output = processrunner.run(command)
        self.assertEquals("5\r\n", output)
        
        command = "python -c 'print(5+3)'"
        output = processrunner.run(command)
        self.assertEquals("8\r\n", output)
        
    def testBasicScriptsFile(self):
        """Make sure that we can run a python file from the scripts dir"""
        try:
            with file('scripts/test.py','w') as f:
                f.write('print(6*3)')
            
            command = "python scripts/test.py"
            output = processrunner.run(command)
            self.assertEquals("18\r\n", output)
        finally:
            try:
                os.remove('scripts/test.py')
            except OSError:
                pass
                
    def testStdError(self):
        """We should make sure the any stderr is also sent to the output"""
        command = '/bin/bash -c "echo test 1>&2"'
        output = processrunner.run(command)
        self.assertEquals("test\r\n", output)
        
        command = "python -c 'print(12/0)'"
        output = processrunner.run(command)
        self.assertTrue("ZeroDivisionError" in output)
        
    def testListScripts(self):
        """Return the list of available scripts"""
        try:
            with file('scripts/test.py','w') as f:
                pass
            with file('scripts/test2.py','w') as f:
                pass
            scripts_list = processrunner.list_scripts()
            self.assertItemsEqual(['test.py', 'test2.py'], scripts_list)
        finally:
            try:
                os.remove('scripts/test.py')
                os.remove('scripts/test2.py')
            except OSError:
                pass
        
    def testChunkedResponses(self):
        """The output of running the process needs to be made available
        incrementally as the process runs.
        """
        
        command = "python -c 'print(\"first\n\"); from time import sleep; sleep(1);print(\"second\n\")'"
        
        #TODO write code for run returning only an ID
        proc_id = processrunner.run(command)
        
        #TODO write code for getting process output by id
        #initial_output = processrunner.current_output(id=proc_id)
        
        #self.assertEqual('first\n', initial_output)
        time.sleep(2)
        #final_output =  processrunner.current_output(id=proc_id)
        
        #self.assertEqual('first\nsecond\n', final_output)
        
    def testRunReturnsId(self):
        """ When invoked the process runner run() method returns an identifer
        for the process.  The identifier is the sha1 hexdigest() of the command
        that was run plus the time the command is invoked as returned from the
        time.time() command.
        The processes as stored returned in the processrunner.output dictionary
        """
        self.assertEqual(0, len(processrunner.output))
        