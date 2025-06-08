lst = []
mylist = ['ball','wandas', 'smoke','games','beer']
print(len(mylist))
print(mylist[0],mylist[2],mylist[-1])
mixed_data_types = ['awa', 23, 1.72, False ,'yaounde']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(mixed_data_types)
print(it_companies)
print(len(it_companies))
print(it_companies[0],it_companies[3],it_companies[-1])
it_companies.append('Nvidia')
print(it_companies)
it_companies.insert(4,'Tesla')
print(it_companies)
it_companies.extend('#')
print(it_companies)
print('Amazon' in it_companies)

it_companies.sort(reverse=True)
print(it_companies)

it_companies.pop(0)
print(it_companies)
del it_companies[4]
print(it_companies)
del it_companies[-1]
print(it_companies)
it_companies.clear()
print(it_companies)
#
front = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back = ['Node', 'Express', 'MongoDB']
front.extend(back)
print(front)

#execise level 2
age = [19, 22,19,24,20,25,26,24,25,24]
age.sort()
print(age)
print(f'min number is : {age[0]} and maximum number is {age[-1]}')
print(f'median age is : {(age[4] + age[5])/2}')
