7 * 1 = 7
7 * 2 = 14
tab_ = int(input('Enter a num: '))
for j in range(1,11):
    print('f'{tab_} x {j} = {tab_*j})


num = 153
length_ =len(str(num)0
am_ = 0
for j in str(num):
am_ = int(j) ** length_ + am_
if am_ == num:
    print(f'{num} is Amstrong')
else:
    print(f'{num} is not')

num_2  = 1
print(num,num_2,end='')
for j in range(1,limit_+1):
    all_ad = num + num_2
    num_2 = all_ad
    print(all_ad,end='')
 
num_1 = int(input('Enter a num: '))
num_2 = int(input('Enter a num:'))
opt_ = int(input('Enter \n1.Add \n2.sub: '))
if opt_ == 1:
print(num_1 + num_2)
elif opt_ == 2:
    print(num_1 = num_2)
   

enter atm pin
ICIC_Santhi={'name':'Sandy',
             'addhar':'454323456',
             'Pan':'3er345678g',
             'ATM_PIN':'2020',
             'Balance':5000}
remain_A=3
while remain_A>0:
        pin_=input('Enter your atm pin: ')
        if len(pin_)==4:
                if pin_ in ICIC_Sandy['ATM_PIN']:
                        opt_=int(input('Enter \n1.Withdraw \n2.Deposite \n3.Balance : \n'))
                        if opt_==1:
                                withdraw_m=int(input('Enter amount you want to withdraw: '))
                                if withdraw_m<=ICIC_Sandy['Balance'] and withdraw_m%100==0:
                                        ICIC_Santhi['Balance']-=withdraw_m
                                        print(f'You have withdraw {withdraw_m} and the total balance {ICIC_Santhi['Balance']}')
                                        break
                                else:
                                        print('Can not provide change or no balance')
                                        break
                else:
                    remain_A-=1
                    if remain_A>0:
                        print(f'Incorrect pin and you have only {remain_A}')
                    else:
                        print('Your card is block')
                        break
        else:
                print(Please enter only 4 digit a
    
'''
ICIC_Santhi={'name':'Santhi',
             'addhar':'454323456',
             'Pan':'3er345678g',
             'ATM_PIN':'2020',
             'Balance':5000,
             'Transaction History':[]}
remain_A=3
withdraw=0
deposite=0
while remain_A>0:
        pin_=input('Enter your atm pin: ')
        if len(pin_)==4:
                if pin_ in ICIC_Santhi['ATM_PIN']:
                        opt_=int(input('Enter \n1.Withdraw \n2.Deposite \n3.Check Balance \n4.Transaction History \n5.Pin change: \n'))
                        if opt_==1:
                                withdraw_m=int(input('Enter amount you want to withdraw: '))
                                if withdraw_m<=ICIC_Santhi['Balance'] and withdraw_m%100==0:
                                        ICIC_Santhi['Balance']-=withdraw_m
                                        withdraw=withdraw_m
                                        print(f'You have withdraw {withdraw_m} and the total balance {ICIC_Santhi['Balance']}')
                                        user_=int(input('Enter  \n1.Homepage \n2.Exit: \n'))
                                        if user_==1:
                                                print('Home page')
                                        else:
                                                print('Thank you for visiting')
                                                break
                                else:
                                        print('Can not provide change or no balance')
                                        break
                        elif opt_==2:
                                deposite_m=int(input('Enter the money you want to deposite: '))
                                if deposite_m%100==0:
                                        ICIC_Santhi['Balance']+=deposite_m
                                        print(f' You have deposite {deposite_m} and the total balance {ICIC_Santhi['Balance']}')
                                        deposite=deposite_m
                                        user_=int(input('Enter  \n1.Homepage \n2.Exit: \n'))
                                        if user_==1:
                                                print('Home page')
                                        else:
                                                print('Thank you for visiting')
                                                break
                                else:
                                        print('Change can not be deposite')
                                        break
                        elif opt_==3:
                                print(f'Balance is {ICIC_Santhi['Balance']}')
                                user_=int(input('Enter  \n1.Homepage \n2.Exit: \n'))
                                if user_==1:
                                        print('Home page')
                                else:
                                        print('Thank you for visiting')
                                        break
                                
                        elif opt_==4:
                                print(f'Transaction history withdraw amount:{withdraw} deposite amout:{deposite}')
                                
                                user_=int(input('Enter  \n1.Homepage \n2.Exit: \n'))
                                if user_==1:
                                        print('Home page')
                                else:
                                        print('Thank you for visiting')
                                        break
                                
                        elif opt_==5:
                                pass
                else:
                    remain_A-=1
                    if remain_A>0:
                        print(f'Incorrect pin and you have only {remain_A}')
                    else:
                        print('Your card is block')
                        break
        else:
                print('Please enter only 4 digit atm pin')
'''
ICIC_Santhi={'name':'Santhi',
             'addhar':'454323456',
             'Pan':'3er345678g',
             'ATM_PIN':'2020',
             'Balance':5000,
             'Transaction History':[]}
remain_A=3
withdraw=0
deposite=0
while remain_A>0:
        pin_=input('Enter your atm pin: ')
        if len(pin_)==4:
                if pin_ in ICIC_Santhi['ATM_PIN']:
                        opt_=int(input('Enter \n1.Withdraw \n2.Deposite \n3.Check Balance \n4.Transaction History \n5.Pin change: \n'))
                        if opt_==1:
                                withdraw_m=int(input('Enter amount you want to withdraw: '))
                                if withdraw_m<=ICIC_Santhi['Balance'] and withdraw_m%100==0:
                                        ICIC_Santhi['Balance']-=withdraw_m
                                        withdraw=withdraw_m
                                        print(f'You have withdraw {withdraw_m} and the total balance {ICIC_Santhi['Balance']}')
                                        user_=int(input('Enter  \n1.Homepage \n2.Exit: \n'))
                                        if user_==1:
                                                print('Home page')
                                        else:
                                                print('Thank you for visiting')
                                                break
                                else:
                                        print('Can not provide change or no balance')
                                        break
                        elif opt_==2:
                                deposite_m=int(input('Enter the money you want to deposite: '))
                                if deposite_m%100==0:
                                        ICIC_Santhi['Balance']+=deposite_m
                                        print(f' You have deposite {deposite_m} and the total balance {ICIC_Santhi['Balance']}')
                                        deposite=deposite_m
                                        user_=int(input('Enter  \n1.Homepage \n2.Exit: \n'))
                                        if user_==1:
                                                print('Home page')
                                        else:
                                                print('Thank you for visiting')
                                                break
                                else:
                                        print('Change can not be deposite')
                                        break
                        elif opt_==3:
                                print(f'Balance is {ICIC_Santhi['Balance']}')
                                user_=int(input('Enter  \n1.Homepage \n2.Exit: \n'))
                                if user_==1:
                                        print('Home page')
                                else:
                                        print('Thank you for visiting')
                                        break
                                
                        elif opt_==4:
                                print(f'Transaction history withdraw amount:{withdraw} deposite amout:{deposite}')
                                
                                user_=int(input('Enter  \n1.Homepage \n2.Exit: \n'))
                                if user_==1:
                                        print('Home page')
                                else:
                                        print('Thank you for visiting')
                                        break
                                
                        elif opt_==5:
                                pass
                else:
                    remain_A-=1
                    if remain_A>0:
                        print(f'Incorrect pin and you have only {remain_A}')
                    else:
                        print('Your card is block')
                        break
        else:
                print('Please enter only 4 digit atm pin')
'''
                      

ICIC_Santhi={'name':'Santhi',
             'addhar':'454323456',
             'Pan':'3er345678g',
             'ATM_PIN':'2020',
             'Balance':5000,
             'Transaction History':[]}
remain_A=3
withdraw=0
deposite=0
while remain_A>0:
        pin_=input('Enter your atm pin: ')
        if len(pin_)==4:
                if pin_ in ICIC_Santhi['ATM_PIN']:
                        opt_=int(input('Enter \n1.Withdraw \n2.Deposite \n3.Check Balance \n4.Transaction History \n5.Pin change: \n'))
                        if opt_==1:
                                withdraw_m=int(input('Enter amount you want to withdraw: '))
                                if withdraw_m<=ICIC_Santhi['Balance'] and withdraw_m%100==0:
                                        ICIC_Santhi['Balance']-=withdraw_m
                                        withdraw=withdraw_m
                                        print(f'You have withdraw {withdraw_m} and the total balance {ICIC_Santhi['Balance']}')
                                        user_=int(input('Enter  \n1.Homepage \n2.Exit: \n'))
                                        if user_==1:
                                                print('Home page')
                                        else:
                                                print('Thank you for visiting')
                                                break
                                else:
                                        print('Can not provide change or no balance')
                                        break
                        elif opt_==2:
                                deposite_m=int(input('Enter the money you want to deposite: '))
                                if deposite_m%100==0:
                                        ICIC_Santhi['Balance']+=deposite_m
                                        print(f' You have deposite {deposite_m} and the total balance {ICIC_Santhi['Balance']}')
                                        deposite=deposite_m
                                        user_=int(input('Enter  \n1.Homepage \n2.Exit: \n'))
                                        if user_==1:
                                                print('Home page')
                                        else:
                                                print('Thank you for visiting')
                                                break
                                else:
                                        print('Change can not be deposite')
                                        break
                        elif opt_==3:
                                print(f'Balance is {ICIC_Santhi['Balance']}')
                                user_=int(input('Enter  \n1.Homepage \n2.Exit: \n'))
                                if user_==1:
                                        print('Home page')
                                else:
                                        print('Thank you for visiting')
                                        break
                                
                        elif opt_==4:
                                print(f'Transaction history withdraw amount:{withdraw} deposite amout:{deposite}')
                                
                                user_=int(input('Enter  \n1.Homepage \n2.Exit: \n'))
                                if user_==1:
                                        print('Home page')
                                else:
                                        print('Thank you for visiting')
                                        break
                                
                        elif opt_==5:
                                pass
                else:
                    remain_A-=1
                    if remain_A>0:
                        print(f'Incorrect pin and you have only {remain_A}')
                    else:
                        print('Your card is block')
                        break
        else:
                print('Please enter only 4 digit atm pin')
'''
ICIC_Santhi={'name':'Santhi',
             'addhar':'454323456',
             'Pan':'3er345678g',
             'ATM_PIN':'2020',
             'Balance':5000,
             'Transaction History':[]}
remain_A=3
withdraw=0
deposite=0
while remain_A>0:
        pin_=input('Enter your atm pin: ')
        if len(pin_)==4:
                if pin_ in ICIC_Santhi['ATM_PIN']:
                        opt_=int(input('Enter \n1.Withdraw \n2.Deposite \n3.Check Balance \n4.Transaction History \n5.Pin change: \n'))
                        if opt_==1:
                                withdraw_m=int(input('Enter amount you want to withdraw: '))
                                if withdraw_m<=ICIC_Santhi['Balance'] and withdraw_m%100==0:
                                        ICIC_Santhi['Balance']-=withdraw_m
                                        withdraw=withdraw_m
                                        print(f'You have withdraw {withdraw_m} and the total balance {ICIC_Santhi['Balance']}')
                                        user_=int(input('Enter  \n1.Homepage \n2.Exit: \n'))
                                        if user_==1:
                                                print('Home page')
                                        else:
                                                print('Thank you for visiting')
                                                break
                                else:
                                        print('Can not provide change or no balance')
                                        break
                        elif opt_==2:
                                deposite_m=int(input('Enter the money you want to deposite: '))
                                if deposite_m%100==0:
                                        ICIC_Santhi['Balance']+=deposite_m
                                        print(f' You have deposite {deposite_m} and the total balance {ICIC_Santhi['Balance']}')
                                        deposite=deposite_m
                                        user_=int(input('Enter  \n1.Homepage \n2.Exit: \n'))
                                        if user_==1:
                                                print('Home page')
                                        else:
                                                print('Thank you for visiting')
                                                break
                                else:
                                        print('Change can not be deposite')
                                        break
                        elif opt_==3:
                                print(f'Balance is {ICIC_Santhi['Balance']}')
                                user_=int(input('Enter  \n1.Homepage \n2.Exit: \n'))
                                if user_==1:
                                        print('Home page')
                                else:
                                        print('Thank you for visiting')
                                        break
                                
                        elif opt_==4:
                                print(f'Transaction history withdraw amount:{withdraw} deposite amout:{deposite}')
                                
                                user_=int(input('Enter  \n1.Homepage \n2.Exit: \n'))
                                if user_==1:
                                        print('Home page')
                                else:
                                        print('Thank you for visiting')
                                        break
                                
                        elif opt_==5:
                                pass
                else:
                    remain_A-=1
                    if remain_A>0:
                        print(f'Incorrect pin and you have only {remain_A}')
                    else:
                        print('Your card is block')
                        break
        else:
                print('Please enter only 4 digit atm pin')

                      
                      
'''
ICIC_Santhi={'name':'Santhi',
             'addhar':'454323456',
             'Pan':'3er345678g',
             'ATM_PIN':'2020',
             'Balance':5000,
             'Transaction History':[]}
remain_A=3
withdraw=0
deposite=0
while remain_A>0:
        pin_=input('Enter your atm pin: ')
        if len(pin_)==4:
                if pin_ in ICIC_Santhi['ATM_PIN']:
                        opt_=int(input('Enter \n1.Withdraw \n2.Deposite \n3.Check Balance \n4.Transaction History \n5.Pin change: \n'))
                        if opt_==1:
                                withdraw_m=int(input('Enter amount you want to withdraw: '))
                                if withdraw_m<=ICIC_Santhi['Balance'] and withdraw_m%100==0:
                                        ICIC_Santhi['Balance']-=withdraw_m
                                        withdraw=withdraw_m
                                        print(f'You have withdraw {withdraw_m} and the total balance {ICIC_Santhi['Balance']}')
                                        user_=int(input('Enter  \n1.Homepage \n2.Exit: \n'))
                                        if user_==1:
                                                print('Home page')
                                        else:
                                                print('Thank you for visiting')
                                                break
                                else:
                                        print('Can not provide change or no balance')
                                        break
                        elif opt_==2:
                                deposite_m=int(input('Enter the money you want to deposite: '))
                                if deposite_m%100==0:
                                        ICIC_Santhi['Balance']+=deposite_m
                                        print(f' You have deposite {deposite_m} and the total balance {ICIC_Santhi['Balance']}')
                                        deposite=deposite_m
                                        user_=int(input('Enter  \n1.Homepage \n2.Exit: \n'))
                                        if user_==1:
                                                print('Home page')
                                        else:
                                                print('Thank you for visiting')
                                                break
                                else:
                                        print('Change can not be deposite')
                                        break
                        elif opt_==3:
                                print(f'Balance is {ICIC_Santhi['Balance']}')
                                user_=int(input('Enter  \n1.Homepage \n2.Exit: \n'))
                                if user_==1:
                                        print('Home page')
                                else:
                                        print('Thank you for visiting')
                                        break
                                
                        elif opt_==4:
                                print(f'Transaction history withdraw amount:{withdraw} deposite amout:{deposite}')
                                
                                user_=int(input('Enter  \n1.Homepage \n2.Exit: \n'))
                                if user_==1:
                                        print('Home page')
                                else:
                                        print('Thank you for visiting')
                                        break
                                
                        elif opt_==5:
                                pass
                else:
                    remain_A-=1
                    if remain_A>0:
                        print(f'Incorrect pin and you have only {remain_A}')
                    else:
                        print('Your card is block')
                        break
        else:
                print('Please enter only 4 digit atm pin')
'''
                      
                      


                      
                      
