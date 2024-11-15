Palindrome_Number=int(input("Enter the number:"))#456
res=Palindrome_Number#456
rev=0#0

while(res>0):#456#45#4
    r=res%10#6#5#4
    rev=rev*10+r#6#65#654
    res=res//10#45#4#0
print("Reverse of given number is:",rev)

if(rev==res):
    print(rev,"is Palindrome")
else:
    print(rev, "is not Palindrome")

