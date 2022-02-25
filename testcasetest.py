from suite import TestSuite
from testresult import TestResult
from wasrun import TestCase, WasRun

class TestCaseTest (TestCase):

    #Collecting parameter pattern (we have general TestSuite for all test cases, which we change, and at the end check its' summary)
    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))

        result = TestResult()
        suite.run(result)
        assert("2 run, 1 failed" == result.summary())

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.log == "setUp testMethod tearDown") # exception here is caught in TestCaseTest.run() in exception handling part, and exception counter is increased
    
    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 failed" == result.summary()) # result deliveres result here, and if assertion exception appears, it's caught in TestCaseTest.run()
        # in general there is 1 level of assertion string above, which logs "runs and fails" in 'testResult()',  in 'run()' method

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


suite= TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testSuite"))
result= TestResult()
suite.run(result)
print (result.summary())
