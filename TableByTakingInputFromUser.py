#By using while loop
constant_Number=int(input("Enter the table number your want to print:"))

count=1
while(count<=10):
    result=constant_Number*count
    print(f"{constant_Number}*{count}={result}")
    count+=1

#By using for loop
constant_Number=int(input("Enter the table number your want to print:"))

for middle_number in range(1,11):
    print(constant_Number,"*",middle_number,"=",constant_Number*middle_number)
