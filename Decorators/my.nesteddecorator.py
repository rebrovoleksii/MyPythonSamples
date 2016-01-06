def testsuite_logging_decorator(function):
    def wrapper():
        print "Test Suite execution started"
        function()
        print "Test Suite execution finished"
    return wrapper

def testcase_logging_decorator(function):
    def wrapper():
        print "Test Case execution started"
        function()
        print "Test Case execution finished"
    return wrapper

@testsuite_logging_decorator
@testcase_logging_decorator
def simple_testcase():
    print "Step1 --> Passed"
    print "Step2 --> Failed"
    print "Step3 --> Blocked"

simple_testcase()