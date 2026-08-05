set
----
-set do not allows duplicate values inside it..
-set mutable..
- set is represented in {}

do = {1,2,3,2}
print(do)
#creating empty set
so = set()
print(type(so))

methods
------
1.update
------
use to add new value into set

syntax-- variable_name.update(itterable)
eg
---
2.add
-----
use to add new value into set

syntax ---variable name.update(value)
do = {1,2,3}
do.add(4)
print(do)

do={1,2,3}
do.update('python')
print(do)

3.remove()
------
used to del the value from the set, incase if the value is not present in the set will get the kayerror

syntax --variable_name.remove(value)
eg
--
do  {1,2,3,4}
do.remove(4)
print(do)

4.discard()
--------
used to del the value from the set, but never give any error incase value is not present inside the et...

syntax --variable_name.remove(value)
eg
--
d0 = {1,2,3}
do.discard(4)
print(do)
5.pop()
-----

used to delete the value but this pop() will take 0 arguments inside it

syntax -- variable_name.pop()

eg
--
do = {1,2,3}
do.pop()
print(do)

operations
------
1.union
--------
gives all sets value together but no duplicates

eg
--
do = {1,2,3}
so = {3,4,5}
print(do|so)
print(do.union(so))

2.intersection
-----
eg
--
do = {1,2,3}
so = {3,4,5}
print(do&so)
print(do.intersection(so))


3.difference
------------
eg
--
do = {1,2,3}
so = {3,4,5}
print(so - do)
print(do.difference(so))

TYPE CONVENTION
Int : string:Float
string -- str()
eg
--
num = 9
print(type(num))
so = str(num)
print(type(so))

Float
-----
 string --str()
 Integer
 eg
 ---
 print(type(so))
nums = 8.67
print(type(nums))
all_ = int(nums)
print(all_)
print(type(all_))


string
-------
eg
-- 
how = "67"
print(type(how))
who = int(how)
print(type(who))

list--list
eg
--
how ='2345'
print(type(how))
who = list(how)
print(who)
print(type(who))

tuple -- tuple()

eg
--
how ='2345'
print(type(how))
who = tuple(how)
print(who)
print(type(who))

list
------
eg
--
nums = [1,2,3,4]
print(type(nums))
all_n = list(nums)
print(type(all_n))


string -- str()
eg
--
nums = [1,2,3,4]
print(type(nums))
all_n = str(nums)
print(type(all_n))


tuple -- tuple()
eg
--
nums = [1,2,3,4]
print(type(nums))
all_n = tuple(nums)
print(type(all_n))

tuple
---
list -- list()
string -- str()
eg
--
nums = [1,2,3,4]
print(type(nums))
all_n = list(nums)
print (all_n)
print(type(all_n))

string -- str()
eg--
nums = [1,2,3,4]
print(type(nums))
all_n = str(nums)
print(type(all_n))

(+) -- Concatination
--------------------
eg--
Integers--
num1=3
num2=6
print(num1+num2)

strings--
s1='python is a'
s2=' language'
print(s1+s2)

list--
num=[1,2]
all_=[3,4]
print(num+all_)























