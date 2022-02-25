# when we invoke 'run()' method, it calls 'setUp()' and  invokes <name> method passed in constructor (dynamically)

from tempfile import gettempdir
from unittest import result
from testresult import TestResult


class TestCase:
    def __init__(self, name):
        self.name = name
        
    def setUp(self):
        pass

    def tearDown(selr):
        pass

    def run(self, result):
        result.testStarted()
        self.setUp()

        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()


        self.tearDown()

