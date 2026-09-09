'''



name = "codegnan"
batch = 23
email_id = "saketh@codegnan.com"
print(len(email_id[7:15]))

email_ids = ['sandhyapyla075@gmail.com','pylasandhya773@gmail.com','pylapadma@gmail.com','maheshbotta@gmail.com']
print(len(email_ids))
print(email_ids[1])
print(type(email_ids[-2:-1]))

#store 3 more mailids into above at a time

email_ids.extend([1,2,3])
print(email_ids)
#access each mail id one by one -->loops

for mail in email_ids:
    print(mail)
    print(f'mailid of person is {mail}')
users = {}
print(type(users))
#get the above emailids with relevant user dctionary

users = dict.fromkeys(email_ids)
users['sandhyapyla075@gmail.com'] = 2345
print(users)
#all python built-in-functions datatypes are built-in-functions

#(int,float,str,list,tuple,dict,set,bool)

print(users)
for i in range(len(email_ids)):
    #print(i,email_ids[i])
    users[i] = email_ids[i]
print(users)
#enumerate --> it provides by default a counter object (you can store )

#desired collection)

data = dict(enumerate(email_ids,1))
print(data)

#python --> object
#functions --> first class objects
# a set is a unordered collection as no indexing


s = 'LEARNING PYTHON IS VERY EASY'
s1 = s.split(' ')
res=''
for i in s1:
    res=i+' '+res
print(res)
r = ''
for i in s:
    r=i+r
print(r)

n=len(a)
even=""
odd=""
for i in range(n):
    if i%2==0:
        even+=a[i]
    else:
        odd+=a[i]
print(even)
print(odd)
'''
s = 'sandhya'
v=len(s)
r=''
for i in range(1,v,3):
    print(s[i],end='')
    













