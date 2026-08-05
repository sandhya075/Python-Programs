'''
Anonymous function
---------------
--> Anonymous function is a function that don't that don't any name
--> This is also called as lambda function
--> Lambda function will take n number arguments but only one expression

syntax --> lambda arguments : expression
eg
--
so = lambda a,b,c : a+b+c
print(so(2,45,6))

map()
----
--> The map function will be applied on the given functions of each and every element of of an iterable
eg
--
nums = [1,2,3,4,5]
so = list(map(lambda x: x+2==(),nums))
print(so)

filter()
--------
--> filter function will only consider if the condition is true, then it will keep that values...
eg
--
nums = [1,2,3,4,5]
so = list(filter(lambda x: x+2==(),nums))
print(so)

reduce
-------
--> The ruduce() function consider all elemnts an reduce to one single
eg
--
from functools import reduce
nums = [1,2,3,4,5]
so = reduce(lambda x,y : x+y,nums)
print(so)

print()
------
--> print() is an inbuilt dunction that is used to display purpose and display the values stored by variable

return()
--------
--> Only used inside the functions
--> when the return executed then it will exit from that function and holds the returned values in the calling




'''

from functools import reduce
nums = [1,2,3,4,5]
so = reduce(lambda x,y : x+y,nums)
print(so)

