#today we are going to stuf=dy python classes
#creating a class
class person():
    pass
print(person)

#crearting an object
p = person()
print(p)

#creating class with contructor to create a constructor in python we use its built in class constructor wtih has a self parameter 
#which is a reference to the corrent instance

class people:
    def __init__(self,name):
        #self enables us to attach parameter to class
        self.name = name
p = people('Awa precious kiyang')
print(p.name)

class user_info:
    def __init__(self,firstname,secondname,age,city,country,married):
        self.user_firstname = firstname   #when attaching a parameter to class using self you can name the parameter anyhow
        self.user_secondname = secondname   #here we named it user_secondname and attached secondname to it
        self.age = age  #here we named it age and attached age to it
        self.city = city
        self.country = country
        self.Marital_status = married

p_user = user_info('Awa','Precious',22,'Yaounde','Cameroon',True)
print(p_user.user_firstname)
print(p_user.user_secondname)
print(p_user.age)
print(p_user.city)
print(p_user.country)
print(p_user.Marital_status)

#creating object methods (methods are built in functoins of an object)
class user_information:
    def __init__(self,firstname,secondname,age,city,country,married):
        self.user_firstname = firstname   #when attaching a parameter to class using self you can name the parameter anyhow
        self.user_secondname = secondname   #here we named it user_secondname and attached secondname to it
        self.age = age  #here we named it age and attached age to it
        self.city = city
        self.country = country
        self.Marital_status = married
    def person_info(self):
        return f'{self.user_firstname} {self.user_secondname} is {self.age} years old. He lives in {self.city}'
p_user = user_information('Awa','Precious',22,'Yaounde','Cameroon',True)
print(p_user.person_info())

#object with default values we can assign defualt values to our objects
class car_info:
    def __init__(self,car_name = 'mercedes',model = '2018',engine = 'v6'):
        self.carName = car_name
        self.Model = model
        self.engine = engine
    def car_details(self):
        return f'your car brand is {self.carName} of the year {self.engine} with a {self.engine} engine'
    

p1 = car_info() #will run with default values
print(p1.car_details())
p2 = car_info('rolls royce','2024','v8')
print(p2.car_details())

#method to modify class default values
class individual:
    def __init__(self,firstname,secondname,age,city,country,married):
        self.user_firstname = firstname   #when attaching a parameter to class using self you can name the parameter anyhow
        self.user_secondname = secondname   #here we named it user_secondname and attached secondname to it
        self.age = age  #here we named it age and attached age to it
        self.city = city
        self.country = country 
        self.Marital_status = married
        self.skills = list()
    def person_info(self):
        return f'{self.user_firstname} {self.user_secondname} is {self.age} years old. He lives in {self.city} with skills '
    
    def add_skill(self,skill):   #method created to append items into skills list
        self.skills.append(skill)

    def upper_case(self):   #methos created to transform text to uppercase
        return self.user_firstname.upper()
p1 = individual('muye','Princewill',18,'Bamenda','Cameroon',False)
p1.add_skill('python')  #here we created a method add_skill which appends the self.skills parameter
p1.add_skill('Node_js')
p1.add_skill('Sql')
p2 = individual('Awa','Precious',22,'Yaounde','Cameroon',True)
p2.add_skill('Html')
p2.add_skill('css') 

print(p1.person_info(),p1.skills)
print(p2.person_info(),p2.skills)
print(p1.upper_case())


####inheritance#####
#inheritance allows us to define a class that inherits all the methods and properties from parent class

#exampple of inheritance
class student(individual):  #student here is the child class which inherits methods from th parent class individual
    pass

s1 = student('Emmanuel','Blaise', 16,'Kobdombo','Togo',False) # as we can see student immediatley inherited all individual parameter
s2 = student('nji','lum',34,'bambili','nigeria',True)
print(s1.person_info())
s1.add_skill('coding')
print(s1.skills)
print(s2.person_info())
s2.add_skill('nursing')
s2.add_skill('crochetting')
print(s2.skills)

"""we did not call the init() constructor in the chils class but if we call the init() we can still access the parent properties by calling super
we can add and overide methods in the child , to overide we create the same method name and add our modifications to it
when we add the init() function the child class no longer iherits it parents properties unless you use super
"""

class scholars(individual):
    def __init__(self, firstname, secondname, age, city, country, married , gender): 
        self.gender = gender  #we have modified our class inheritance by adding another parameter gender
        super().__init__(firstname, secondname, age, city, country, married)
    def person_info(self):
        sex = ''
        if self.gender == 'male':
            sex = 'He'
        else:
            sex = 'She'
        # sex = 'He' if self.gender == 'male' else 'She'
        return f'{self.user_firstname} {self.user_secondname} is {self.age} years old . {sex} lives in {self.city}, {self.country}'

sch1 = scholars('Ntambo','Allan',49,'buchi','Cameroon',True,'male')
sch2 = scholars('Ndipewah','loveline',39,'meta','Cameroon',True,'female')
#
print(sch1.person_info())
sch1.add_skill('police')
print(sch1.skills)
#
print(sch2.person_info())
sch2.add_skill('cooking')
print(sch2.skills)