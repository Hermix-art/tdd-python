# when we invoke 'run()' method, it calls 'setUp()' and  invokes <name> method passed in constructor (dynamically)

from testresult import TestResult


class TestCase:
    def __init__(self, name):
        self.name = name
        
        #default implementation 
    def setUp(self):
        pass

    def tearDown(selr):
        pass

    def run(self):
        self.setUp()

        # dynamical invocation of "testmethod"
        method = getattr(self, self.name)
        method()

        self.tearDown()
        return TestResult()

