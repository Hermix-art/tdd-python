from wasrun import TestCase, WasRun

class TestCaseTest (TestCase):
    def setUp(self):
        #global instance for current TestCaseTest object
        self.test = WasRun("testMethod")

    def testRunning(self):
        #invocation, which changes 'None' to '1'
        self.test.run()

        #meaning of wasRun attribute is '1'
        assert(self.test.wasRun)

    def testSetUp(self):
        self.test.run()
        assert(self.test.log == "setUp testMethod")


#  it extends TestCase class. So it has 'run()' method. When we call run below, it invokes, method name provided in constructor
#  in case of WasRun we provide 'testMethod()', so it invokes it. currently, we provide 'testRunning()'
TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
