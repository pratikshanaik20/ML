# adding and removing element from set
s={'g','e','k','s','m'}
s.add('f')
print("set after updating:",s)

s.discard('g')
print("\nset after updating:",s)

s.remove('e')
print("\nset after updating:",s)

print("\npopped element",s.pop())
print("set after updating:",s)

s.clear()
print("\nset after updating:",s)


#without frozenset
mylist=['college','university','country']
x=(mylist)
x[0]="college_1"
print(mylist)