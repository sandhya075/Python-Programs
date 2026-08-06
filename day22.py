'''


print(string.ascii_letters)
print(string.digits)
print(string.punctuations)
# asscii_letters --> this string module function that can give
# upper and lpwer letters
# digits ---> string module function that can give number(0-9)
# punctuation --> this string module function can give us
# punctiontion(&$@)
import random
import string
letters = string.ascii_letters
digits = string.digits
punctuation = string.punctation

all_chars = letters + digits + special_char

password = ''
for i in range(5):
    password +=random.choice(all_chars)
    print(pasword)

bank_balance = 10000
from datetime import datetime
import sys
now = datetime.now()
while True:
    print("----Welcome to SBI ATM----")
    user_otp = int(input(" \n1.withdraw \n2.Deposit \n3.check \n4.Exit"))
    if user_otp == 1:
        with_m = int(input('Enter the money you want to withdraw: '))
        if with_m < bank_balance:
            bank_balance -= with_m
            print(f"remaining money {bank_balance} {now.strftime("%H%M %y-%m-%d")}")
        else:
            print('insufficient money')
    elif user_otp == 2:
        Deposite_m = int(input('Enter the money you want to deposite: '))
        bank_balance += Deposite_m
        print(f"Money added successfully: {bank_balance} {now.strftime("%H%M %y-%m-%d")}")
    elif user_otp == 3:
        print(f"Available balance: bank balance) {now.strftime("%H%M %y-%m-%d")}")
    elif user_otp == 4:
        sys.exit()
    else:
        print("incorrect choice")
        print("Thank for visiting the ATM")
        sys.exit()
                  

import_random
-------------
'''
import random
num = random.randint(1,100)
user_otp = int(input("pick a number(1-100): "))
if user_otp == num:
    print(f'you have picked {user_otp} number')
else:
    print('Better luck next time')
                         











