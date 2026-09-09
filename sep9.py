




Number List Analyser
--------------------
numbers=[20,10,30,20,40,20]
#sort the list in ascending order
numbers.sort()
#print(numbers)
numbers.reverse() #reverse to descending order
#print(numbers)
#ask user for a number to search in the list
num=int(input('Enter a number to search: '))
if num in numbers:
    print('Number found')
    print('Count: ', numbers.count(num))#count of the search element in list
    print('First index: ',numbers.index(num))#index of the search element in the list
else:
    print('Number not found')
print('smallest value: ',min(numbers))
print('Largest value: ',max(numbers))
print('Total: ', sum(numbers))


Even and Odd numbers separator
-------------------------------
numbers=[10,15,20,30,35]
even=[] #create empty list to store even values
odd=[] #create empty list to store odd values
for num in numbers:
    if num%2==0: #check the element in the list is even or not
        even.append(num) #if the element is even then we store it in the even list using append() method
    else:
        odd.append(num) #if the element is odd then we store it in the odd list using append() method
print('Even numbers: ', even)
print('Odd numbers: ',odd)
print('First 3 numbers in the list: ',numbers[:3])
print('Last 3 numbers in the list: ',numbers[-3:])
backup=numbers.copy() # copy the numbers list 
#print(backup)
numbers.clear() #delete all the elements in the original list using clear() method
print(f'Original list: {numbers}')
print(f'backup list: {backup}')
