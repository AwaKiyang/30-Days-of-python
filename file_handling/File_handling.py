#in python we are able to handle files an dperform some ooperations with them
#syntax  open('filenme', mode) # mode('r','a','w','x','t','b') used for writing ,reading, updating other modes exist
#by default open is set to read mode
f = open('file.txt')
print(f)  #<_io.TextIOWrapper name='file.txt' mode='r' encoding='cp1252'> # as we can see it's set by default to read
txt = f.read()  #read here is the mode read() here specify to read everything
print(txt)
f.close()

b = open('file.txt')
txt10 = b.read(10)   # here we have specified the first ten characters
print(txt10)

#readline() mode enables us to read a single line
t = open('read_line.txt')
line = t.readline()
print(line)
t.close()

#readlines() mode read all text line by line and returns a list of lines
a = open('read_line.txt')
lines = a.readlines()
print(lines)
a.close()

#splitlines mode read all lines as a list using splitlines()
c = open('read_line.txt')
text2 = c.read().splitlines()
print(text2)
c.close()

'''#NB every opened file has to closed we often forget to do that 
# the new syntax used which closes file automatically isby using with'''

with open('read_line.txt') as r:  #with will enable us automatically close so this is the syntax to be used
    lines = r.read(20)
    print(lines)

#####writing and updating in files
#to do so we use 
# write() will overwrite any existing content, if the file does no exist it creates it
with open('damn.txt','a') as f: #mode set to 'a' append open file for appending create file if not exist
    f.write('\nStop playin bro am stuying python')

with open('file.txt','w') as f: #mode set to 'w' overwrite file content and create file if not exist
    f.write('Damn')  #change the word inside to see how it overwites the file or add something at the level of file name to see how it create a new file

#deleting a file we use the os module
#if the file does not exit we are going to have this error # FileNotFoundError: [WinError 2] The system cannot find the file specified: 'damn.txt'
import os
try:
    os.remove('./python_codes/file_handling/damn2.txt') #removes specified file
except FileNotFoundError:
    print('File does not exist')  # we have combined it with execption handling to resolve incase specified fikle is not seen

########manipulating JSON files ##########
#JSON is a stringified javascript object or python dictionary
import json
#JSON
person_json = '''{
    "name" : "Awa",
    "country" : "Cameroon",
    "city" : "Yaounde",
    "age" : 23,
    "skills" : ["Javascipt","Python"]
}'''
#changing json to python dictionary
person_dct = json.loads(person_json) #json.loads converts person_json to python dictionary
print(type(person_dct)) #type dict
print(person_dct)

#changing dictionary to json 
#python dictionary
player = {
    'game':'fifa',
    'age':22,
    'isPRo':True,
    'controller':'joystick',
    'married' : False
}
player_json = json.dumps(player, indent=4) #indent could be 2,4,6,8 it beutifies the json
print(type(player_json)) #type string
print(player_json)

#saving as a json file
with open('C:/Users/awaki/Desktop/python_codes/file_handling/damn2.json','w',encoding='utf-8') as f:  #create file if not exist
    json.dump(player,f,ensure_ascii=False,indent=4)  
    #ensure_ascii=False allows us to write non-ascii characters in the json file
#reading a json file
with open('C:/Users/awaki/Desktop/python_codes/file_handling/damn.json') as f:
    waar = json.load(f)# json.load() reads the json file and transfers it's content 
    print(type(waar))
    print(waar) 