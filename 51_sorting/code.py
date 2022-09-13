li = [9,1,5,6,4,5,2,3]
s_li = sorted(li)
print("li ",li)
print("s_li ",s_li)
li.sort()
print("li ",li)
li = [-6,-5, -4, 6,4,5,2,3]
s_li =sorted(li ,key=abs)
#sorting basd on particular criteria , eg abs value
print("s_li " ,s_li)
tu = [9,1,5,6,4,5,2,3]
s_tu = sorted(tu)
print("s_tu ",s_tu)
s_tu_rev = sorted(tu, reverse=True)
print("s_tu_rev ",s_tu_rev)

#Employee object

class Employee():

    def __init__(self, name ,age, salary):
        self.name =name
        self.age =age
        self.salary = salary

    def __repr__(self):
        return '[ "{}" ,{} , {} ]'.format(self.name,self.age,self.salary)

e1 = Employee('wayne' ,26 , 25000)
e2 = Employee('sam' ,23 , 27000)
e3 = Employee('john' ,30 , 30000)
e4 = Employee('alice' ,22 , 21000)
e5 = Employee('dominik' ,27 , 28000)

eli = [e1,e2,e3,e4,e5]
print('eli -> ',eli)

def e_sort_name(emp):
    return emp.name

def e_sort_age(emp):
    return emp.age

s_emp_name =sorted(eli ,key=e_sort_name)
print('s_emp_name -> ', s_emp_name)
s_emp_age =sorted(eli ,key=e_sort_age, reverse =True)
print('s_emp_age -> ', s_emp_age  )
s_emp_lambda =sorted(eli ,key=lambda e : e.salary)
print('s_emp_lambda -> ', s_emp_lambda  )

from operator import attrgetter
s_emp_attrgetter =sorted(eli ,key=attrgetter('age'))
print('s_emp_attrgetter -> ', s_emp_attrgetter  )