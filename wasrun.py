from testcase import TestCase

#WasRun is a subclass of TestCase
class WasRun(TestCase):
    def __init__(self,name):
        # if name is "testMethod" than this method is invoked
        TestCase.__init__(self, name)

    def testMethod(self):
        self.wasRun= 1

    def setUp(self):
        self.wasRun= None
        self.wasSetUp= 1
