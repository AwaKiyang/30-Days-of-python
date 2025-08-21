#a set is a collection of unodered and un-indexed distinct elements in python sets are used to stored unique items and its possible to find thier intersection,difference,symmetric difference, subset,super set and disjiont set among sets

# creating a set 
st = set()
fruits = {'banana','orange','mango','lemon','lemon'}
print(fruits)
waat = {'pablor','roger','evina'}
animal_products = {'milk', 'meat', 'butter', 'yogurt'}
spices = {'salt', 'pepper', 'cumin', 'turmeric'}
web_techs = {'HTML','CSS','JS','React','Redux','Node','MongoDB'}
countries = {'Finland','Estonia','Denmark','Sweden','Norway'}
print(len(fruits))


#checking if an item exist withis a set
print('mango' in fruits)
#adding items to a set using add()
fruits.add('pear')
#adding multiple items to a set using update()
fruits.update(['peach','kiwi','plum'])
print(len(fruits))
#removing items from a set using remove()
fruits.remove('plum')
print(fruits)
#removing a random item from the set using pop()
fruits.pop()
print(fruits)
#clear a set using clear()
waat.clear()
print(waat)
#is you want to delete a set using del
del st
#conveting a list to a set
veges = ['tomato','onion','garlic','leeks']
veges = set(veges)
print(type(veges))

#joining sets we can join sets using update() or union()

veges_fruits = fruits.union(veges)
print(veges_fruits)
#or
spices.update(countries)
print(spices)

#finding items in both sets using intersection()
st1 = {'item1','item2','item3','item4'}
st2 = {'item3','item2'}
print(st1.intersection(st2))

#checkin is a set is a subset or a superset of another
print(st1.issuperset(st2)) #returns true
print(st2.issubset(st1)) #returns true

#cheking the diffrence btw sets using difference()
print(st1.difference(st2))

#checking is sets have a similar item
print(st1.isdisjoint(st2)) #false
print(veges.isdisjoint(web_techs)) # true no similar items