elif
----
eg1-- Grade
marks_=int(input())
if marks_>=90:
    print('A+')
elif marks_>=80:
    print('B+')
elif marks_>=70:
    print('C+')
elif marks_>=35:
    print('Pass')
else:
    print('Fail')

eg2-- Greater number
num1=int(input())
num2=int(input())
num3=int(input())
if num1>num2 and num1>num3:
    print(num1,'is greater value')
elif num2>num1 and num2>num3:
    print(num2,'is greater value')
else:
    print(num3,'is greater value')


nested if
---------
eg--
details={'ATMPIN' : '2002'}
atm=input('Enter your 4 digit atm pin: ')
if len(atm)==4:
    if atm==details['ATMPIN']:
        opt=int(input('1.Enter \n1.Withdraw\n2.Deposite \n3.pinchange\n'))
        if opt==1:
            money_w=int(input('Enter money to withdraw: '))
        elif opt==2:
            money_d=int(input('Enter money to deposite: '))
    else:
        print('Icorrect pin entered')
else:
    print('Please enter only 4 digit pin')

    
--> control statements

1.break
------
eg
--
num = [34,67,90,107,56]
for i in num:
    print(i)
    if i == 90:
        break
else:
    print('end')

2.continue
-----
--skips the particular part
eg
--
num = [34,67,90,107,56]
for i in num:
    if i == 90:
        continue
    print(i)
else:
    print('end')

3.pass
-----
eg
--
num = [34,67,90,107,56]
for i in num:
    if i == 90:
        pass


 -->loops

1.for loop
-------
-- for loop is used to iterate over sequence such as str,list,tuple
--else in for loop it will execute when whole itterates are completed..
--incase if condition becomes true, then else will never execute..

--range()
---------
-- range function is used to generate numbers upto a limit...
syntax -- range(start,end,step)
eg
--
for j in range(1,101):
    print(j)

2.while loop
---------
-- it is combination for and if condition
eg
--
num = 1
while num < 10:
    print(num)
    num +=1

-->Assert keyword
--------------
-- the keyword is used to check the condition









    
