'''
Listcomprehension
-----------------
--> the comprehension is the short form of syntax used to generate a new list from the old list....

syntax --> [Expression loop]
eg1
--

nums = [1,2,3,4,5]
new_l = [j if j % 2 == 0 else 'odd' for j in nums]
print(new_l)
eg2
--
nums = [1,2,3,4,5]
nel_ = [i for i in nums if i % 2 !=0]
print(nel_)

Nested comprehension
--------------------
--> Nested comprehension mmeans an comprehension inside the another comprehension is called nested comprehension
syntax--> [expression loop_1 and loop_2]
eg1
---

match1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
any_ = [i for i in match]
all_ = [num for j in match for num in j]
print(any_)
print(all_)

eg2
--
new_ = [[i*j for j in range(1,6)] for i in range(1,6)]
ne = [i for i in range(1,6)]
print(ne)
print(new_)

Generator(lazor evalution)
--------------------------
--> This generate will generate values one at time and the pause it on the same position when we are using yield keyword
--> here we will use yield to get the value

Yield keyword
-------------
--> this yeild() will used to get the value and will only gives one value and pauses there itself

Next keyword
------------
--> the next() will retrive the value
def gen(n):
    for i in range(1,n+1):
        yield i*i
a = gen(5)
print(next(a))
print(next(a))
print(next(a))

Function
--------
--> return
--> when the return executed , it will exit for the fucntion
--> in function will get all values once

Generator
---------
--> yield
--> When the yield is excuted ,it will pause the function  and the next yield is called then it will resume again
--> in generator we will get one at a time..

'''
