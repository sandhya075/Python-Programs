factorial
---------
--> it will give factorial value
 eg
 -----
import math
print(math.factorial(5))

import math
print(math.log(2,3))
print(math.cos(math.pi))
print(math.pi)

random
-------
--> therandom module used to get the random number

import random
print(random.randint(1,100))

randint
-------
--> used to generate random nubers based on the range
eg
----

import random
color = ['red','green','blue','yellow']
print(random.choice(color))
random.shuffle(color)
print(color)

choice
-----
--> it will give the random value from the given data
eg
-----
import random
color =['red','blue','yellow']
print(random.choice(color))

shuffle
-----
--> it will shuufle the data randomly

import random
color = ['red','green','blue','yellow']
print(random.choice(color))
random.shuffle(color)
print(color)

uniform
-----
--> will give the decimal values in a range given
eg
----
import random
print(random.uniform(1,100))


sys
-----
--> sys module is used to ger details of python interperter
import sys
print(sys.version)
print(sys.path)



version
------
--> the version of python interpreter
eg
----
import sys
print(sys.version)
path
----
--> .py path will get by this function
eg
---
import sys
print(sys.platform)

exit
-------
--> this function will exit from the program
eg
-----

import sys
print(sys.exit())

platform
------
--> it will gives the python run platform
eg
----
impot sys
print(sys.platform)

argv
-----
--> it will give the current file run path
eg
----
import sys
print(sys.argv)

datetime
-------
--> used to work with date and time
eg
----
from datetime import datetime,date,time
print(datetime.now())
print(datetime.today)

now
----
--> it will give the today time+date
eg
---
from import datetime
print(datetime.now())

from datetime import datetime
now =datetime.now()
print(now.strftime('%y-%m'))
print(now.strftime("%A"))
print(now.strftime("%B"))
print(now.strftime("%H:%M:%S"))
print(now.strftime("%Y-%m-%d"))

%y ---> will get the year
%m ---> will get the month
%d ---> will get the dat
%h ---> will get the hour
%m --> will get the minute
%s ---> will get the second
%A ---> current day
%B ---> current month

collections
----------
--> the collections module will provide container type data which is more powerfull than buil-in data types(dict,list,tuple
eg
-----
import collections
data = ['apple','banana','orange','pineapple']
print(collections.counter(data))

deque
------
--> used to work with list
eg
------

from collections import deque
how = deque([1,2,3])
how.appendleft(7)
print(how)

extend
-------
from collections import deque
how = deque([1,2,3])
how.extend([4,5,6])
print(how)
pop
------
eg
----
from collections import deque
how = deque([1,2,3])
how.pop()
print(how)

named tuple
-----
eg
-----
from collections import namedtuple
data = namedtuple("stu",('name','age'))
print(data('john','18'))

import itertools
------

from itertools import count
c = count(100)
for j in range(5):
    print(next(c))

count
----

import itertools 
for j in itertools.repeat('python',10):
   print(j)

 permutations
 -----
 eg
 -----
from itertools import permutations

data = permutations ([1,2,3],2)
print(list(data))

combinations
-------
eg
----

from itertools import combinations

any_ = combinations([1,2,3],2)
print(list(any_))
'''
import platform
print(platform.python_version())
print(platform.python_compiler())
print(platform.machine())
print(platform.processor())
