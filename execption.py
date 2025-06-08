#today we are going to study exeption handling in python
#python uses try and except to handle errors gracefully exit or gracefull handling)
# let try using execption handling

try:
    name = 'awa'
    num = 8
    print(name - num)
except:
    print('something went wrong') # here were are saying that if the block of code written in try section does'nt funtion print code written in exception

#or we can combine it with different type errors
try:
    name = input('enter your name: ')
    year_born = input('Year you were born: ')
    age = 2019 - int(year_born)         #int was added here to mask the typeError
    print(f'your are {name} you were born in {age}')
except TypeError:
    print('Type_Error occured')
except ValueError:
    print('Value erro occured')
except ZeroDivisionError:
    print('Zero division error')
else:
    print('I usually run with the try block')
finally:
    print('I always run')

#packing and unpacking in python
# we use * for tuples and strings while we use ** fro dictionaries

########unpacking############

#unpacking a list
lst = [1,2,3,3,5]
def sum_of_five(a,b,c,d,e):
    return a+b+c+d+e
print(sum_of_five(*lst))

#unpacking a range function
args = [2,7]
number = list(range(*args))
print(number)

#
countries = ['finland','sweden','norway','denmark','iceland']
fin,swe,*rest = countries
print(fin,swe)
print(rest)

#unpacking a dictionary
dct = {
    'name':'Awa',
    'country':'Cameroon',
    'city':'Yaounde',
    'age':21
}
def unpack_dict(name,country,city,age):
    return f'your name is {name}, you live in {country} precisely {city}, you are {age} years old'
print(unpack_dict(**dct))  

##########packing#########
def total(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum
print(total(1,2,3,4,4,5))

#packing dictionary
def pack_dict(**args):
    for key in args:
        print(f'{key} = {args[key]}')
    return args
print(pack_dict(name='Awa',country='Cameroon',age=23))

#spreading in python
lst_one = [1,2,3]
lst_two = [4,5,6]
lst_three = [*lst_one,*lst_two]
print(lst_three)

#enumaratoin
for index, item in enumerate([23,30,40]):
    print(index,item) # returns the item in the kist and its index
#
for index, country in enumerate(countries):
    if country == 'finland':
        print(f'the country {country} has been found at index {index}') #iterates through countries and reutn the index of finlan
#

for index, country in enumerate(countries):
    if 'i' in country :
        print(f'the country {country} containing i has been found at index {index}') #print ing the indexes of the countries containing i
#OR
for i in countries:
    if 'i' in i:
        print(f'the country {i} has i at index of {countries.index(i)}')#an altenative

#Zip used to combine list when looping through them
fruits = ['Banana','orange','mango','lemon','lime']
vegetables = ['Tomato','Potato','Cabbage','onion','carrot','plum']
fruit_veges = list()
for f,v in zip(fruits,vegetables):
    fruit_veges.append({"fruits":f , "vegetables":v})
print(fruit_veges) # print a combination of fruits and vegetables within a dictionary

#
names = ['Finland','Sweden','Norway','Denmark','Iceland','Estonia','Russia']
*nordic_countries,es,ru = names
print(es) # prints estonia