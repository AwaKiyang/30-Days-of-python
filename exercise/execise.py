dog = dict()
print(type(dog))
#add items to dog
dog['name'] = 'lucy'
dog['color'] = 'darkBrown'
dog['breed'] = 'GermanSherperd'
dog['age'] = 23
print(dog)
#length of the dog dictionary
print(len(dog))
#
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
#print length
print(len(person))
print(type(person['skills']))
print(person['skills'])
#add valuse into skills
person['skills'].append('Mysql')
person['skills'].append('C++')
print(person['skills'])
#getting dcitionary keys to a list
key = person.keys()
print(key)
values = person.values()
print(values)
#changing dictionary to a list of tuples
print(person.items())
#delete one item of a dictionary
dog.pop('age')
print(dog)