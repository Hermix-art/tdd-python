# first we initialize WasRun object, invoking it's superclass constructor (which sets up name of method to be invoked).
# then we invoke 'run()' method 
# notice! wasRun attribute belongs only to subclass WasRun

class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        # dynamical invocation of "testmethod"
        exec ("self." + self.name + "()")  



#WasRun is a subclass of TestCase
class WasRun(TestCase):
    def __init__(self,name):
        # if name is "testMethod" than this method is invoked
        self.wasRun= None
        TestCase.__init__(self, name)


    def testMethod(self):
        self.wasRun= 1
