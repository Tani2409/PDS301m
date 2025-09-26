#Logical Operators & Boolean Variables

x = 5
y = 2
print(x > y)
print(not (x > y))
print(x == y)

print(2*(x>y))
j = (x>y)+(x==y)+(y>x)
print(j)

print((x>y)|(y>x))
print((x>y)&(y>x))
print((x>y)|(x==y))
print(not (x==y))
print((x>y)|(-1*(x==y))==True)