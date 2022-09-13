#field(*, default=MISSING, default_factory=MISSING,
#       init=True, repr=True, hash=None, compare=True, metadata=None)¶
#
#default eg ->  city field
#default_factory -> age field
#init    -> part of init , eg -> salary field
#repr    -> part of repr
#hash    -> part of hash
#compare -> part of order
#metadata -> meta info
#Note:
#
#      1. default parameter's object is shared by all the objects of a class
#      whereas default_factory parameter's object is unique for each object.
#
#      2. Method defined for default_factory paramter cannot take any arguments.

from dataclasses import dataclass, field


def get_default_age():
    ages = [12,34,56,34,32]
    return sum(ages) // len(ages)

@dataclass(unsafe_hash=True)
class Person:
    name: str = field(compare=False)
    city: str = field(default="Delhi", hash=False)
    age: int = field(default_factory=get_default_age, metadata={'format': 'year'})
    salary: int = field(init=False, repr=False, default=0)

#Person(name='Nikhil', city='Delhi', age=33) #error


p = Person("alice")
print("p ->" , p)

print('hash(p) ->', hash(p))
p1 = Person("Nikhil")
p2 = Person("Vivek")
print('p1==p2 ->',  p1==p2)
print('############################################################')
print(p.__dataclass_fields__)
print('############################################################')
print(p.__dataclass_fields__['age'].metadata['format'])