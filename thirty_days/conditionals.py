#python condotionals 
a = 3
if a > 0:
    print('A is apositive number')

#using if/else
a=3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
#else if(elif)
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A ia a nrgative number')
else:
    print('A is Zero')
#short hand
a = 3
print('A is positive') if a > 0 else print('A is negative')
#nested conditions

b = int(input('enter you age'))
if b > 0:
    print('A is a positive even interger') if a % 2 == 0 else print('A is a positive odd interger')
elif b < 0:
    print('A is a negative interger')
else:
    print('A is equal to zero')

#if condition and logical operators
a =0
if a > 0 and a % 2 == 0:
    print(f'{a} is a positve even interger')
elif a > 0 and a % 2 != 0:
    print(f'{a} is a positive odd interger')
elif a == 0:
    print(f'{a} is Zero')
else:
    print(f'{a} is negative')

#if condition  or logical opreators
user = 'james'
access_level = 3
if user =='admin' or access_level>=4:
    print('Access granted!')
else:
    print('Access denied!')
#dictionary """
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
#check is the person dictionary has skills key
print(person['skills']) if 'skills' in person else print('skills is not iside person')