list_Name=[1,2.56,"Villain",True]

#Orderd
print(list_Name)

#Indexed
print(list_Name[0])
print(list_Name[-1])

#Mutable
list_Name[1]=0.67
print(list_Name)

#Allow duplicates
list_Name[0]="Villain"
print(list_Name)

#By using insert function
list_Name.insert(4,"End")
print(list_Name)

list_Name.insert(4,18)
print(list_Name)

#Second Lists
list_name1=[1,5.09,"King","CEO",False]

list_name1.append("last")
print(list_name1)

#By using slicings
print(list_name1[1:3])
print(list_name1[:2])
print(list_name1[2:])

# list_Name.extend(list_name1)
# print(list_Name)

for i in list_name1:
    print(i,end=" ")
