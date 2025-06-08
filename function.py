#how to declare functions in python

def generate_full_name():
    firstname = input('enter your name: ')
    last_name = input('last_name: ')
    print(f'your name is {firstname} {last_name}')
generate_full_name() #calling the function

#function returning a value
def total():
    num1 = int(input('enter firt number: '))
    num2 = int(input('enter second number: '))
    total = num1 + num2
    return total
print(total())

#function with parameters
def sum(num1,num2):
    total = num1 + num2
    return total
print(sum(12,10))

def rangetotal(n):
    sum = 0
    for i in range(n+1):
        sum+=i
    return sum
print(rangetotal(100))

#function parameters with key
def name(fname,sname):
    return f'your name is {fname} {sname}'
print(name(fname = 'awa', sname = 'precious'))

#function with default parameter 
def weight(mass,gravity = 9.81):
    return f'object weigth is {(mass*gravity):.2f} newtons'
print(weight(20))
print(weight(20,1.62))#moon gravity

#unlimited number of sarguments
def realname(*args):
    sum = 0
    for num in args:
        sum+=num
    return sum
print(realname(2,3,4,5,6))    

#function as a parameter
def square(n):
    return n*n
def qube(f,n):
    return f(n) * n
print(qube(square,3))
