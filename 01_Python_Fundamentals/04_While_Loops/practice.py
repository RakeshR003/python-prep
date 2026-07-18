# ==========================================
# While Loop Practice
# ==========================================

# ------------------------------------------
# Program 1 - Print Numbers from 1 to 10
# ------------------------------------------

i = 1

while i <= 10:
    print(i)
    i += 1


# ------------------------------------------
# Program 2 - Print Even Numbers
# ------------------------------------------

i = 2

while i <= 10:
    print(i)
    i += 2


# ------------------------------------------
# Program 3 - Print Odd Numbers
# ------------------------------------------

i = 1

while i <= 10:
    print(i)
    i += 2


# ------------------------------------------
# Program 4 - Print Multiples of 3
# ------------------------------------------

i = 3

while i <= 30:
    print(i)
    i += 3


# ------------------------------------------
# Program 5 - Sum of Numbers from 1 to 10
# ------------------------------------------

i = 1
total = 0

while i <= 10:
    total += i
    i += 1

print("Sum =", total)


# ------------------------------------------
# Program 6 - Store Numbers in a List
# ------------------------------------------

i = 1
numbers = []

while i <= 5:
    numbers.append(i)
    i += 1

print(numbers)


# ------------------------------------------
# Program 7 - Store Even Numbers in a List
# ------------------------------------------

i = 2
even_numbers = []

while i <= 10:
    even_numbers.append(i)
    i += 2

print(even_numbers)


# ------------------------------------------
# Program 8 - Right Triangle Pattern
# ------------------------------------------

i = 1

while i <= 5:
    print("* " * i)
    i += 1