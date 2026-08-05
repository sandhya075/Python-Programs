'''funtions
---------
--> function is block that can  be executes when we call it..
--> to avoid the repeated lines of code..
def function_name(parameters):
-------
----
-----
function_name(arguements)


types of functions
--------
1. built-in
---------
eg
--
print()
len()
max()
min()
2. userdefine
----------
--> user-define are  the function that are develop by the user
num= 56
num_2 =89
def total_(num, num_2):
    
    print(num+num_2)
          
total_(num,num_2)
total_(1,2)
    
    
required arguements
---------------
--> we have to pass same number arguements that match the parameters
-->

num= 56
num_2 =89
def total_(num, num_2):
    
    print(num)
          
total_(num,num_2)
total_(1,2)

positional arguements
---------
--> it does not matter how we are passing the variable, if we assign the value to that variable in the calling.....

def name_(name_,name):
    print(name)
    print(name_)
name_(name ='vasavi', name_ ='bantupalli')
'''
a = 0
b = 9
c = 8
d = 7
m = 6
def pos_(m,d,a,c,b):

    print(m)

pos_(a=0,b=8,c=4,d=1,m=7)
