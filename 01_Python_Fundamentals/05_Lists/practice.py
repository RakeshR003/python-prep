"""
==========================================================
Python Lists - Practice
Author : Raghavendra Rakesh
Topic  : Lists
Status : Completed
==========================================================

Programs Covered
1. append()
2. insert()
3. remove()
4. pop()
5. len()
6. count()
7. index()
8. sort()
9. reverse()
10. Combined Interview Practice
"""

# ==========================================================
# 1. append() - Add Numbers
# ==========================================================

numbers = []
numbers.append(10)
numbers.append(20)
numbers.append(30)

print(numbers)


# ==========================================================
# 2. append() - Add Student Names
# ==========================================================

students = []

for i in range(5):
    name = input("Enter student name: ")
    students.append(name)

print(students)


# ==========================================================
# 3. insert() - Add CR at First Position
# ==========================================================

students = []

count = int(input("How many students: "))

for i in range(count):
    students.append(input("Name: "))

cr = input("CR Name: ")

students.insert(0, cr)

print(students)


# ==========================================================
# 4. remove() - Remove Student
# ==========================================================

students = []

count = int(input("How many students: "))

for i in range(count):
    students.append(input("Name: "))

remove_name = input("Student to remove: ")

if remove_name in students:
    students.remove(remove_name)
else:
    print("Student not found")

print(students)


# ==========================================================
# 5. pop() - Remove Using Position
# ==========================================================

students = []

for i in range(5):
    students.append(input("Name: "))

position = int(input("Position to remove: "))

students.pop(position)

print(students)


# ==========================================================
# 6. len() - Print Names Longer Than 5 Letters
# ==========================================================

students = []

for i in range(5):
    students.append(input("Name: "))

for name in students:
    if len(name) > 5:
        print(name)


# ==========================================================
# 7. count() - Count Occurrences
# ==========================================================

students = []

for i in range(8):
    students.append(input("Name: "))

search = input("Search Name: ")

print("Count:", students.count(search))


# ==========================================================
# 8. index() - Find Position
# ==========================================================

students = []

for i in range(6):
    students.append(input("Name: "))

find = input("Find Student: ")

if find in students:
    print("Position:", students.index(find))
else:
    print("Student not found")


# ==========================================================
# 9. sort() - Alphabetical Order
# ==========================================================

students = []

for i in range(7):
    students.append(input("Name: "))

students.sort()

print(students)


# ==========================================================
# 10. reverse() - Reverse List
# ==========================================================

students = []

for i in range(6):
    students.append(input("Name: "))

students.reverse()

print(students)


# ==========================================================
# 11. Interview Practice - Student Management System
# ==========================================================

students = []

count = int(input("How many students: "))

for i in range(count):
    students.append(input("Name: "))

cr_position = int(input("CR Position: "))

cr = students.pop(cr_position)

students.insert(0, cr)

leave = input("Student Leaving: ")

if leave in students:
    students.remove(leave)
else:
    print("Student not found")

print("\nFinal Student List")

for student in students:
    print(student)

long_names = 0

for student in students:
    if len(student) > 5:
        long_names += 1

print("\nStudents with names longer than 5 letters:", long_names)

if long_names > 2:
    print("Large Class")
else:
    print("Small Class")