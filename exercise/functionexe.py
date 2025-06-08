def adnum():
    num1 =10
    num2 =13
    print(f'{num1} + {num2} = {num1 + num2}')
adnum()
#add numbers from a list
numbers = [1,2,3,4,5,6,7]
def listnum(ar):
    sum = 0
    for i in ar:
        sum+=i
    return sum
print(listnum(numbers))

#from a range of numbers
def listnum(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum
print(listnum(1,2,4,7,34,6))

#write a function which takes a score as parameter and returns your grade
def grade(score):
    if score <= 100 and score>=80: 
        print('Your grade is A')
    elif score <= 80 and score >=70:
        print('Your age grade is B')
    elif score <= 70 and score >=60:
        print('Your age is C')
    elif score <= 60 and score >=50:
        print('Your grade is D')
    else:
        print('Your grade is F')
    return score
print(grade(60))

#write a function to reverse a list
def reverse(lit):
    lit.reverse()
    return lit
print(reverse(numbers))

#declare a funtion which takes alist as parameter and returns a capitalized version of it
skills = ['javascript','react','node','mongoDb','python']
def capitalized(arr):
    capi = []
    for i in arr:
        capi.append(i.capitalize())
    return capi
print(capitalized(skills))

# a function which takes a list as paramter and add all number in that list
def oddsum(arr):
    sum = 0
    for i in arr:
        if i%2 != 0:
            sum+=i
    return sum
print(oddsum(numbers))

# decale a function that take positive interger as parameter and count the number of even or odd number in the range

def numrange(ran):
    even = 0
    odd = 0
    for i in range(ran+1):
        if i%2 != 0:
            odd+=1
        elif i%2 == 0:
            even+=1
    return f'odd {odd} : even {even}'
print(numrange(146))
    