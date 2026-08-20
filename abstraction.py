
'''
Abstraction
-----------
--> Abstraction means hiding the implemented data and showing anly need data to the user
--> ABC--> Abstract base class
--> abstract is used to hide that parcticular information of a base class
eg
--
from abc import ABC,abstractmethod
class gov_bank(ABC):
    @abstractmethod
    def interest(self):
        print('Government interest is 3.5')
        
class SBI_bank(gov_bank):
    def interest(self):
        print('SBI bank interest is 7.8')
        
class ICIC_bank(gov_bank):
    def interest(self):
        print('ICIC bank interest is 8.9')
        
obj = SBI_bank()
obj.interest()

obje = ICIC_bank()
obje.interest()

1. write a code on calculator to add given numbers 2 or 3 or 4 inputs
2.create the class with name vehicals child class and hirachiracal class

       

class Person:
    university_name = "Codegnan University"   # Class Attribute

    def __init__(self, name, age, Edu_BG, Gender, Department):
        self.name = name
        self.age = age
        self.Edu_BG = Edu_BG
        self.Gender = Gender
        self.Department = Department

    def display_info(self):
        """Method to be overridden"""
        pass


# ---------------- Student ---------------- #

class Student(Person):
    student_count = 0

    def __init__(self, name, age, student_id, course, Year_, Edu_BG, Gender, Department):
        super().__init__(name, age, Edu_BG, Gender, Department)

        self.__student_id = student_id
        self.course = course
        self.Year_ = Year_

        Student.student_count += 1

    def display_info(self):
        print("\n------ Student Details ------")
        print("University :", Person.university_name)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Student ID :", self.__student_id)
        print("Course     :", self.course)
        print("Year       :", self.Year_)
        print("Education  :", self.Edu_BG)
        print("Gender     :", self.Gender)
        print("Department :", self.Department)

    def get_student_id(self):
        return self.__student_id

    @classmethod
    def total_students(cls):
        print("Total Students :", cls.student_count)


# ---------------- Faculty ---------------- #

class Faculty(Person):
    faculty_count = 0

    def __init__(self, name, age, faculty_id, Department, Edu_BG, Gender):
        super().__init__(name, age, Edu_BG, Gender, Department)
        self.__faculty_id = faculty_id

        Faculty.faculty_count += 1

    def display_info(self):
        print("\n------ Faculty Details ------")
        print("University :", Person.university_name)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Faculty ID :", self.__faculty_id)
        print("Education  :", self.Edu_BG)
        print("Gender     :", self.Gender)
        print("Department :", self.Department)

    @staticmethod
    def university_policy():
        print("\nUniversity Policy:")
        print("Codegnan University follows strict academic policies.")

    @classmethod
    def total_faculty(cls):
        print("Total Faculty Members :", cls.faculty_count)

class Driver(Person):
    driver_count = 0

    def __init__(self, name, age, Edu_BG, driver_id, Department, Gender, Bus_n, Bus_R):
        super().__init__(name, age, Edu_BG, Gender, Department)

        self.__driver_id = driver_id
        self.Bus_n = Bus_n
        self.Bus_R = Bus_R

        Driver.driver_count += 1

    def display_info(self):
        print("\n------ Faculty Details ------")
        print("University :", Person.university_name)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Driver ID :", self.__driver_id)
        print("Education  :", self.Edu_BG)
        print("Gender     :", self.Gender)
        print("Department :", self.Department)

    @staticmethod
    def university_policy():
        print("\nUniversity Policy:")
        print("Codegnan University follows strict academic policies.")

    @classmethod
    def total_drives(cls):
        print("Total Drivers Members :", cls.driver_count)

# ---------------- Objects ---------------- #

student1 = Student("Rahul Sharma",21,"CNU12345","Computer Science",2026,"Intermediate","Male","IT")

student2 = Student("Ananya Reddy",22,"CNU67890","Data Science",2026,"Intermediate","Female","IT")

faculty1 = Faculty("Dr. Ravi Kumar",45,"F001","AI & ML","PhD","Male")

faculty2 = Faculty("Dr. Meera Srinivas",50,"F002","Cybersecurity","PhD","Female")

driver1 = Driver("Mr.Teja",56,"SSC","DV001","Transport","Male","AP02-8978","Maduravada")
# ---------------- Output ---------------- #

student1.display_info()
student2.display_info()


print("\nStudent ID:", student1.get_student_id())

faculty1.display_info()
faculty2.display_info()

Faculty.university_policy()
driver1.display_info()


Student.total_students()
Faculty.total_faculty()
Driver.total_drives()

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("Sum=",a+b)
class vehicle:
    def bike(self):
        print('bike')
class vehicle:
    def scooty(grandfather):
        print('scooty')
class vehicle:
    def van(father):
        print('van')
class vehicle:
    def car(mother):
        print('car')
v1 = vehicle()
v1.vehicle()
'''




    


