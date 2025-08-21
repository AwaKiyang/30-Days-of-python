#list comprehension in python is a compact way of creating a list from a sequence. it is a short way to create a new list.
#list comprehension is conderably faster than processing a list using the for loop
#first method
language = 'Python'
lst = list(language)
print(type(lst))
print(lst)

#second way
seclst = [i for i in language]
print(seclst)

#generating numbers
num1 = [i for i in range(11)]
print(num1)
#also do mathemtical operations
num2 = [i * i for i in range(11)]
print(num2)
#it is also possible to make a list of tuples
num3 = [(i,i) for i in range(11)]
print(num3)

##conbining list generation with expressions
even = [i for i in range(21) if i%2 == 0]
odd = [i for i in range(21) if i%2 != 0]
print(even)
print(odd)

##lets filter out even positive numbers
number = [-1,-2,-8,-7,0,1,3,4,5,7,6,8,10]
pos_even = [i for i in number if i%2 ==0 and i > 0]
print(pos_even)

#
waar = [[1,2,3],[4,5,6],[7,8,9]]
flat = [number for row in waar for number in row]
print(flat)

#lambda function
#its a funtion without a name
#eg
def add_num(a,b):
    return a+b
print(add_num(1,2))
#or using lambda
add_dig = lambda a, b: a+b
print(add_dig(2,3))

#self invoking lambda function
print((lambda a,b: b - a)(4,7))

#lambda function inside another lambda function
def power(x):
    return lambda n : x ** n
print(power(2)(3))
