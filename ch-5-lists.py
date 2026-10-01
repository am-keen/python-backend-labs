#Lists
names=["John", "Tim", "Mary", "Beatrice", "Bluto"]
print(names[2])
print(names)

#Putting different things into lists
variable1="Tim"
names=["John",variable1,"Mary",41,"Bluto"]
print(names[1])

#Another way to create a list
names=[]
names=["John","April"]
print(len(names))

#Adding a Name to the list
names=["John","April"]
names.append("Bob")
print(names)

#Adding Things to a List Later on
names=["John","April"]
names.insert(0,"Bob")
print(names[0])
print(names)

#Adding Multiple Names to a List
names=["John","April"]
names.extend(["Tim","Bob"])
print(names)

#Removing Items from a list
names=["John","Tim", "Mary","Bluto"]
names.remove("Bluto")
print(names)

#Remove a Specific Index Number

names=["John","Tim","Mary","Bluto"]
names.pop(0)
print(names)

names=["John","Tim","Mary","Beatrice","Bluto"]
names.remove("Mary")
print(names)

# Multi-Dimensional Lists
names = ["John", "Mary", "Beatrice", "Bluto", [1,2,3,4]]
print(names)
print(names [4] [2])

numbers = [1,2,3,4]
names = ["John","Mary","Beatrice","Bluto", numbers]
print(names [4] [2])