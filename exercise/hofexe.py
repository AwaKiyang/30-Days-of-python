countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland','chile']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#use for loop to print out each country incountries list
for pay in countries:
    print(pay)
#use map() to create a new list of uppercase countries
upper_pay = list(map(lambda country : country.upper(),countries))
print(upper_pay)

#use filter to check for counryies having land
country_land = list(filter(lambda land: 'land' in land, countries))
print(country_land)

#use filter to filter out countryies having 6 characters
def sixshar(x):
    return True if len(x) == 6 else False
country_six = list(filter(sixshar,countries))
print(country_six)

#filter out countries having six letters and more
country6andMore = list(filter(lambda country: len(country) >= 6,countries))
print(country6andMore)

#use filter to filter out countries starting with 'E'
countryE = list(filter(lambda E: E.startswith('E'),countries))
print(countryE)

#declare a functoin which takes a list as parameters and only returns the strings it contains
strArr = [1,'awa',True,'boring']
def get_string(arr):
    stringlst = list(filter(lambda str: type(str) == type('string'),arr)) 
    return stringlst
print(get_string(strArr))

#use reduce to summ all numbers in the number list
from functools import*
Numsum = reduce(lambda x,y: x + y,numbers)
print(Numsum)

#
sentence = reduce(lambda acc,country: acc+', '+country if country != countries[-1] else acc+', and '+country+' are caribain countries',countries)
print(sentence)
