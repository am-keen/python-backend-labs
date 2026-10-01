#Choose You Own Adventure
#String Manipulation

name=input("Enter Your Name: ")
print(f"Hi there {name.lower()}")


name=input("Enter Your Name: ")
name=name.lower()
print(name)

#len() function

name=input("Enter your name: ")
print(f"The name {name} has {len(name)} characters.")

#Choose your own adventure

from os import system
system("clear")
print("Welcome To Choose Your Own Adventure!")
print("The goal is to find the Python Princess...")
name=input("Enter Your Name: ")
name=name.lower()
system("clear")
print("You're standing in front of two doors...")
print("Do you want the door on the left or right?")
question=input().lower()
if question=="left":
    system("clear")
    print("You fell into a pit and died. GAME OVER")
elif question=="right":
    system("clear")
    print(f"Congratulations {name.capitalize()} you found")
    print("the Python Princess!  YOU WIN!")
else:
    system("clear")
    print("Sorry, I don't recongize your response GAME OVER")
