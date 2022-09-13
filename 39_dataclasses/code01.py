class Person:

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __repr__(self):
        return "Person(name={}, age={}, city={})".format(self.name, self.age, self.city)

    def __eq__(self, other):
        return (self.name, self.age, self.city) == (other.name, other.age, other.city)

p1 = Person("Nikhil", 21, "Delhi")
p2 = Person("Nikhil", 21, "Delhi")
print("p1 -> ", p1)
print("p1==p2 ->" , p1==p2)


#Class impelementation using dataclasses

from dataclasses import dataclass

@dataclass
class NewPerson:
    name: str
    age: int
    city: str

p1 = NewPerson("Nikhil", 21, "Delhi")
p2 = NewPerson("Nikhil", 21, "Delhi")
print("p1 -> ", p1)
print("p1==p2 ->" , p1==p2)

