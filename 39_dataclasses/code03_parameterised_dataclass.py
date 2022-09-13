#dataclass(_cls=None, *, init=True, repr=True, eq=True,
#          order=False, unsafe_hash=False, frozen=False)
#
# init -> __init__
# repr -> __repr__
# eq   -> __eq__
# order -> 1. > __gt__
#          2. >= __ge__
#          3. < __lt__
#          4. <= __le__
#
# unsafe_hash -> if true any way it will generate hash
# frozen  -> imutable class (True)
#         Here if we do below code
#         p1.name = "NIKHIL"
#---------------------------------------------------------------------------
#FrozenInstanceError                       Traceback (most recent call last)
#<ipython-input-5-dc5810b32590> in <module>
#----> 1 p1.name = "NIKHIL"
#
#<string> in __setattr__(self, name, value)
#
#FrozenInstanceError: cannot assign to field 'name'
#


from dataclasses import dataclass

@dataclass(order=True, frozen=True)
class Person:
    name: str
    age: str
    city: str

p1 = Person("Nikhil", 20, "Delhi")
p2 = Person("Nikhil", 21, "Delhi")

print("p1<p2 ->" , p1>p2)

print('hash of p1', hash(p1))
print('hash of p2', hash(p2))