#Author: Sarah Bolton

#########################################################################
#- Write a function that takes a single argument, prints the value of
#the argument, and returns the argument as a string.

def myFunction(arg1):
    print(arg1)
    return (arg1)

string = myFunction("hello world")
print(string)

#########################################################################
#- Write a function that takes a variable number of arguments and
#prints them all.

def variableFunction(*args):
    for i in args:
        print(i)

variableFunction("Hello", "world", 1, False)

#########################################################################
#- Write a function that prints the names and values of keyword
#arguments passed to it.

def variableKeywordFunction(**kwargs):
    for key, value in kwargs.items():
        print (key, "=", value)

variableKeywordFunction(aa = 11, bb = 33, cc = 'Hello', dd = 22)

#########################################################################
#- Write a python script (file) that prints your name as all lower case, upper case and
# proper capitalization. (Bonus) if you can pass in your name: input()? argparse? etc

def captialization():
    name = input("Enter your name:")
    print("Upper case name:", name.upper())
    print("Lower case name:", name.lower())
    print("Title case name:", name.title())

captialization()