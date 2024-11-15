from random import randint

def random():
    while True:
        n=str(randint(100,999))
        if not (n[0]==n[1] or n[1]==n[2] or n[0]==n[2]):
            return n

Name=input("Wellcome to Cows and Bulls game\nEnter your name:")
print("hi",Name,"lets start the game")
chances=8
cows=0
bulls=0

num=str(random())
while chances>0:
  print("You have",chances,"chances left")
  num1=input("Enter the gusse number:")

  if num1==num:
     print("Great you gussed the correct number")
     break
  else:
        for i in range (0,3):
            if num1[i]==num[i]:
               bulls+=1
            elif num1[i] in num:
               cows+=1
  print("Good keep going,the number of bulls are",bulls,"and cows are",cows)
  bulls=0
  cows=0
  chances-=1
print("The correct answer is:",num)