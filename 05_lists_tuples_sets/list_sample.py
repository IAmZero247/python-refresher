from collections.abc import Iterable

#emptylist

empty_list = []
my_list1 = [1, "zero", 2.5 , True , 'sam']
my_list2 = ['p','y','t','h','o','n']

# to get the methods of list
print(dir(list))

my_list1[0] = 10
print(my_list1)

#append extend insert remove/del pop

my_list1.append('append1')
my_list1.extend('extend')



print("Try to flat below list : ->")
sample = [5,1,9,["Saif",'2',"Ram"],5,5,5,[20,30,40], "Aniket"]


flat_list = []
for sub in sample:
    if (isinstance(sub, Iterable) and type(sub) != str):
    # iterable
      for item in sub:
        flat_list.append(item)
    else:
        flat_list.append(sub)
print(flat_list)

sample2 = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
flat_list = [item for sublist in sample2 for item in sublist]
print(flat_list)

# i = 0
# while i < len(a):
#     if a == [i]:
#         a.remove()
#         i = i - 1
#     i = i + 1
# print(a)

# list(filter( lambda i : i !=5, a))
# print(a)

print("Try to reverse below list : ->")
a = [5,1,9,["Saif", 2, "Ram"],5,5,5, "Aniket"]

import math
b = math.floor(len(a)/2)
for i in range(b):
    temp = a[i]
    a[i] = a[-(i+1)]
    a[-(i+1)] = temp
print(a)