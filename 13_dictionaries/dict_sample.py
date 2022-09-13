empty_dict ={}
d1 = {'a':1 , 'a':2 , 'a':3 , 'b':4}
print(d1)
print(type(d1))
print(d1['a'])
print(d1.get('a'))
d1['a'] = 100
print(d1)


#keys() values() items() clear() copy()
#1 copy() - deep and shallow copy

a = [1, 2, 3, 4 ,5]
b_shallow = a.copy() #shallow copy
b_deep = a #deep copy
a[2] = 300
b_shallow[2] = 3000
print(a)
print(b_shallow)
print(b_deep)

#values

a1 = { 'a11' :5 , 'a12' : 10}
b1 = { 'b11' :50 , 'b12' : 100}
c = a1.values() # return dictvalue object
d=  b1.values()
print(sum(c) + sum(d))

#List Comprehension

#expression for loop

populations = {'c1':100,'c2':200,'c3':300}
total_pop1 = sum([ i for i in populations.values()])
print('total_pop1:' +  str(total_pop1) )

pop_complex_dic = {'c1,c2,c3':[100,200,300], 'c4,c5':[400, 500],'c6':600}
print(pop_complex_dic)


