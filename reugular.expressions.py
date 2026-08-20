
'''
Regular Expressions
-------------------
--> This RegEx is used form a search pattern to find out the string contain sequence of chracters char or not
--> To use this RegEx , we need to import re module

Functions
---------
findall
-------
--> The searching pattern is found then , it will gives the o/p in the list[]
eg
--
import re
some = 'python is a programming language'
print(re.findall('[a]',some))

search
-----
--> this is also used to form a search pattern, but it will give only the first matched object
--> where it will gives with the index position, where the matched object is found by the pattern 
eg
--
import re
do = 'I hvae 1000 ruppees with me'
print(re.search('e',do))

meta characters
---------------
-->meta characters are the symbols used in the search pattern
1.[]
--> this [] symbol is used find a group char that present in the string, where we cn also specify the range
syntax --> re.findall('[range]',variable_name)
--> by using this we can search cap(A-Z), small(a-z) and digit(0-9)
eg
--
import re
some = 'we are in class'
print(re.findall('[aguo]',some))
eg2
--
import re
some = 'we are in class'
print(re.findall('[aguo]',some))
print(re.search('[a-z]',some))


2. .
. char
-------
--> this symbol will refer only one means can match only  a single char in the pattern...
--> syntax -->  re.search('c...',variable_name)
eg
--
import re
some = 'Hello World'
print(re.findall('H...o',some))
print(re.search('H..',some))


3. ^
----
--> this symbol is used find the pattern where string starting match or not
syntax --> re.finall('^', variable_name)
eg
--
import re
some = 'Hello! World'
print(re.findall('^HEllo',some))
print(re.search('^Hello',some))

4. $
-----
--> this symobol will find out if the string is ending with pattern or not
syntax--> re.findall('sequence$', variable_name)
eg
--
import re
any_ = 'I am planning for a trip'
print(re.findall('for a trip$',any_))
print(re.search('for a trip$',any_))


5.{}
----
--> the symbol is used to find a group char that present in string
syntax--> re.findall('E.{size}', variable_name)
eg
---
import re
all_ = 'I have 1000 ruppees with me'
print(re.findall('I.{2}',all_))
6.?
---
--> the symbol will find  max upto 1 match in the string
syntax --> re.findall('.?',variable_name)
eg
--
import re
some = 'Hello! World Hello'
print(re.findall('Hel.?o',some))
7.*
----
--> the symbol max number of sequnce from the string
syntax --> re.findall('.*',variable_name)

eg
--
import re
some = 'the symbol is used to find a group char that present'
print(re.findall('T.*r',some))

8.+
---
--> the symbol can find max no of things from alleast one character
--> syntax--> re.findall('.+', variable_name)


















