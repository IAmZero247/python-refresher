#Note: The example given below assumes that age of
#       person is not going to get changed.


from dataclasses import dataclass, field


@dataclass
class Person:
    name: str
    city: str
    age: int
    is_senior: bool = field(init=False)

    def __post_init__(self):
        if self.age >= 60:
            self.is_senior = True
        else:
            self.is_senior = False


p = Person("Nikhil", "Delhi", 70)
print(p.is_senior)

