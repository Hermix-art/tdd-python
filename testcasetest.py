from wasrun import TestCase, WasRun

class TestCaseTest (TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        #meaning of wasRun attribute is 'None'
        assert(not test.wasRun)
        #invocation, which changes 'None' to '1'
        test.run()
        #meaning of wasRun attribute is '1'
        assert(test.wasRun)

<<<<<<< HEAD
# it extends TestCase class. So it has 'run()' method. When we call run below, it invokes, method name provided in constructor
# in case of WasRun we provide 'testMethod()', so it invokes it. currently, we provide 'testRunning()'
=======
#vark = TestCaseTest()
#vark.testRunning()
>>>>>>> 15247962c45d382f18249880ccb8b5cccddad8de
TestCaseTest("testRunning").run()
