l1=[33,54,2,34,55]
i=int(input("Enter the index number:"))
a=9
b=0
try:
    print(l1[i])
except Exception as e:
    print(e)
try:
    c=a/b
    print(c)
except Exception as e:
    print(e)

finally:
    print("This was printing from the finally block")
print("This was last line in code")