#python date and time module to handle date and time
import datetime
print(dir(datetime)) # with dir or help its possible to know the in built functions in a module as we can see the dattime module has many functions

#getting datetime information from datetime import all
from datetime import datetime
today = datetime.now()
print(today)
day = today.day
month = today.month
year = today.year
hour = today.hour
minute = today.minute
second = today.second
timestamp = today.timestamp()
print(day,month,year,hour,minute)
print('timestamp',timestamp) # timestamp is the number seconds elapsed since january 1970

day = datetime(2020,1,1)
print(day)
 
#formating using strftime
now = datetime.now()
time = now.strftime('%H:%M:%S') #where %H is hour %M minute %S second
timeone = now.strftime('%d/%m/%y , %H:%M:%S')
timetwo = now.strftime('%m/%d/%y , %H:%M:%S')
print(f'{time}\n{timeone}\n{timetwo}')
#there are other strftime symbols that exist like %B month name or %A day name

#string to time using strptime
date_string = '5 December, 2019'
print('date_string : ', date_string)
date_object = datetime.strptime(date_string, '%d %B, %Y')
print('date_object: ', date_object)

#time objects to represent time
from datetime import time
a = time()
print('a :',a)
b = time(10,30,50)
print('b =', b)
c = time(hour= 10,minute=30,second=50)
print('c =', c)
d = time(10,30,50,200555)
print('d=',d)

#difference btw two dates
from datetime import date
today = date(year=2019,month=12,day=5)
new_year = date(year=2020,month=1,day=1)
print('time_difference : ', new_year - today)

#    