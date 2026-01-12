#convert list to tuple
a=[0,1,2]
t=tuple(a)
print(t)

#convert tuple to list
a=(0,1,2)
t=list(a)
print(t)

#built in functions for delete
#remove item from list
a=[10,20,30,40,50]
a.remove(30)
print(a)

#remove item from list using pop 
a=[10,20,30,40,50]
a.pop(3)
print(a)

#using clear()
a=[10,20,30,40,50]
a.clear()
print(a)


#using del()
a=[10,20,30,40,50]
del(a)
