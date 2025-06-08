#Hihger oder funtions enable us to perform more complex operaations using functions
#callback funtion
def sqr(n):
    return n*n
def qube(n):
    return sqr(n) * n #here the function is been called back
print(qube(2))
# or
def sum_numbers(nums):
    return sum(nums)
def hof(f,lst):
    return f(lst)
result = hof(sum_numbers,[1,2,3,4,5])
print(result)
#function as a return value
def name():
    return 'awa'
def hof2():
    return name
#nested funtion
def add_ten():
    ten = 10
    def sums(nums):
        return nums + ten
    return sums
print(add_ten()(3))

# 
def greeting():
    return 'hello world'
def cap(n):
    return n.upper()
print(cap(greeting()))

#using decorators
def waar(n):
    return n * n
def dams():
    return 2
print(waar(dams()))

#built in higher order functions
#map() is a built in function that takes a function and an iterable param
#map(function,iterable)
numbers = [1,2,3,4,5] #iterable
def square(x):
    return x ** 2
numsqr = list(map(square,numbers))
print(numsqr)

#using lambda function
numsqr2 = list(map(lambda x : x**2, numbers))
print(numsqr2)
#
num_str = ['1','2','3','5','6']
wow = list(map(int,num_str))
print(wow)
#
names = ['awa','precious']
toUpp = list(map(lambda name : name.upper(),names))
print(toUpp)

#using filter() filters out items based on a true or false condition
#filter(function,iterable)
def even(num):
    if num%2 == 0:
        return True
    return False
even_lst = list(filter(even,numbers))
print(even_lst)

#reduce() if defined in the functools module and we should import it from this module. like map and filter it takes two param
#reduce(function,iterable)
from functools import *
tota = reduce(lambda x,y: x + y,numbers)
print(tota) 

