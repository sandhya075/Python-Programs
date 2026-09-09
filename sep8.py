

'''
students marks manager

#make sure to create marks list
marks = []
for mark in range(3):
    mark = int(input("Enter the marks: "))
    #print(mark)
    marks.append(mark)
#print(marks)
#insert 90 marks into the list
marks.insert(0,90)
#print(marks)
marks.extend([75,85])
#check for 75 marks in given maarks list
if 75 in marks:
    marks.remove(75)
#to remove the final mark using pop
removed_mark = marks.pop()
print(f'Removed Mark is {removed_mark}')
#final list of marks
print(f'Final student Marks List in {marks}')
print(f'count of student marks list is {len(marks)}')

#control block (if,elif,else,for,while,break,continue)
#BMI usecase--> BMI (Body Mass Index)
#weight--> kgs
#height--> metres
#feet -->12 inches--> inch--> 2.54cm
#bmi = (Weight) / ((height)**2)
'''
weight = float(input("Enter the weight in kgs: "))
height = float(input("Enter the height in meters: "))
name = input("Enter the user name: ")
bmi = (weight) / ((height)**2)
print(bmi)
'''
<18.5 --> underweight
18.5 --> 24.9--> normal weight
25 - 29.9 --> overweight
>=30 --> obesity


if bmi<18.5:
    print('underweight')
elif bmi>=18.5 and bmi <=24.9:
    print('normal weight')
elif 25.0<=bmi<=29.9:
    print('over weight')
elif bmi>=30:
    print('obesity')

#BMI = (weight) / ((height)**2)
n_of_t_user_input = int(input("Enter the value:"))
for i in range(n_of_t_user_input):
    #weight = 75
    weight = float(input("Enter the weight in kgs:")
    #height = 1.45
    height = float(input("Enter the height in meters:"))
    name = input("Enter the user name:")
    if weight > 0 and height > 0:
        bmi = (weight
#Task --> store the results of name,weight,heigth -->BMI into a collection
'''
#repetition-->while
#same above task we need to handle the errors(exception handling) and also
#make user strictly to enter only numeric values
while True:
    try:
        weight = int(input('enter the weight in kgs:'))
        height = float(input('enter the height in metres:'))
        name = input("Enter the name")
        if weight > 0 and height > 0:
        
    # in this case we prefer exception handling
    try:
        if weight>0 and height>0:
            bmi = (Weight) / ((height)**2)
            break
    except Exception as e:
            print(f'the error is{e}')
            break


    

    
                         
