l1=[1,'Ceo',78.09,'c']
l2=[l1,2,'Manager',98.12]

print(l1.index('Ceo'))
for i in l1:
    print(i)

for j in l2:
    print(j)

l2.append("List")
print(l2)

print(l1.pop(1))
print(l1)