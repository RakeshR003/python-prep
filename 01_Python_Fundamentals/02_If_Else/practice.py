# ==========================================
# If-Else Practice
# ==========================================

# ------------------------------------------
# Program 1 - Even or Odd
# ------------------------------------------

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# ------------------------------------------
# Program 2 - Positive or Negative
# ------------------------------------------

number = int(input("Enter a number: "))

if number >= 0:
    print("Positive")
else:
    print("Negative")


# ------------------------------------------
# Program 3 - Largest of Two Numbers
# ------------------------------------------

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is larger")
else:
    print(b, "is larger")


# ------------------------------------------
# Program 4 - Voting Eligibility
# ------------------------------------------

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")


# ------------------------------------------
# Program 5 - Grade Calculator
# ------------------------------------------

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# ------------------------------------------
# Program 6 - Fizz
# ------------------------------------------

number = int(input("Enter a number: "))

if number % 3 == 0:
    print("Fizz")
else:
    print(number)


# ------------------------------------------
# Program 7 - FizzBuzz
# ------------------------------------------

number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)