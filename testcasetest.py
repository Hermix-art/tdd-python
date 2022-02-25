from unittest import TestSuite, suite
from testresult import TestResult
from wasrun import TestCase, WasRun

class TestCaseTest (TestCase):

    def testSuite(self):
        suite = TestSuite()

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.log == "setUp testssMethod tearDown") # exception here is caught in TestCaseTest.run() in exception handling part, and exception counter is increased
    
    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 failed" == result.summary()) # result deliveres result here, and if assertion exception appears, it's caught in TestCaseTest.run()

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
#  3) as TestCaseTest also extends TestCas, exception handling and TestResuld returning is also implemented in its' 'run()' method

print (TestCaseTest("testTemplateMethod").run().summary())
print (TestCaseTest("testResult").run().summary())
print (TestCaseTest("testFailedResultFormatting").run().summary())
print (TestCaseTest("testFailedResult").run().summary())


