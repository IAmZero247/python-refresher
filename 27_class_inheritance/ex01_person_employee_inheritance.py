

class Person(object):

    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    # To get name
    def getName(self):
        return self.name

    # To check if this person is an employee
    def isEmployee(self):
        return False


class Employee(Person):

    def __init__(self, name, idnumber, job, salary):
        self.salary = salary
        self.job = job
        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

    def isEmployee(self):
        return True


per = Person("Sam" ,"idx1")  # An Object of Person
print(per.getName(), per.isEmployee())
per.display()

emp = Employee("Alice" , 886012,  "Intern", 200000) # An Object of Employee
print(emp.getName(), emp.isEmployee())
emp.display()