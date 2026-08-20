'''
oops
----
--> object oriented programming system
--> oops is used to maintain the code structure in object and class...
1.class
-------
--> class is an blueprint or template to an object
syntax
------
class(keyword) Name:
     #attribute
     #methods
eg
--
class stu:
     name = 'Sandy'
     age= 23
s1 = stu()
print(s1.name)
print(s1.age)

2.object
---------
--> object is instance of the class
syntax
------
class(keyword) Name:
    #attribute
    #methods
eg
--
class car:
   def__init__(self):
    self.colour = 'Red'
    self.seat = 6
    self.brand = 'BMW'
c1 = car()
print(c1.colour)
print(c1.brand)
  

any_= class_name
3.attribute
4.methods
---------
--> Method is a function that is created inside the class
syntax
-----
class(keyword) name:
  #attributes
  def fun_name(self):
  #code
obj = class_name()
print(obj.fun_name())
eg
--
class bank:
    def __init__(self):
        self.Adr = '123456789011'
        self.age = 22
        self.pan = '1234aADC23'
        self.ph = 1234567890
per_d = bank()
print(per_d.Adr)
print(per_d.age)
print(per_d.pan)
print(per_d.ph)
        


class
object
Attributes
---------
--> Attribute is the data present in the class or pass to the class
eg
--
class students:
    def __init__(self,name,age,batch):
        self.name = name
        self.age = 23
        self.batch = 5

    def all_data(self):
        print(self.name)
        print(self.age)
        print(self.batch)

stu_1 = students('sandy',22,5)
stu_1.all_data()

stu_2 = students('sandy',22,5)
stu_2.all_data()





Take car

colour

brand
seet

methods
-------

class student:
    def __init__(self):
        self.color = 'blue'
        self.seat = 6
        self.Brand= 'BMW'
        
    def brake_(self): usage
        print(f'{self.Brand} brake will apply at speed 250KM')
        
    def accelater_(self): usage
        print(f'{self.Brand} will take 2 sec to reach 180 speed')
        
    def clucth(self): usage
        print(f'{self.Brand} with {self.seat} No automatic')
Bwm = car()
Bwm.brake_()
Bwm.accelater_()
Bwm.clucth()

class registration:
    def __init__(self,name,age,email,ph):
        self.name = name
        self.age = 23
        self.email = email
        self.ph = 1234567890

    def all_data(self):
        print(self.name)
        print(self.age)
        print(self.email)
        print(self.ph)

registration_1 = registration('sandy',22,'sandhyapyla075@gmail.com','1234567890')
registration_1.all_data()

registration_2 = registration('sandy',22,'sandhyapyla075@gmail.com','1234567890')
registration_2.all_data()



