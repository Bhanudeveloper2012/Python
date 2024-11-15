#To print duplicate elements
Duplicate_list=[23,45,66,23,56,66]
Duplicate=[]
Orginal=[]

for i in Duplicate_list:
    if i not in Orginal:
        Orginal.append(i)
    else:
        Duplicate.append(i)
print("Actually listis:",Duplicate_list)
print("The duplicate numbers:",Duplicate)
print("The orginal numbers:",Orginal)
