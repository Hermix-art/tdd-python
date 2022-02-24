# when we invoke 'run()' method, it calls 'setUp()' and  invokes <name> method passed in constructor (dynamically)

class TestCase:
    def __init__(self, name):
        self.name = name
        
        #default implementation 
    def setUp(self):
        pass

    def run(self):
        self.setUp()
        # dynamical invocation of "testmethod"
        exec ("self." + self.name + "()")  