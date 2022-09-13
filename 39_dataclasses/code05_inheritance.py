from dataclasses import dataclass, field

print('#################### Ex 1 ####################')
@dataclass
class Person:
    name: str
    city: str
    age: int


@dataclass
class Student(Person):
    grade: int
    subjects: list

s = Student("Nikhil", "Delhi", 20, 9.8, ['A', 'B', 'C'])

print("student " ,s)

print('#################### Ex 2 ####################')


@dataclass
class A:
    x: int = 10
    y: int = 20


@dataclass
class B(A):
    z: int = 30
    x: int = 40


print(help(B))


print('##############################################')

b = B()
a = A()
print ('b ->' , b)
print ('a ->' , a)