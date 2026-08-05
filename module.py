'''
Modules
-------
--> Modules are the python oce which is saved in (.py) that contains functions variables, classes
Types
----
1.Built in
-----------
--> The built in modules that are already designed which comes with python when we are installing
eg
--
1.math
eg-import math
print(math.sqrt(25))

2.sys
eg-import sys
print(sys.version)

3.os
4.random
eg-import random
print(random.randint(1000,9999))


2.user defined
--------------
--> the user defined modules are created by the programmer
syntax
--> import (keyword) module_name
importing wuth alias name
-------------------------
--> we can also import a module with different name
--> after importing with the alias name, we have to use that alias name in the code...
eg
--
import first_module as am

print(am.add(56,8))
print(am.subtact(56,8))

importing only need function
----------------------------
-->When we are importing the few functions from the module can only access that function
syntax
------
---> from (keyword) module_name import(keyword) functions
eg
--
from first_module import add,mul
print(add(56,8))
print(mul(6,7))

importing the all functions
----------------------------
--> use the all fucntions in that module we have to use (*) to get all those....
syntax
------
-->from (keyword) module_name import(keyword)*)
eg
--
from first_module import*
print(add(56,8))
print(mul(56,8))
print(subtract(67,8))
print(div(2,3))
print(power(2,3))




details={
    'name':'sandy'
    'ATM_PIN':'2020'
    }
import random

remain_ = 3
while remain_>0:
    pin = input('Enter pin number: ')
    if pin_==details['ATM PIN']:
        otp = random.randint(1000,9999)
        print(otp)

        user_otp=int(input('Enter user opt: '))
            if user_otp ==otp:
               otp = int(input('Enter option \n1.withdraw \n2.depposite \n3.check balance \n4.history:/n'))
        else:
            remain_-=1
            if remain_>0:
                print(f"incorrect pin entered and you have {remain} left')
            else:
                print(f"you have entered 3 times incorrect pin, card is blocked')

math
----
--> math module used to work on mathematical functionality
floor
---
it will round-down to near value
eg
--
import math
print(math.ceil(3.78))

god
----
--> it will find the gcd value
eg
--
import math
print(math.gcd(24,24))

lcm
---
--> it will find the lcm value
eg

---
import math
print(math.lcm(24,36))

sqrt
-----
--> it will get the square root value
eg
--
import math
print(math.sqrt(25))

factorial
----------
--> it will give factorial value
eg
--
import math
print(math.factorial(5))

random
------
--> the random module is used to get the  random number
randint
-------
--> used to generate random numbers based on the range
eg
--
import random
print(random.randint(1,100))

choice
------
--> it will the random value from the given data
eg
--
import random
colour = ['red','green','blue','yellow']
print(random.choice(colour))

shuffle
-------
--> it can shuffle the data randomly
eg
--
import random
colour = ['red','green','blue','yellow']
print(random.choice(colour))
random.shuffle(colour)
print(colour)

uniform
-------
--> will give the decimal value in a range given
eg
--
import random
print(random.uniform(1,100))

sys
---
--> sys module is used to get the details of python interpreter

version
------
--> the version of python interpreter
eg
--
import sys
print(sys.version)
print(sys.path)

path
----
--> .py path we will get by this function
eg
--
import sys
print(sys.path)

exit
----
--> this function will exit from the program
eg
--
import sys
print(sys.exit())

platform
--------
--> it will gives the python run platfrom
eg
--
import sys
print(sys.platform)


        




        


'''
import_sys
print(sys.platform)



        
        
        
    
