def my_cool_decorator(function_to_decorate):

    #define wrapper since we can't return function decorator function itself
    def wrapper_around_original_func():
        print "this text will be print BEFORE decorated func"
        #call to decorated function
        function_to_decorate()
        print "this text will be print AFTER decorated func"

    #return wrapper function
    return wrapper_around_original_func


def standalone_function():
    print "DONT TOUCH ME!!!"


standalone_function_decorated = my_cool_decorator(standalone_function)

standalone_function_decorated()