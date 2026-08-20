
'''
'''
Types
-----
1.single inheritance
--------------------
---> If one child class inherite from one parent class this is called single inheritance
eg
--
class father:
    def land(self):
        print('5 acer land')

class me(father):
    def flat(self):
        print('6 flat')

all_ = me()
all_.flat()
all_.land()



2.multiple inheritance
----------------------
--> if one child inherit from more than one parant class this is called multiple inheritance
eg
--
class father:
    def home(self):
        print('Home at village')

class mother:
    def gold(self):
        print('50kg gold')
        
class son(father, mother):
    def flat(self):
        print('sons flat')
all_to = son()
all_to.home()
all.to.gold()

3.multi level  inheritance
---------------------------
--> one child class become parent class to the another is called multi-level inheritance
eg
--
class grandfather:
    def land(self):
        print('Grandfather land')

class father(grandfather):
    def flat(self):
        print('Father flat')
        
class son(father):
    def car(self):
        print('sons car')
fam = son()
fam.land()
fam.flat()
fam.car()

4.hierachrchiacal inheritance
-----------------------------
--> if two child class inherite from one parant is called as hierichical inheritance
eg
--
class father:
    def land(self):
        print('50 acer land')

class son_1(father):
    def flat(self):
        print('first son flat')
        
class son_2(father):
    def car(self):
        print('second son car')

S1 = son_1()
S1.land()
S1.flat()
S2 = son_2()
S2.land()
S2.car()


    
5.hybrid  inheritance
---------------------
--> inherite from more than two types into one class is called ashybrid inheritance
eg
---
class person:
    def name(self):
        print('sandy is her name')
class student(person):
    def study(self):
        print('B.Tech final year')
class py_teacher:
    def teach(self):
        print('python')
class java_teacher:
    def teac(self):
        print('java')
class learner(py_teacher,java_teacher):
    def learn(self):
        print('Learner')
class all_get(student,learner):
    def get_it(self):
        print('This person getting all data')

an = all_get()
an.name()
an.study()
an.teach()
an.teac()
an.learn

practice
-------

class father:
    def house(self):
        print('house')
class me(father):
    def car(self):
        print('car')
all_ = me()
all_.house()
all_.car()
class father:
    def money(self):
        print('5 lakh money')
class me(father):
    def scooty(self):
        print('scooty')
all_ = me()
all_.money()
all_.scooty()
class mother:
    def silver(self):
        print('silver')
class me(mother):
    def gold(self):
        print('10 grams')
all_ = me()
all_.silver()
all_.gold()
class father:
    def land(self):
        print('2 acer land')
class mother:
    def gold(self):
        print('100 grams')
class son(father,mother):
    def car(self):
        print('sons car')
all_ = son()
all_.land()
all_.gold()

        
             

        
    
            
