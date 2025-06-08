#write a funtion which generates a userId of 6 characerter contain numbers and numbers
import string
from random import random,choice,sample,shuffle
import math 
import sys
#write a function to generate random user id
def randomId():
    char = string.ascii_lowercase + string.digits
    Id = ''
    for i in range(6):
        Id+=char[math.floor(random() * len(char))]
    return Id
print(randomId())

#write a function which generate random Id based on user input

def gen_Id_by_user():
    numChar = int(input('enter the number of characters you want: '))
    numTimes = int(input('enter the number of Ids you want to generate: '))
    damn = []
    for ntimes in range(numTimes):
        char = string.ascii_lowercase+string.digits
        Ids=''.join(choice(char) for nchar in range(numChar))  #random.choice helps to select items randomly 
        damn.append(Ids)
    return damn
print(gen_Id_by_user())

#write a function which will generate rgbcolors
print('rgb({},{},{})'.format(sys.argv[1],sys.argv[2],sys.argv[3]))

#write a function whish returns an array of seven random  numbers
def arran():
    return sample(range(10), 7) #sample returns an array of unique random numbers number
print(arran())

#write a functoin which takes an array as parameter and returns a shuffle array
num = [1,2,3,4,5,6,7,8,9,0]
def shuf(arr):
    shuffle(arr) #shuffles an array
    return arr
print(shuf(num))



