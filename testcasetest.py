from wasrun import TestCase, WasRun

class TestCaseTest ():
    def testRunning(self):
        test = WasRun("testMethod")
        #meaning of wasRun attribute is 'None'
        assert(not test.wasRun)
        #invocation, which changes 'None' to '1'
        test.run()
        #meaning of wasRun attribute is '1'
        assert(test.wasRun)

#invocation of 'testRunning()
vark = TestCaseTest()
vark.testRunning()
# TestCaseTest("testRunning").run()
