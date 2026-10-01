#1. Get the numerical score from the user.

score = int(input("Enter score: "))
#2. Check if the score qualifies for an A (90+)

if score >= 90:
    print("Grade: A")

#3. If not, check for a B (80+)
elif score >= 80:
    print("Grade: B")

#4. If not, check for a C (70+)
elif score >= 70:
    print("Grade: C")

#5. Otherwise, assign an F
else:
    print("Grade: F")
