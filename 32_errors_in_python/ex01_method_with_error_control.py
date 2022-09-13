def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor


#print(divide(10/0))


grades = []  # Imagine we have no grades yet
# average = divide(sum(grades) / len(grades))  # Error!

try:
    this_variable_is_visible_accross_try_and_catch_block_unlike_java=20;
    average = divide(sum(grades), len(grades))
    print(average)
except ZeroDivisionError as e:
    print(e)
    print(this_variable_is_visible_accross_try_and_catch_block_unlike_java)
    # Much friendlier error message because now we're dealing with it
    # In a "students and grades" context, not purely in a mathematical context
    # I.e. it doesn't make sense to put "There are no grades yet in your list"
    # inside the `divide` function, because you could be dividing something
    # that isn't grades, in another program.
    print("There are no grades yet in your list.")




grades = [90, 100, 85]

try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError:
    print("There are no grades yet in your list.")
else:
    print(f"The average was {average}")



