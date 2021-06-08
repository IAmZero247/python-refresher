numbers = [1, 3, 5]
squares = [x * 2 for x in numbers]

# -- Dealing with strings --

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = []

for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)

print(starts_s)


# -- Can make a new list of friends whose name starts with S --

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]

print(starts_s)

# -- List comprehension creates a _new_ list --

friends = ["Sam", "Samantha", "Saurabh"]
starts_s = [friend for friend in friends if friend.startswith("S")]  # same as above

print(friends)
print(starts_s)
print(friends is starts_s)
print("friends: ", id(friends[0]), " starts_s: ", id(starts_s[0]))
print("friends: ", id(friends), " starts_s: ", id(starts_s))


even = [n for n in range(100) if n % 2 ==0]
odd =[n for n in range(100) if n % 2 ==1]
print(even)
print(odd)
