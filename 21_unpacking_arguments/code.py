# -- Packing --
print("--line:02--")
def multiply(*args):
    print(args) #args from a tuple
    total = 1
    for arg in args:
        total = total * arg

    return total


print(multiply(3, 5))
print(multiply(-1))
print("--line:14--")
# The asterisk takes all the arguments and packs them into a tuple.

# -- Unpacking list to argument --
# The asterisk can be used to unpack sequences into arguments too!
print("--line:19--")

def add(x, y):
    return x + y


nums = [3, 5]
print(add(*nums))  # instead of add(nums[0], nums[1])
print("--line:27--")
# -- Uses with keyword arguments --
# Double asterisk packs or unpacks keyword arguments
print("--line:30--")

def add(x, y):
    return x + y

nums = {"x": 15, "y": 25}

print(add(**nums))
print("--line:38--")
# -- Forced named parameter --
print("--line:40--")

def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg

    return total


def apply(*args, operator):
    print(args) # tuple -> (1,3,6,7)
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."


print(apply(1, 3, 6, 7, operator="+"))
print(apply(1, 3, 6, 7, operator="*"))
print(apply(1, 3, 5, "+"))  # Error
print("--line:63--")