# compare age
"""age = int(input('Enter your age: '))
if age >= 18:
    print('you are old enough to dive')
else:
    print(f'you need {18-age} more yesra to dive')
# compare two numbers
num1 = int(input('enter 1st number: '))
num2 = int(input('enter second number: '))
if num1 > num2:
    print('num1 is bigger than num2')
elif num2 > num1:
    print('num2 is bigger than num1')
else:
    print('num1 is equal to num2')"""
#write a code which gives grades to students according to thier scores
score = int(input('Enter your score: '))
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
#
fruits = ['apple','orange','plum','pear','mango']
cocktail = input('Enter  a fruit: ')
if cocktail in fruits:
    print('fruit already exist')
else:
    fruits.append(cocktail)
    print(fruits)

