
'''
1.constructor
------------
--> __init__
--> The constructor is a special method that only run when the object is created
--> Mostly we will take data inside this method..
eg
--
class cls_data:
    def __init__(self):
        self.name = 'sandy'
        self.course = 'python'

cls_ = cls_data()
print(cls_.name)
print(cls_.course)


2.self
-------
--> the self keyword refers to current object
eg
--
class stu:
    def __init__(self):
        self.name = 'sandy'

    def any_(self.name)
s1.cls
s1.any_()
eg2
---
class stu_data
    def __init__(self,name,batch,age):
        self.name = name
        self.batch = batch
        self.age = age

    def student(self):
        print(f'{self.name} from batch {self.batch} and age {self.age})
detail = stu_data('sony',125,22)
detail.student()
    
        
        
3.encapsulation
----------------
--> wrapping data and methods together is called as encapsulation and using or controlling the data in methods
eg
--
class stu_data:
    def __init__(self,name,batch,age):
        self.name = name
        self.batch = batch
        self.age = age

    def student(self):
        print(f'{self.name} from batch {self.batch} and age {self.age}')
detail = stu_data('sony',125,22)
detail.student()

access specifiers
-----------------
1.public
----------
--> this can be access normallly and can call it like a normal variable
eg
--
self.name = name
print(self.name)

2.proctected(_name)
-------------------
--> just adding single(_) before a variable it becomes
protector variable
eg
--
self._age = age
print(self._age)
eg
--
class stu_data: usage
     def __init__(self, name, batch, age, fee):
        self._name = name
        self._batch = batch
        self._age = age
        self._fee = fee
        
    def only_name(self): 1usage
        print(f"{self._name}")
        
    def only_batch(self): 1usage
        print(f"(self._name}')

    def only_fee(self): 1usage
        print(f'{self._fee}')
    
data1 = stu_data('sony',125,22,45000)
data1.only_name()
data.only_age()
data.only_fee()

    
        

3.private  (__name)
-------------------
--> adding (__) before a varible it becomes it becomes private variable
eg
--
self.__balance = balance
print(self.__balance)
eg
--
class stu_data: usage
     def __init__(self, name, batch, age, fee):
        self._name = name
        self._batch = batch
        self._age = age
        self._fee = fee
        
    def only_name(self): 1usage
        print(f"{self._name}")
        
    def only_batch(self): 1usage
        print(f"(self._name}')

    def only_fee(self): 1usage
        print(f'{self._fee}')
    
data1 = stu_data('sony',125,22,45000)
data1.only_name()
data.only_age()
data.only_fee()
eg
--
class bank_ac:
    def __init__(self):
        self.name = 'sandy'
        self.Adr = '123456789'
        self.pan = 'ad3456789'
        self.__balance = 4567

    def details(self):
        print(self.name)
        print(self.Adr)
        print(self.pan)

    def bank_bal(self):
        print(self.balance)

AC = bank_ac()
AC.details()
        
practice
--------
class university:
    def __init__(self):
        self.name = 'sandy'
        self.course = 'B.Tech'
        self._Department = 'C.S.E'
        self._Batch = 2026-2026
        

    def details(self):
        print(self.name)
        print(self.course)
        

    def income_(self):
        print(self.Department)

    def type_(self):
        print(self._Batch)

university = university()
university.details()

class collage:
    def __init__(self):
        self.name = 'sandy'
        self.course = 'BCA'
        self.batch = 'CSE'

    def details(self):
        print(self.name)
        print(self.course)

    def income_(self):
        print(self.batch)

collage = collage()
collage.details()


  
