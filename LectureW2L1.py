#Author: Sarah Bolton

#########################################################################
# Pr 1
# Create a python script file (example: Pr1_WK2.py), that when executed prints
# to screen.
# Hello problem 1 from Week 2 Lesson 1.

print("Hello World")

#########################################################################
# Pr 2
# Explain why you should ALWAYS have a .gitignore file in your repo.

#It allows you to ignore updating files that you don't want git to track.

#########################################################################
# Pr 3
# Using open , create a new file that records user input (min 1, max 4 inputs) and
# then opens that files and APPENDS the following “Received User Input”

inputNumber = 10
while (inputNumber > 4):
    inputNumber = int(input("How many inputs would you like? (must be <= 4)"))

infile = open('myfile.txt', 'w+')

for i in range(0,inputNumber):
    userInput = input("What would you like to add?")
    infile.write(userInput + '\n')

infile.close()

infile2 = open('myfile.txt', 'a')
infile2.write('Received User Input')
infile2.close()

#########################################################################
# Pr 4
# repeat # 3 with a with

inputNumber = 10
while (inputNumber > 4):
    inputNumber = int(input("How many inputs would you like? (must be <= 4)"))

with open('myfile.txt', 'w+') as infile:
    for i in range(0,inputNumber):
        userInput = input("What would you like to add?")
        infile.write(userInput + '\n')

with open('myfile.txt', 'a') as infile2:
    infile2.write('Received User Input')


#########################################################################
#Pr 5
# Homework
# • Create a new git repo in github.
#• Populate it with typical files and directories (.gitignore and README.md)
#• Commit your changes.
#• Push it to your repository

#Created here: https://github.com/sjbolton/PythonClass