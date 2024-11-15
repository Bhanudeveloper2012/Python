Dicitionaries_Name={
    "Name":"Villain",
    "Age":18,
    "Goal":"CEO",
    "Religion":"Hindusim"
}

#Order of dictionarie
print(Dicitionaries_Name)

#Index of dictionarie
print(Dicitionaries_Name["Religion"])

#By using get
print(Dicitionaries_Name.get("Name"))

#By getting the keys
k=Dicitionaries_Name.keys()
print(k)
for i in k:
    print(Dicitionaries_Name.get(i))

#By getting the values
print(Dicitionaries_Name.values())

#By using items
print(Dicitionaries_Name.items())

#By using update
Dicitionaries_Name.update({"Age":20,"Height":6})
print(Dicitionaries_Name)

Dicitionaries_Name["Weight"]=60
print(Dicitionaries_Name)

#Adding a list
Dicitionaries_Name["Hobbies"]=["Playing/Watching Cricket,Reading Books"]
print(Dicitionaries_Name)

Dicitionaries_Name.pop("Hobbies")
print(Dicitionaries_Name)

