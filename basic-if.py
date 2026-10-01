x=41
if x==42:
    print("X Does in face equal 42!")


# if/else statements

x=41
if x==41:
    print("X Does in fact equal 41!")
else:
    print("X Does Not equal 41!")

#if/elif

name="John"
if name=="Bob":
    print("Hi there Bob!")
elif name=="John":
    print("What up John!")
else:
    print("I don't know who you are!")

#Multiple Conditionals

name="John"
if name== "John" or name=="Bob":
    print("Hi there John or Bob!")
    
#And or
name=input("Enter Your Name: ")
if name=="John" or name=="Bob":
    print(f"Hi there {name}!")
else:
    print("Hi there Stranger!")
