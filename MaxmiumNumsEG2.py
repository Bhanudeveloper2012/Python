list=[22,4,65,73,45]
Max=list[0]
for i in list:
    if i>Max:
        Max=i
print("The maximum number in given list is",Max)
   
print(min(list))
print(max(list))

Min=list[0]
for i in list:
    if i<Min:
        Min=i
print("The minmum number in the given list is",Min)
