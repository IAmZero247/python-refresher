from collections import namedtuple
#named tuple is like a light weight object

color_dict = {'red':55, 'green':155, 'blue':255}
Color = namedtuple('Color', ['red' ,'green' ,'blue'])
sampleColor= Color(55,155,255)

print(type(sampleColor))
white= Color(255,255,255)
print(sampleColor.red)
print(sampleColor.green)
print(sampleColor.blue)


# Student Tuple
# _make() :- This function is used to return a namedtuple() from the iterable passed as argument.
# _asdict() :- This function returns the OrderedDict() as constructed from the mapped values of namedtuple().
# using “**” (double star) operator :- This function is used to convert a dictionary into the namedtuple().

Student = namedtuple('Student', ['name', 'age', 'DOB'])
jacobNtp = Student('Jacob', '19', '2541997')

print("The Student age using index is : ", end="")
print(jacobNtp[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(jacobNtp.name)

# Access using getattr()
print("The Student DOB using getattr() is : ", end="")
print(getattr(jacobNtp, 'DOB'))

print("The namedtuple instance using iterable is  : ")
davidLi = ['David', '19', '411997']
print(Student._make(davidLi))

# using _asdict() to return an OrderedDict()
print("The OrderedDict instance using namedtuple is  : ")

print(jacobNtp._asdict())

# using ** operator to return namedtuple from dictionary
print("The namedtuple instance from dict is  : ")
aliceDt = {'name': "Alice", 'age': 19, 'DOB': '1391997'}
print(Student(**aliceDt))