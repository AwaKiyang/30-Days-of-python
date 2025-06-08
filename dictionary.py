#A dictionary is a collectoin of unordered modifiable(mutable) paired (key:value) data type

#to create a dictionary we use curly brackets, or the dict() built in function.
empty_dict = {}
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
dog = dict()
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

player = {
    'game':'fifa',
    'age':22,
    'isPRo':True,
    'controller':'joystick'
}

#using len() to know the size of a dictionary
print(len(person)) #return 7

#accessing dictionaries by using its key name
print(person['firstName'])
print(person['age'])

#Adding new key and values
person['job_title'] = 'Student' #here we have added a new key and giving its value
person['skills'].append('Html') #here we have added a new value to skills key 
print(person)

#modifying a dictionary
person['age'] = '21'
person['secondName']='Kiyang' #here we have modifyied the initial vlues assigned to age and fistrname
print(person)
#checking if a key exist in a dictionary
print('skills' in person)#returns TRUE
print('waar' in person)#returns FALSE
#using pop(), popitem() and del for removing key and value pairs in  dictionary
player.pop('age') #removes the age item
player.popitem() #removes the last item
del player['isPRo'] #removes the specified item
print(player)
#changing a dictionay to a list of tuples using item()
print(player.items())
#clering the items in a dictionary using clear()
print(player.clear())
print(player)
#dlelting a dictionary using del
del empty_dict
#copying a dictionary using copy()
individual = person.copy()
print(individual)
#getting dictionary keys as lists using the key()method
key = person.keys()
print(key) #returns as dict_keys()
#getting dictionary values as a list
values = person.values()
print(values) #returns as dict_values()
print(type(person))
#
print(type(person['skills']))


