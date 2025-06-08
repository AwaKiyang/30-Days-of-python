#
for num in list(range(1,11)):
    print(num)
#iterate from 1 to ten using while loop
count = 1
while count < 11:
    print(count)
    count+=1

#write a loop the print out this
coun = 1
while coun < 8:
    print('#'*coun)
    coun+=1

#or
for i in range(1,8):
    print('#'*i)

#
for dems in range(8):
    print("# " * 8)

for i in range(11):
    print(f'{i} x {i} = {i*i}')
#iterate through the list
tech = ['python','django','panda','flask']
for tec in tech:
    print(tec)

#pritt 0 100 even numbers
for even in range(0,101,2):
    print(even)
#print only odd numbers
for odd in range(1,100,2):
    print(odd)
#add numbers from 0 to 100
total = 0
for sum in range(101):
    total+=sum
print(total)

#
oddnum = 0
evennum = 0
for evenodd in range(101):
    if evenodd % 2 != 0:
        continue
    evennum+=evenodd
for evenodd in range(101):
    if evenodd % 2 == 0:
        continue
    oddnum+=evenodd 
print(f'even numb ers are {evennum} and odd numbers are {oddnum}')

#reversinng a lis into another list3
fruit = ['banana','mango','orange,','lemon']
revfruitst = list()
for i in range(len(fruit)-1,-1,-1):
    revfruitst.append(fruit[i])
print(revfruitst)