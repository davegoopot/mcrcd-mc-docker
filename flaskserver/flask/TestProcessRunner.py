import os
import processrunner
import time
import unittest

class ProcessRunnerTests(unittest.TestCase):

    def testBasicRunFile(self):
        """The runner should run python against a file and return the stdout contents"""
        command = "python -c 'print(2+3)'"
        id = processrunner.run(command)
        processrunner.wait_to_complete(id)
        self.assertEquals("5\r\n", processrunner.output[id])
        
        command = "python -c 'print(5+3)'"
        id = processrunner.run(command)
        processrunner.wait_to_complete(id)
        self.assertEquals("8\r\n", processrunner.output[id])
        
    def testBasicScriptsFile(self):
        """Make sure that we can run a python file from the scripts dir"""
        try:
            with file('scripts/test.py','w') as f:
                f.write('print(6*3)')
            
            command = "python scripts/test.py"
            id = processrunner.run(command)
            processrunner.wait_to_complete(id)
            self.assertEquals("18\r\n", processrunner.output[id])
        finally:
            try:
                os.remove('scripts/test.py')
            except OSError:
                pass
                
    def testStdError(self):
        """We should make sure the any stderr is also sent to the output"""
        command = '/bin/bash -c "echo test 1>&2"'
        id = processrunner.run(command)
        processrunner.wait_to_complete(id)
        self.assertEquals("test\r\n", processrunner.output[id])
        
        command = "python -c 'print(12/0)'"
        id = processrunner.run(command)
        processrunner.wait_to_complete(id)
        self.assertTrue("ZeroDivisionError" in processrunner.output[id])
        
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
        
        command = "python -c 'print(\"first\"); from time import sleep; sleep(1);print(\"second\")'"
        
        proc_id = processrunner.run(command)
        time.sleep(0.2)
        self.assertEquals("first\r\n", processrunner.output[proc_id])
        
        time.sleep(2)
        self.assertEquals("first\r\nsecond\r\n", processrunner.output[proc_id])
        
        
    def testRunReturnsId(self):
        """ When invoked the process runner run() method returns an identifer
        for the process.  The identifier is the sha1 hexdigest() of the command
        that was run plus the time the command is invoked as returned from the
        time.time() command.
        The processes as stored returned in the processrunner.output dictionary
        """
        starting_output_entries = len(processrunner.output)
        pid = processrunner.run('echo "hello"')
        self.assertEqual(starting_output_entries+1, len(processrunner.output))
        self.assertIn(pid, processrunner.output)
        processrunner.wait_to_complete(pid)
        self.assertEqual("hello\r\n", processrunner.output[pid])
        
    def testCreateId(self):
        """ createid generates ids based on command and time ran. Check here for
        uniqueness.
        """
        self.assertEquals(
            processrunner.createid("test", time_ran="1"),
            processrunner.createid("test", time_ran="1"))
            
        self.assertNotEquals(
            processrunner.createid("test", time_ran="1"),
            processrunner.createid("test", time_ran="2"))

        self.assertNotEquals(
            processrunner.createid("test", time_ran="1"),
            processrunner.createid("test2", time_ran="1"))

        # If you don't pass a time_ran then take the system time.time() value
        id1 = processrunner.createid("test")
        time.sleep(0.1)
        id2 = processrunner.createid("test")
        self.assertNotEquals(id1, id2)

