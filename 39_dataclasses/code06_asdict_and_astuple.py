import json
from dataclasses import dataclass, asdict, astuple


@dataclass
class Address:
    lat: float
    lng: float
    city: str
    country: str


@dataclass
class Person:
    name: str
    addr: Address
    age: int

a = Address(28.75, 77.21, 'Delhi', 'India')

p = Person("Nikhil", a, 99)

print("p ->", p)

d = asdict(p)
print("as dictionary ->" , d)
print("type(d) ->" , type(d))

j = json.dumps(asdict(p))
print("as json st ->" ,j)
print("type(j) ->" , type(j))

t = astuple(p)
print("as tuple ->" , t)
print("type(t) ->" , type(t))
