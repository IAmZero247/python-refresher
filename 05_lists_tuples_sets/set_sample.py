#set cant hv mutable elements
empty_set = set()
wrong_empty_set = {} #dictionary
s1 = {1 ,2 ,3 ,"ABC" , True}
print(s1)


'''
s2 = [1 ,[2 ,3] ,"ABC" , True] # error->cz of list
print(s2)
'''

#slicing operator
#print(s1[2:4]) --------------> will work only with list/tuple

a= {1,2,3,4,5}
b= {4,5,6,7,8}
#union |
print(a|b)
# intersection &
print(a&b)
#difference
print(a-b)
#symmetric difference = a|b - a&b
print(a^b)
print((a|b) - (a&b))
#enumerate - add counter to iterable and return enuerate object
a = ['alice' , 'john', 'rose']
enum_a = enumerate(a,1)
print(list(enum_a))

