#using oprators
print('comple number', (1 + 1j)*(1 - 1j))
#using comparison operators
print(3>2)
print(3<2)
body = 'andrew'
#suing comparison operators
print('a' in body)
print('A' in body) #returns false since A is uppercase
print('c' not in body) #returns true since c is not in andrew
print(1 == 1)
print(1 != 2)
print('True == False', True == False)
#using logical operators and, or, not
print(3 > 2 and 4 > 3)
print(3 > 2 and 4 < 3) #both statements have to be true to return true
print(3 > 2 or 4 < 3)
print(3 < 2 or 4 < 3) # atleast one statement has to be true