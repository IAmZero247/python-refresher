#tuple - immutable
#write protect - faster then list

a = [1,2]

#swapping
a[0] ,a[1] = a[1],a[0]
print(a)


empty_tuple = ()
t1 =(1, 2 ,3,'abc', ['xyz' , 3])
print("t1 ->" ,type(t1))
t1[4][0] = 'uvw' #changing item in list
print("t1 ->" ,t1)

t2_str = ('abc')
print("t2 ->" ,type(t2_str))
t2_tup = ('abc',)
print("t2 ->" ,type(t2_tup))
t3_int = 10
print("t3 ->" ,type(t3_int))
t3_tup = 10,
print("t3 ->" ,type(t3_tup))
