def add(x, y):
    return x + y


print(add(5, 7))

# -- Written as a lambda --

add = lambda x, y: x + y
print(add(5, 7))

# Four parts
# lambda
# parameters
# :
# return value


print((lambda x,y,z : x*y*z)(10,11,12))

# Lambdas are meant to be short functions, often used without giving them a name.
# For example, in conjunction with built-in function map
# map applies the function to all values in the sequence , returns map object.


def double(x):
    return x * 2


sequence = [1, 3, 5, 9]

doubled_list_comprehension = [
    double(x) for x in sequence
]  # Put the result of double(x) in a new list, for each of the values in `sequence`
doubled_with_map = map(double, sequence)
print(doubled_list_comprehension)
print(list(doubled_with_map))

# -- Written as a lambda --

sequence = [1, 3, 5, 9]
doubled_list_comprehension_with_lambda = [
    (lambda x: x *2)(x) for x in sequence
]
doubled_with_map_and_lambda = map(lambda x: x * 2, sequence)
print(doubled_list_comprehension_with_lambda)
print(list(doubled_with_map_and_lambda))

# -- Important to remember --
# Lambdas are just functions without a name.
# They are used to return a value calculated from its parameters.
# Almost always single-line, so don't do anything complicated in them.
# Very often better to just define a function and give it a proper name.
