'''
Chapter 4 Exercises.
1.Create a simple math flashcard game that asks a user what two numbers added together equals and tell them whether or not they got the answer correct.
2.Write some code that asks for a person's full name (first and last name) and then output their name with both first and last name capitalized (my hint: title()).
3. Write some code that asks for a person's name and then tell them how many characters they name adds up to. make sure adds up correctly.
'''

#2. exercise 2
name=input("What is your first and last name? ")
print(name.title()) 


# exercise 1

answer=int(input("What is 5+7? "))

if answer==12:
    print("Correct! You got it right!")
else:
    print("Sorry, that is incorrect. The answer is 12.")

#exercise 3

name=input("What is your name?: ")
print(f"The name {name} has {len(name)} characters.")
