from wasrun import TestCase, WasRun

class TestCaseTest (TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.log == "setUp testMethod tearDown")


#  it extends TestCase class. So it has 'run()' and 'setUp()' methods.
#  When we call run below, it invokes those methods. 'run()' invokes the method with the name, passed via constructor (testTemplateMethod)
#  1) create TestCase subclass, providing method name to invoke; 
#  2) call 'run()' and it will invoke 'setUp()' method (default) first and method, passed via constructor then.
TestCaseTest("testTemplateMethod").run()
