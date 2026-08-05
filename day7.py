'''
2. F-String (doc-string)
----
eg
---
name = 'sandy'
age = 22
print('WElCOME',name,'your age is',age)

%
---
%s --> all
--
eg
--
print('name : %d' % name)
price = 89

%d --> digit
eg
--
price = 89
print('name : %d' % name)
%f --> float
eg
--
price = 89
print('name : %f' % name)



name = 'sandy'
age = 89
print('name : {} \nage : {}'.format(name,age))


If condition
---------
--> the if condition is used to check it is true or false
eg
--
age = int(input()("Enter your age: "))
if age >=18:
print(f"your age is {age} and eligible to vote")

if-else
----
--> else is the fall back statement, incase if condition is false then this else block will execute...
eg
--
age = int(input()("Enter your age: "))
if >=18:
print(f"your age is {age} and eligible to vote")
else:
print(f"your age is {age}, you have to wait {18 - age} years")
so = 'madam'
do = so[::-1]
print(do)
if so[::-1] == so:
print(f' {so} is a pali
else:
print(f' {so} not a pali')
eg
--leap year or not

year_ = int(input("Enter a year: "))
if year_% 4 == 0 and year_% 100 != 0 or year_ % 400 == 0:
     print(f'{year_} is a leap')
else:
     print(f'{year_} not a leap')



'''
year_ = int(input("Enter a year: "))
if year_% 4 == 0 and year_% 100 != 0 or year_ % 400 == 0:
     print(f'{year_} is a leap')
else:
     print(f'{year_} not a leap')





