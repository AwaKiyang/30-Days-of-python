#module is a file containing set of codes or a set of functions which can be included to an application
#a module could be file containing a single varailble, afunction or a code base

#importing the file we use the import key word and the name of the file
import mymodule
print(mymodule.sum(1,2,3,4,5,6)) #it has imported sum function from mymodule.py file

#importing a function from a file
from mymodule import sqr, gravity #importing multiple functions
print(sqr(3))
print(gravity())

#importin and renaming
from mymodule import generate_full_name as fullname, persons as p
print(fullname('awa','precious'))
print(p()['age'])

#importing bulit in modules we can also import exisintg python modules using 

