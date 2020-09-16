#Author: Sarah Bolton

#########################################################################
# - Write a conditional expresion statement with, "if, Elif and else." to check if Mystring = "Hello World" is a string

test1 = "Hello World"
test2 = 3
test3 = True

def stringChecker(Mystring):
    if type(Mystring) == str:
        print (Mystring, "is a string")
    elif type(Mystring) == int:
        print(Mystring, "is an int")
    else:
        print(Mystring, "is a", type(Mystring))

stringChecker(test1)
stringChecker(test2)
stringChecker(test3)

#########################################################################
#- Write a list comprehension that returns all the keys in a dictionary
#whose associated values are greater than zero.
#- The dictionary: `{'aa': 11, 'cc': 33, 'LESS Than': -55, 'bb': 22}`
#- Output should be a list

a = {'aa': 11, 'cc': 33, 'LESS Than': -55, 'bb': 22}
tempList = [x[0] for x in a.items() if x[1] > 0]
print (tempList)

#########################################################################
#- Write a list comprehension that produces even integers from 0 to 10.
#Use a `for` statement to iterate over those values and print results to screen.
numberlist = [ x for x in range(11) if x%2 == 0]
for i in numberlist:
    print (i)

#########################################################################
#- Write a list comprehension that iterates over two lists and produces
#all the combinations of items from the lists.
a = ['aa', 'bb', 'cc']
b = [1,2,3]
combination = [(x, y) for x in a for y in b]

print(combination)

#########################################################################
#- Using `break` , write a `while` statement that
#prints integers from zero to 5.
i = 0
while True:
    print(i)
    i+=1
    if i > 5:
        break


#########################################################################
#- Using `continue` , write a `while` statement
#that processes only even integers from 0 to 10. Note: `%` is the
#modulo operator.

i = 0
while i <= 10 :
    if i%2 == 0:
        print(i)
    i+=1