#python reggular expressions using re module and it functions
import re

#Method in re modole
#re.match() searches only in the begining of the first line of the string and returns matched objeccts if found, else returns none
#syntax re.match(substring, string, re.I)   # re.I is case ignore
txt  = 'I love to teach python and Javascript espacially Python'
match = re.match(r'I love to teach',txt,re.I)
#we can get the starting and ending position of the match as tuple using span
span = match.span()
print(match)
print(span)

#re.search()  Returns a match object if there is one anywhere in the string and returns its first occurence
#, including multiline strings
#syntax re.search(sunstring,string,re.I)
search = re.search(r'to',txt,re.I)
print(search)
#we can still get the stating and ending position of the string
search_span = search.span()
print(search_span)

#re.findall() returns all the matches as a list
matches = re.findall(r'python',txt,re.I)
print(matches) #retuns all occurences of python as list

#since using re.I makes it case insensitive there are other altenative to re.I
matches1 = re.findall(r'python|PYTHON',txt) #here we specified its exact way its written
print(matches1)
#of
matches2 = re.findall(r'[Pp]ython',txt)
print(matches2)

#re.sub() for replacing a substring within a string
text2 = """Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming languages"""
print(re.sub(r'Python|python','Javascript',text2))  #replaces [Pp]ython occurences with javascript

text3 = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''
refine_text = re.sub('%','',text3)  #still functioning without r'' varaible

print(refine_text) # replacing % with an empty string to print a more clearer sentence
#using re.split() to split the string
print(re.split(r'\n',refine_text)) #spliting at the end of the line into a list


########Writing RegEx patterns###########

#to declare varable we use r'' or NB its not oblage to use it you will still do well without it
#there are many RegEx patterns we will see some of them

"""
 []:  A set of characters
  - [a-c] means, a or b or c
  - [a-z] means, any letter from a to z
  - [A-Z] means, any character from A to Z
  - [0-3] means, 0 or 1 or 2 or 3
  - [0-9] means any number from 0 to 9
  - [A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9
- \\:  uses to escape special characters
  - \d means: match where the string contains digits (numbers from 0-9)
  - \D means: match where the string does not contain digits
- . : any character except new line character(\n)
- ^: starts with
  - r'^substring' eg r'^love', a sentence that starts with a word love
  - r'[^abc] means not a, not b, not c.
- $: ends with
  - r'substring$' eg r'love$', sentence  that ends with a word love
- *: zero or more times
  - r'[a]*' means a optional or it can occur many times.
- +: one or more times
  - r'[a]+' means at least once (or more)
- ?: zero or one time
  - r'[a]?' means zero times or once
- {3}: Exactly 3 characters
- {3,}: At least 3 characters
- {3,8}: 3 to 8 characters
- |: Either or
  - r'apple|banana' means either apple or a banana
- (): Capture and group

"""
#eg
text4 = 'this regular expression was made on December 6, 2019 and revised on july 8 2021'
digits = r'\d' #escape character to locate digits
print(re.findall(digits,text4)) # returns a list of all digits found in the string ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1']
#eg
print(re.findall(r'\d+',text4)) # r'\d+' will permit us to return numbers in whole ['6', '2019', '8', '2021']
#eg  #using (.) period which means any character except new line character
word = "Apple and banana are fruit"
print(re.findall(r'[a].',word)) #retuns all occurences of a an the substring that follows it 
#eg (?) using zero or one time
txt5 = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
print(re.findall(r'[Ee]-?mail',txt5)) # means [Ee]mail with or withou -  # ['e-mail', 'email', 'Email', 'E-mail']

#eg using quantifier {}
print(re.findall(r'\d{4}',text4)) #we can specify the length of a substring we want in a text  
#it will print whole numbers with 4 indexes  ['2019', '2021']

##########you can combine the patterns and use them to query a string
