
'''
Data analysis
-------------
--> Data anlysis is the process of analysis the data collacetion cleaning transforming,organizing, and analyzing data to convert into useful information... and also used for maikng decisions
 to get the better outcome...

--> library used
----------------
numpy
pnadas
matplotlib
seaborn

numpy
----
--> this refers to nummerical python
--> it is pyhon library used for calculate the the operations
--> this python library is more faster than the list to the operations to perform operations
--> An also supports multidimensional arrays

eg
---
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr.ndim)
eg2
--
import numpy as np
arr_2 = np.array([1,2,3,4,5])
print(arr_2.ndim)
arr_3 = np.array([
    [1,2,3],
    [4,5,6],
    

])
print(arr_3.shape)


functions
---------
--> the functions is used to find out the dimensions of an array
synatx--> array.ndim
eg
--
import numpy as np
arr_2 = np.array([1,2,3,4,5])
print(arr_2.ndim)

shape
------
--> the shape function is used to find the rows and colomns of an arary
syntax --> array.shape
eg
--
import numpy as np
arr_2 = np.array([1,2,3,4,5,6])
print(arr_2.reshape(2,3))

reshape
-------
--> the function can used to convert one dimensions to another if the the elemnts are there to convert into the any dimension
--> synatx --> array.reshape(row,col)
eg
--


eg
--
import numpy as np
arr_2 = np.array([1,2,3,4,5,6])
print(arr_2.reshape(2,3))
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr.reshape(3,3))

size
----
--> the size function is used to findout the the number pof elements present in the array
--> synatx --> array.size
eg
--
import numpy as np
arr_2 = np.array([1,2,3,4,5,6])
print(arr_2.size)

operations
-----------
--> same as list we can also perform some operations are arrays
1.indexing
----------
eg
--
import numpy as np
arr_2 = np.array([1,2,3,4,5,6])
print(arr_2[5])

2.slicing
----------
eg
--
import numpy as np
arr_2 = np.array([1,2,3,4,5,6])
print(arr_2[2:5])

3.sum
-----
eg
--
import numpy as np
arr_2 = np.array([1,2,3,4,5,6])
print(arr_2.sum())

4.add
-----
eg
--
import numpy as np
arr_2 = np.array([1,2,3,4,5,6])
arr = np.array([7,8,9,10,11,12])
print(arr_2 + arr)
eg2
---
import numpy as np
arr_2 = np.array([1,2,3,4,5,6])
arr = np.array([7,8,9,10,11,12])
print(arr_2 + arr)
print(arr_2 + 5)

5.sub
------
eg
--
import numpy as np
arr_2 = np.array([1,2,3,4,5,6])
arr = np.array([7,8,9,10,11,12])
print(arr_2 - arr)
print(arr - 5)

6.mul
-----
eg
----
import numpy as np
arr_2 = np.array([1,2,3,4,5,6])
arr = np.array([7,8,9,10,11,12])
print(arr_2 - arr)
print(arr - 5)

7.**(power)
----
eg
__
import numpy as np
arr_2 = np.array([1,2,3,4,5,6])
print(arr_2 **3)
8.max()
-------

eg
--
import numpy as np
arr_2 = np.array([1,2,3,4,5,6,15])
print(arr_2.max())

Arange
------
--> arange function is used to generate the numbers in a sequence upto certain  a limit and that can beit forms one dimensional array
--> this array can be reshaped can convert into 2D arrys by using reshape
syntax --> np.aranhge(range)
eg
--
import numpy as np
arr_ = np.arange(1,10)
print(arr_.reshape(3,3))
print(arr_)






























