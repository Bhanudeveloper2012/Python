string_Name=input("Enter the string:")

ans=string_Name.split()
print(len(ans))
print(ans)

#Without using split function
string_Name1=input("Enter the string:")

ans=0
for i in string_Name1:
    if i == " ":
        ans=ans+1
ans=ans+1
print(ans)
