


#Array Declaration

a0 = [[10,20,30],[11,21,22],[12, 22 , 32]]

print(a0)

a1 = []
for x in range(3):
    a1.append([int(i) for i in input('Input Please:').split()])

print(a1)

#Array Updation

a2 = [[10,20,30],[11,21,22],[12, 22 , 32]]

print(a2)

a2[1] = [100, 200, 300]
print(a2)


#Array Traversing

for i in a2:
    for j in i:
        print(j , end = " ")

    print()

#Array Deletion

del(a2[1][1])
del(a2[2])

print(a2[:])

#Array Slicing
a2 = [[10,20,30],[11,21,22],[12, 22 , 32]]

print(a2[1:4])
print(a2[1:2])
print(a2[:])

#Array Length
print(len(a2))