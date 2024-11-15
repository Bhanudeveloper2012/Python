string_Name="Developer"
for i in string_Name:
    print(i,end=" ")
for i in string_Name:
    print("The string character is {}: index of it {}".format(i,string_Name.index(i)))
print(string_Name.index("e",4,8))
print("e" in string_Name)
print("k" in string_Name)
print("i" not in string_Name)

#\r is used for carriage return
print("Hello,welocme\r to my world")

#To print \n in output
print(r"\n")

length_Of_String="Sernior developer"
print(len(length_Of_String))
print(length_Of_String.find("developer"))

#Taking input from user
user_Name=input("Enter your name:")
print("Hi",user_Name,"How are you?")
print("Hi,How are you?",user_Name)
print("Hi {},How are you?".format(user_Name))