from testresult import TestResult
from wasrun import TestCase, WasRun

class TestCaseTest (TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.log == "setUp testMethod tearDown")
    
    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 failed" == result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert("1 run, 1 failed" == result.summary())

    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed" == result.summary())


#  it extends TestCase class. So it has 'run()' and 'setUp()' methods.
#  When we call run below, it invokes those methods. 'run()' invokes the method with the name, passed via constructor (testTemplateMethod)
#  1) create TestCase subclass, providing method name to invoke; 
#  2) call 'run()' and it will invoke default'setUp()' method, method, passed via constructor, and tearDown method (default)

TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
TestCaseTest("testFailedResultFormatting").run()

#TestCaseTest("testFailedResult").run()


