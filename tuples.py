#creating a tuple is a collection of different datatypes which is ordered and unchangeable, once atuple is created we cannot change it's values. we cannot use insert remove methods on a tuple because its not modifiable

tupe = ()
fruits = ('banana', 'apple','orange','plum')
devices = ('usb','phone','computer','cable')
spices = ('tomato','onion','garlic','leeks','leeks')
print(spices)
numbers = (1,2,3,4,5)
a = tuple()
#length of a tuple
print(len(fruits))

#accesing a tuple 
first_fruit = fruits[0]
second_fruit = fruits[1]
last_fruit = fruits[-1]

#checking for an item in tuple
print('apple' in fruits)

#joining tuple 
fruitsanddevices = fruits + devices
print(fruitsanddevices)

#deleting a tuple its not possible to delete a single item from the tuple but you can delete the whole tuple
del numbers

#converting a tuple to a list
spices = list(spices)#it has been converted to a list
spices[0] = 'peper'
print(type(spices))# it shows its a list
spices = tuple()
print(spices)
print(type(spices))