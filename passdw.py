from itertools import product
import string

min_len = int(input("enter min length of charater: "))
max_len = int(input("enter max length of characters: "))
counter = 0
charater = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation

file_open = open("worlist.txt",'w')

for i in range(min_len,max_len+1):
    for j in product(charater,repeat=i):
        word = "".join(j)
        file_open.write(word)
        file_open.write('\n')
        counter+=1
print("wordlist of {} passwords created".format(counter))
