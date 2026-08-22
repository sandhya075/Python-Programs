
'''

matplotlib
----------
--> This is an python library used to create graphs and chats

plot
----
--> The function can create 
eg--
import matplotlib.pyplot as plt
marks=[45,89,90]
stu=['santhi','sony','sandhya']
plt.plot(stu,marks)
plt.show()

xlabel
------
--> used to represent the X-axis values

ylabel
------
--> used to represent the Y-axis values

title
-----
--> To define the title of the graph

eg--
import matplotlib.pyplot as plt
marks=[45,90,85,35,75]
stu=['sony','santhi','sandhya','ravi','madhu']
plt.plot(stu, marks, color='red')
plt.title('Students_Marks')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.show()

bar graph
---------
eg--
import matplotlib.pyplot as plt
sales=[890,150,800,1200]
cars=['BMW','Nano','Swipf','Tayoto']
plt.bar(cars, sales, color='blue')
plt.title('Car_sales')
plt.xlabel('Company names')
plt.ylabel('Number of sales')
plt.show()

Horizontal bar graph
--------------------
eg--
import matplotlib.pyplot as plt
sales=[890,150,800,1200]
cars=['BMW','Nano','Swipf','Tayoto']
plt.barh(cars, sales, color='violet')
plt.title('Car_sales')
plt.xlabel('Number of sales')
plt.ylabel('Company names')
plt.show()

pie chart
---------
import matplotlib.pyplot as plt
subjects=['Python','Java','C']
students=[45,25,36]
plt.pie(students,labels=subjects)
plt.title('Total Students')
plt.legend(subjects)
plt.show()


scatter plot
------------
import matplotlib.pyplot as plt
students=['santhi','sandhya','ravi','ram']
marks=[90,85,35,75]
plt.scatter(students,marks)
plt.title('Student-Marks')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.show()


Histograph
----------
import matplotlib.pyplot as plt
sales=[890,400,150,800,1200,850]
plt.hist(sales)
plt.title('Sales_Hist')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

Box plot
--------
import matplotlib.pyplot as plt
marks=[40,50,60,70,80,90]
plt.boxplot(marks)
plt.show()



import matplotlib.pyplot as plt
marks=[40,50,60,70,80,90]
plt.boxplot(marks)
plt.show()

import matplotlib.pyplot as plt
marks=[45,89,90]
stu=['santhi','sony','sandhya']
plt.plot(stu,marks)
plt.show()

import matplotlib.pyplot as plt
marks=[45,90,85,35,75]
stu=['sony','santhi','sandhya','ravi','madhu']
plt.plot(stu, marks, color='red')
plt.title('Students_Marks')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.show()

import matplotlib.pyplot as plt
sales=[890,150,800,1200]
cars=['BMW','Nano','Swipf','Tayoto']
plt.bar(cars, sales, color='blue')
plt.title('Car_sales')
plt.xlabel('Company names')
plt.ylabel('Number of sales')
plt.show()

import matplotlib.pyplot as plt
subjects=['Python','Java','C']
students=[45,25,36]
plt.pie(students,labels=subjects)
plt.title('Total Students')
plt.legend(subjects)
plt.show()





















