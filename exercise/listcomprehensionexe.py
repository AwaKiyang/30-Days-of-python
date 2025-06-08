print('hello')
#filter only negative and 0 in the list
numbers = [-4,-3,-2,-1,0,2,4,6]
num1 = [i for i in numbers if i<=0]
print(num1)

#create this patern
num2 = [(i,i**0,i,i**2,i**3,i**4,i**5) for i in range(11)]
print(num2)

