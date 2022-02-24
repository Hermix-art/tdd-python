class TestCase:
    def __init__(self, name):
        self.name = name



class WasRun(TestCase):
    def __init__(self,name):
        # if name is "testMethod" than this method is invoked
        self.wasRun= None
        TestCase.__init__(self, name)

    def run(self):
        # dynamical invocation of "testmethod"
        exec ("self." + self.name + "()")  

    def testMethod(self):
        self.wasRun= 1
