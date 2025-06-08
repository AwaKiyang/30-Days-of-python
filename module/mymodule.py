#creating a module file we write in a python script and we save it as a .py file
#create a file named mymodule.py inside your project folder a wite a code in it
def sum(*args):
    total = 0
    for num in args:
        total+=num
    return total

def sqr(a):
    return a**2

def gravity():
    return 9.81

def generate_full_name(fname,sname):
    return fname+" "+sname

def persons():
    person = {
        'firstName':'Awa',
        'secondName':'precious',
        'age':250,
        'country':'cameroon',
        'isMarried':True,
        'skills':['javascript','react','Node','MongoDb','Python'],
        'adress':{
            'street':'mbandoumou',
            'Zipcode':'02210'
        }
    }
    return person





