def scream():
    print 'Yeahaaaa!!!'


#Can assign function to variable, hence shout_loud will print 'Yeahaaaa!!!'
shout_loud = scream
shout_loud()


#Delete function will cause exception
del scream
try:
    scream()
except Exception,e:
    print e


#But variable shout_loud still contains assigned function
shout_loud()


#Possible to create one function inside another one
def nested_function():
    def scream_again():
        print 'Cawabunga!!!'
    scream_again()
nested_function()


#However function exist only in scope of function where it was defined
try:
    scream_again()
except Exception,e:
    print e


#It's possible also to return function from function
def get_talk():
    def simple_talk():
        print 'Hello, World!'
    return simple_talk

my_talk = get_talk()
print type(my_talk)


#If we assigned function to variable obviously we can call it
my_talk()


#Also we can pass functions inside other functions
def shared_talk(func):
    print 'The next line printed by func passed as parameter'
    func()

shared_talk(shout_loud)