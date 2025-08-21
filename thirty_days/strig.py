letter = 'p'
name = 'kiyang'
sentendce = """i am creating a multimline string
by using the triple qoute symbol"""
print(letter,"\n",name,"\n",sentendce)
challenge = 'thirty days of python'
web_tech = ['HTML','CSS','JAVASCRIPT','PYTHON']
#concatenate in python using 
letter1 = "A"
letter2 = "W"
letter3 = "A"
age = 23
a = 5
b = 6
height = 1.72332
c = 3.32324
print(letter1+letter2+letter3) #displays AWA
print('\n')
#we now need to learn how to use escape sequence
print('I hope everyone is enjoying the python challenge.\nAre you ?')
print('Days\tTopics\tExecises')
print('Day 1\t5\t\t5')
print('Day 2\t6\t\t20')
print('Day 3\t5\t\t23')
print('Day 4\t1\t\t35')
print('This is a backslash symbol (\\)')
print('In every progaming language it starts with \"Hello world!\"')
#string formating old and new style

#old style
print('my name is %s'%(name))
print('my name is %s my age is %d, my height is %f inches approximately %.2f inches'%(name,age,c,c))
#new style
print(f'my name is {letter1 + letter2 + letter3} {name}, my age is {age}, my height is {height} approximately {height:.2f} inches')
print(f'man {letter1} + i\'ll est trop high{letter2}, {a+b},')

#accesing string charaters by index
print(name[0])
print(name[1])
# you can access a string from the rigth by using negative values
print(name[-1]) #displays k
#reversing a string
print(name[::-1]) # displays gnayik

#STRING METHODS
#capitalize(): converts first character of string to capital letter
print(name.capitalize())
print(name.upper())#to uppercase
print(name.lower())#to lowercase

#count(): used to count the occurence of a substring in a stirng and can be associated with a start and end index values to specify where the method should stat counting
print(challenge.count('y')) # returns 3
print(challenge.count('y',7,14))#where we have specified counting from index 7 to 14
print(challenge.count('days')) # returns 1

#endswith(): used to check if a string ends with a particular substring
print(challenge.endswith('python'))
print(challenge.endswith('java')) # returns false
#startswith(): used to check if a string starts with a particular substring
print(challenge.startswith('t'))
print(challenge.startswith('ze baby'))

#expandtabs(): used to expand tabs
print(challenge.expandtabs(5))#increases its tabs

#find(): returns the index of the first occurence of a substring
#rfind(): returns the index of the last ooccurence of a sub string

print(challenge.find('y'))#returns the index of the first occurence of y
print(challenge.rfind('y'))# returns the index of the last occurence of y

#index(): return the first index of a substring similar to find
#rindex(): returns the last occurence of a substring similar to rfind
print(challenge.index('y'))
print(challenge.rindex('y'))

#isalnum(): to checks if the string is alphanumeric spaces are excluded
print('30DaysPython'.isalnum())# returns true
print('Thirty Days of python'.isalnum())#does not accept spaces

#isalpha(): checks is the string is alphabet
print('ThirtyDaysPyhton'.isalpha())
print('30Daysofpython'.isalpha()) #returns false

#isdecimal(); checks is string is decimal
print('23.05'.isdecimal())
print('1234'.isdecimal()) #returns false

#isdigit(): checks if a string is digit
print('12345'.isdigit())
print('12.34'.isdigit())#returns false

#isnumeric(): check is a string is numeric and also accepts more symbols like 1/2
print('1235'.isnumeric())
print('ae93rj4495'.isnumeric())#returns false

#isupper(): checks if a string is uppercase
print('WAAR PAPA'.isupper())
print('waar papa'.isupper())
#islower(): checks if a string is lowercase
print('waar papa'.islower())
print('WAar papa'.islower())

#using join() to return a concatenated string
print(' '.join(web_tech))
#using strip() to remove all given charaters in a string
print(challenge.strip('days')) 
#using split() to split a string
print(challenge.split())
#using title() to return cased string
print(challenge.title())
#using swapcase() to change a strings value from upper to lower case and vice versa
print(challenge.swapcase())