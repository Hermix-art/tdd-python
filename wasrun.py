class WasRun:
    def __init__(self,name):
        self.wasRun= None
        self.name = name

    def run(self):
        # self.testMethod()
        exec ("self." + self.name + "()")  

    def testMethod(self):
        self.wasRun= 1
