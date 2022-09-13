#all special methods in python
#https://docs.python.org/3/reference/datamodel.html#special-method-names


'''
NOTE 1) self.email = first + '.' + last + '@email.com'

Problem with above is if we update first or last name, email wont auto correct
SO replace with property




'''
class Employee():

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        #self.email = first + '.' + last + '@email.com'
        self.salary = salary

    @property
    def email(self):
        '''
        NOTE 1) self.email = first + '.' + last + '@email.com'

               Problem with above is if we update first or last name, email wont auto correct
               So replace with property
               :return:
        '''
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.salary)

    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)

    def __add__(self, other):
        return self.salary + other.salary

    def __len__(self):
        return len(self.fullname)

    @fullname.setter
    def fullname(self, name):
        first ,last = name.split
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None



emp_1 = Employee('alice', 'john', 50000)
emp_2 = Employee('jack', 'gates', 60000)


print('e1 email: ', emp_1.email)
print('e1 fullname', emp_1.fullname)
emp_1.first = 'alisha'
print('e1 email: ', emp_1.email)
print('e1 fullname', emp_1.fullname)
print(emp_1 + emp_2)
print(len(emp_1))
emp_1.fullname = 'albert john'
print('e1 email: ', emp_1.email)
print('e1 fullname', emp_1.fullname)
del emp_1.fullname
print('e1 email: ', emp_1.email)
print('e1 fullname', emp_1.fullname)
print(emp_1)