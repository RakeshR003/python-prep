# ==========================================
# For Loop Practice
# ==========================================

# ------------------------------------------
# Program 1 - Print Numbers from 1 to 10
# ------------------------------------------

for i in range(1, 11):
    print(i)


# ------------------------------------------
# Program 2 - Print Even Numbers
# ------------------------------------------

for i in range(2, 11, 2):
    print(i)


# ------------------------------------------
# Program 3 - Print Odd Numbers
# ------------------------------------------

for i in range(1, 11, 2):
    print(i)


# ------------------------------------------
# Program 4 - Sum of Numbers from 1 to 10
# ------------------------------------------

total = 0

for i in range(1, 11):
    total += i

print("Sum =", total)


# ------------------------------------------
# Program 5 - Multiplication Table
# ------------------------------------------

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# ------------------------------------------
# Program 6 - FizzBuzz (1 to 20)
# ------------------------------------------

for i in range(1, 21):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# ------------------------------------------
# Program 7 - Square Pattern
# ------------------------------------------

for i in range(5):
    print("* " * 5)


# ------------------------------------------
# Program 8 - Right Triangle Pattern
# ------------------------------------------

for i in range(1, 6):
    print("* " * i)