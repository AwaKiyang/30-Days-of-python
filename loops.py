#loops in python w3e have two types of loops while loop and for loop
#while loop
count =0
while count < 5:
   print(count) 
   count+=1
    
    
#using while loop and else in the below consition will be false when count is 5 and the loop stops and execution starts the else statement \
count1 =0
while count1 <5:
    print(count1)
    count1+=1
else:
    print(count1)
#using break and continue with while loop
count2 =0
while count2 <5:
    print(count2)
    if count2 ==3:
        break # breaks it at 3
    count2+=1
    
#using continue
count3 =0
while count3 < 5:
    count3+=1
    if count3 == 3:
        continue
    print(count3)
    
#for loop is used for iterating in (tuples,dictionary,set or string)
numbers = [0,1,2,3,4,5]
for num in numbers:
    print(num)
language = 'ENGLISH'
for lang in language:
    print(lang)

#for loop with tuple
digits = (0,1,2,3,4,5,6)
sum = 0
for dig in digits:
    sum+=dig
print(sum)

#for loop in dictionary
person = {
    'firstName':'Awa',
    'secondName':'precious',
    'age':250,
    'country':'cameroon',
    'isMarried':True,
    'skills':['javascript','react','Node','MongoDb','Python'],
    'adress':{
        'street':'mbandoumou',
        'Zipcode':'02210'
    }
}
for key in person.keys():#print keys
    print(key)
for values in person.values():#print values
    print(values)
for pers in person.items():#print items
    print(pers)

#break and continue using for loop

for num in numbers:
    print(num)
    if num == 3:
        break

for num in numbers:
    if num == 3:
        continue
    print(num)

#the range function the range funtion is used to list numbers, the range(start, end, step(increment)), by default it starts from 0 and increnent by 1
lst = list(range(11))
print(lst) # [0,1,2,3,4,5,6,7,8,9,10]
st = set(range(1,11)) #starting at one and ending at 11
print(st) #{1,2,3,4,5,6,7,8,9,10}
tup = tuple(range(1,11,2))#start at 1 endat 11 and increment by 2
print(tup) #(1,3,5,7,9)

for num in list(range(0,20,2)):
    print(num)

#nested loops
"""
for x in y:
    for t in x:
        print(t)
"""
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

#for else if you want to execute a message when the loop ends
for number in range(11):
    print(number)
else:
    print('11')

#pass in python when statement is required after a semicolon but we don't want to use any staement there we use pass
for number in range(6):
    pass