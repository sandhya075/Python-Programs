'''
EXCEPTION HANDLING
------------------
--> An error can be handled by try and except
1.try:
------
--> we can check the code here which may contain any  error
eg:
---
try:
try:
    print(n)
except:
    print('some error')

    
2.except:
--------
--> exception can handle any error that come in the try block
eg
--
try:
    num = 0
    num_2 = 
    print(num_2 / num)
except:
    print('will get an error')
num = 8
num_2 = 0
print(num / num_2)
eg2
--
try:
    print(9+'python')
except:
    print('error')

3.else:
-------
--> if no error in the code were raised, then the else block
will execute
eg
--
try:
    print(9/0)
    print(num)
except ZeroDivisionError:
    print('This will raise ZeroDivisionError')
except NameError:
    print('This will raise NameError')
else:
    print('no error')
4.finally:
---------
--> the finally block will execute if error present in the try block or not
eg
try:
    print('hello')
except ZeroDivisionError:
    print('This will raise ZeroDivisionError')
except NameError:
    print('This will raise NameError')
except TypeError:
    print('This will raise Typeerror')
else:
    print('no error')
finally:
    print('end')


FILE HANDLING
-------------
---> an file handler is an object used to connect with that particular file...
1.with (keyword)
----------------
--> by using with keyword no need close the file, it will close itself
syntax
------
by file name
------------
with open('file_name or path','mode') as name:
by file path
------------
with open('r file_path','mode') as name
2.open()
--------
--> by using this open() we have to close the file by using close()
eg
--
any_ = open('demo.text','r')
print(any_.read())
any_.close()

modes
-----
1.'r'
-----
--> the r mode is used for functions readline() and readlines()
eg
--
with open('demo.txt', 'r') as file:
    print(file.read())
    

2.'w'
-------
--> the 'w' mode is used for write() function

3.'a'
-----
--> the 'a' mode is used to for write() function and it will and the text at the last position
eg
--
with open('demo.text', 'a') as file:
    file.write('python module take 2 hour per day')

    


4.'x'
-----
eg
--

with open('dem.txt', 'x') as file:
    file.write('python module take 2 hour per day')

    
-->
function
--------
1.write()
2.read()
--------
--> the function() will read the file read by chunk by chunk  where we can specicify the size
eg
--
with open('dem.txt','r') as file:
    print(file.read(20))

3.readline()
------------
---> read line reads the at a time with open
eg
--
with open('dem.txt','r') as file:
    print(file.readline())
    

4.readlines()
--------------
--> the readlines() will read whole file and written it in a list, where each line is one index in the list
eg
--
with open('dem.txt','r') as file:
    print(file.readlines(20))
    

'''



