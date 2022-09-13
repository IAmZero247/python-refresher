# -- Comparisons --

print(5 == 5)  # True
print(5 > 5)  # False
print(10 != 10)  # False

# Comparisons: ==, !=, >, <, >=, <=

# -- is --
# Python also has the `is` keyword. It's a confusing keyword for now, so I don't recommend using it.

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]
friendsShallowCopy = friends

print(friends == abroad)  # True
print(friends is abroad)  # False
print(friendsShallowCopy is friends) #True

friends[1] = "Tara"
friendsShallowCopy[0] ="Albert"
print(friends)
print(friendsShallowCopy)
