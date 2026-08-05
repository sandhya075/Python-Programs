
1.PRINT NAME 1515 TIMES
------------------------
O/P:
name = "sandhya"
for i in range(1515):
print(i,name)

2.PRINT 5&3 and 6&9
-------------------
O/P:
a = 5
b = 3
result1 = (a&b)
print("5&3 =",result1)
a = 6
b = 9
result2 = (a&b)
print("6&9 =",result2)

3.PRINT STAR PROGRAM
-------------------
***
***
***
O/P:

for i in range(3):
    for j in range(3):
        print("*",end="")
    print()


4.PROGRAM TO PRINT THE STAR PATTERN
----------------------------------------
*****
****
***
**
*
**
***
****
*****
O/P:
n = int(input('Enter num:'))
for j in range(n):
    print('*'*(n-j), end='')
    print()
for j in range(1,n):
    print('*'*(j+1), end='')
    print()



5.PRINT NUMBERS
--------------
1
12
123
1234
12345
1234
123
12
1
O/P:
n = int(input('Enter a number: '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print()
for i in range(n-1,0,-1):
     for j in range(1,i+1):
        print(j,end='')
     print()



6.PRINT IN ORDER ALPHABETS
---------------------------
A
AB
ABC
ABCD
ABCDE
ABCD
ABC
AB
A
AB
ABC
ABCD
ABCDE
O/P:
s = input('Enter alphabets: ')
l=len(s)
for i in range(l):
    for j in range(i+1):
        print(s[j],end='')
    print()
for i in range(l-1, 1, -1):
    for j in range(i):
        print(s[j],end='')
    print()
for i in range(l):
    for j in range(i+1):
        print(s[j],end='')
    print()









