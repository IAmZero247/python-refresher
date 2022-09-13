
'''
Exception:

try:
   #<Code>
   #Running First
except:
   #<Code>
   If Execption Occurs in try block execute this code
except:
   #<Code>
   If Execption Occurs in try block execute this code
except:
   #<Code>
   If Execption Occurs in try block execute this code
else:
   #<Code>
   #Executes if try block succeeds
finally:
   <code>
   #No matter what happen this piece of code will execute
'''






# -- Built-in errors --

# TypeError: something was the wrong type
# ValueError: something had the wrong value
# RuntimeError: most other things

# Full list of built-in errors: https://docs.python.org/3/library/exceptions.html


# -- Doing something if no error is raised --



# -- Doing something no matter what --
# This is particularly useful when dealing with resources that you open and then must close
# The `finally` part always runs, so you could use it to close things down
# You can also use it to print something at the end of your try-block if you like.

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor

students = [
    {"name": "Bob", "grades": [75, 90]},
    {"name": "Rolf", "grades": []},
    {"name": "Jen", "grades": [100, 90]},
]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}.")
except ZeroDivisionError:
    print(f"ERROR: {name} has no grades!")
else:
    print("-- All student averages calculated --")
finally:
    print("-- End of student average calculation --")
