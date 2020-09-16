#Author: Sarah Bolton

#########################################################################
## 1 Lists
#- Create an empty list. Append 4 strings to the list. Then pop one item off the end of the list.

myList = [] #create empty list
myList.append('string1')  #append strings
myList.append('string2')
myList.append('string3')
myList.append('string4')
print("List before popping: ", myList)

myList.pop()  #pop one string off
print("List after popping: ", myList)

#########################################################################
## 2 Dictionaries
#- Create a dictionary using with a zip and two lists
#- Add to this dictionary using the key "HW2" with value "Done"
#- Define a dictionary using both string literals and variables containing strings.

a = 'one'

dict1 = dict(zip((a, 'two'), (1,2))) #Create a dictionary using with a zip and two lists
print("My dictionary before adding: ", dict1)

dict1['HW'] = 'Done'
print("My dictionary after adding: ", dict1)


#########################################################################
## 3 Strings
#- Use a literal to create a string containing:
#* a single quote,
#* a double quote,
#* both a single and double quote.

str1 = 'Hello World'
str2 = "Hello World"
str3 = "Hello 'great' World"


#########################################################################
# 4 Strings Multiline
#- Write a string literal that spans multiple lines.
str4 = "this string spans " \
       "multiple lines"


#########################################################################
## 5 `join`
#- Use the string `join` operation to create a string that contains a
#  colon as a separator.
str5 = ":".join(('Hello', 'World'))

#########################################################################
## 6 String Format.
#- Use string formatting to produce a string containing your last and
#  first names, separated by a comma.

first = 'Sarah'
last = 'Bolton'
name =  '{1} , {0}'.format(first, last)