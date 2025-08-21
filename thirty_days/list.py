#a list is a collection of differrent datatypes which is odered and changeable(modifiable). Allows duplicate member
#creating a list
name = 'awa'
print(len(name))
print(name.count('a'))
lst = list()
print(len(lst))
#or
myList = []
print(len(myList))
fruits = ['banana','orange', 'mango', 'lemon']
veges = ['tomato', 'potato', 'cabbage', 'onion', 'carrot']
animal_products = ['milk', 'meat', 'butter', 'yogurt']
spices = ['salt', 'pepper', 'cumin', 'turmeric']
web_techs = ['HTML','CSS','JS','React','Redux','Node','MongoDB']
countries = ['Finland','Estonia','Denmark','Sweden','Norway']
lst = ['awa',23,True,{'country':'cameroon', 'city':'yaounde'},2.33]
positve_num = [1,2,3,4,5]
negative_num = [-1,-2,-3,-4,-5]
zero = [0]

#printing a list
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('veges:', veges)
print('num of fruits:', len(veges))
print('spices:', spices)
print('num of spices:', len(spices))
print(lst)

#accessing list items using index of list items
print((fruits[0],veges[1],animal_products[3],spices[2],web_techs[3],countries[0]))
#accessing last index using negative numbers
print(lst[-1])
print(spices[-2]) #here negative two refes to the second to the last item

#unpacking list items that actually assing varaible to items in our string using their index
first_fruit,second_fruit,third_fruit,fourth_fruit = fruits
print(first_fruit) #it has been assing item one in fruit list // reutrns banana
print(second_fruit)
print(third_fruit)
print(fourth_fruit)
#you can all use * to display the remaining unassing items
fir_tech, sec_tech, thi_tech, *rest_tech = web_techs
print(fir_tech)#its been assigned the first item
print(sec_tech)
print(thi_tech)
print(rest_tech)#displays all remainig web_tech programs

#modifying a list we use the sytax
fruits[0] = 'lime' #updates the first index of the list
print('fruits: ', fruits)
spices[-1] = 'onion' #updates the last indexof the list
print('spices: ', spices)

#checking items in a list
print('banana' in fruits) # banana does'nt exist anymore since it was replaced with lime so it returns fasle
print('lime' in fruits)

#adding items to a list using append()
fruits.append('apple')
print('fruits:', fruits, len(fruits))

#inserting items to a list and specifying its position using insert in ther bracket the first part specifies the index and second part item to be inserted
spices.insert(1,'garlic')
print('spices: ', spices)

#removing items from a list using remove() which remove a specified item from the list
web_techs.remove('MongoDB')
print('webs: ', web_techs)

#removing items using pop() which
# remove items using the specified index if not specified remove the last item in the list
countries.pop() #since not specified removes the last item in the list
countries.pop(0) #remove the the first item in the list
print('countries: ', countries)

#i have added back norway to list using the append() method
countries.append('Norway') 
countries.insert(1,'Cameroon')
print('countries: ', countries)

#deleting items within a range using del and indexes
del fruits[0]#deletes item with index zero
del veges[1:3] #deletes within a range that is from item index 1 to index 2
print(veges)

#clearing a list using the clear() method
lst.clear()
print(lst) # it has cleared the list

#copying a list assing the values of a list it another using copy() method
fruit_copy = fruits.copy()
print('fruits: ',fruits)
print('fruit_copy: ', fruit_copy)

#joining a;list using the plus operator
number = negative_num + zero + positve_num
print(number)
fruits_and_veges = fruits + veges
print(fruits_and_veges)

#joining a list using the extend() method which permits us to append a list in a list
negative_num.extend(zero) #extends the list by adding the seto list
negative_num.extend(positve_num) #extends also
print('intergers: ', negative_num)

fruits.extend(veges) #extends the fruit list by adding the veges list
print('salad: ', fruits)

#counting items in a list using count()
print(fruits.count('apple'))
print(spices.count('salt'))

#returning the frist occurrence of and item in a list
print(spices.index('salt'))
print(negative_num.index(0))

#reversing the order of a list using reverse() method
spices.reverse()
print(spices)

#using the sort() method to sort out a list 
#sort() sorts out list in ascending order
#sort(reverse=true) sorts out a list in decending order
#sort() method modifies the origina list that is the list that has been sort will remain so

spices.sort() #sorts in ascending aplabetical order
negative_num.sort(reverse=True) # in decending order
print('spices: ', spices)
print('interger: ', negative_num)

#using sorted without modiying the originan list
#can be used with reverse=true to sort in decending order
print(sorted(negative_num))
print(sorted(animal_products,reverse=True))#sorts in decending order
print(animal_products)

