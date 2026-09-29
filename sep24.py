
class Employee:
    count = 0
    def __init__(self, name, emp_id, salary):
        self.__name = name
        self.emp_id = emp_id
        self.salary = salary

        Employee.count += 1
    def display(self):
        print("Employee ID :", self.emp_id)
        print("Name        :", self.__name)
        print("Salary      :", self.salary)
    def details(self):
        return "This is an Employee"
    @staticmethod
    def get_employee_count():
        return Employee.count
    @classmethod
    def get_count(cls):
        return cls.count
    def __str__(self):
        return self.__name + " - " + str(self.salary)
    def __eq__(self, other):
        return self.salary == other.salary
    def __lt__(self, other):
        return self.salary < other.salary
    def __gt__(self, other):
        return self.salary > other.salary
# Inheritance
class Manager(Employee):
    def details(self):
        return "Manager manages the team"
class Developer(Employee):
    def details(self):
        return "Developer develops applications"
# Objects
manager = Manager("Ravi", "M101", 50000)
developer = Developer("Sandhya", "D101", 40000)


print("----------------------------------------")
print("       EMPLOYEE MANAGEMENT SYSTEM")
print("----------------------------------------")

print("\nEmployee 1 Details")
manager.display()

print("\nEmployee 2 Details")
developer.display()


print("\nPolymorphism")
print(manager.details())
print(developer.details())


print("\nEmployee Information")
print(manager)
print(developer)


print("\nEmployee Count")
print("Using Static Method :", Employee.get_employee_count())
print("Using Class Method  :", Employee.get_count())


print("\nSalary Comparison")
print("Manager == Developer :", manager == developer)
print("Manager < Developer  :", manager < developer)
print("Manager > Developer  :", manager > developer)


print("\nProgram Completed Successfully!")
