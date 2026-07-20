# a = []
# a.append(10)
# a.append(20)
# a.append(30)
# print(a)

# names = []
# names.append("Rakesh")
# names.append("Rahul")
# names.append("Amit")
# print(names)

# i = 1
# numbers = []
# while i <= 5:
#     numbers.append(i)
#     i = i + 1
# print(numbers)

# i = 2
# even_numbers = []
# while i <= 10:
#     even_numbers.append(i)
#     i = i+2
# print(even_numbers)

# i = 3
# multiples_of_3 = []
# while i <= 30:
#     multiples_of_3.append(i)
#     i = i + 3
# print(multiples_of_3)

#colors.insert(1, "Yellow")

# numbers = [10, 20, 40, 50]
# numbers.insert(2, 30)
# print(numbers)

# students = ["Ravi", "John", "David"]
# students.insert(0 ,"Rahul")
# students.insert(3 ,"Arun")
# print(students)

# students=[]
# for i in range(0,5):
#     names = input("What is your name :")
#     students.append(names)
# students.insert(0,"Rahul")
# print("Final Student Lists :",students)

# contacts=[]
# n = int(input("How many contacts :"))
# for i in range (n):
#     a = input("names :")                  #basic  add input only i forgot and struggled i want to improve 
#     # a = ("names :")
#     contacts.append(a)
# emer=input("Do you want to add an Emergency Contact (Yes/No):")
# if emer == "Yes":
#     name = (input())
#     contacts.insert(0, name)
#     print(contacts)
# else:
#     print(contacts)

# fruits = ["Apple", "Banana", "Orange", "Mango"]
# fruits.remove("Orange")
# print(fruits)

# shopping = []
# a = int(input("How many iteams :"))
# for i in range(a):
#     name=input("iteams :")
#     shopping.append(name)
# r = input("remove iteam :")
# shopping.remove(r)
# print(shopping)


# students = []
# att_stud = int(input("How many students are present :"))
# for i in range (att_stud):
#     stud_name = input("Name :")
#     students.append(stud_name)
# abs_stud = input("Who is absent :")
# if abs_stud in students:
#     students.remove(abs_stud)
# else:
#     print("Student not Found")
# print(students)


# guest = []
# no_of_guest = int(input("How many guest :"))
# for i in range(no_of_guest):
#     names = input("Name :")
#     guest.append(names)
# vip_guest=input("VIP Guest name :")
# guest.insert(0, vip_guest)
# cancel = input("if any guest cancelled :(yes/no)?")
# if cancel == "yes":
#      a = (input("name :"))
#      if a in guest:   #This is called input validation  This will cause an error (ValueError). so
#         guest.remove(a) #so use in ,This will cause an error (ValueError).
#      else:
#          print("Guest not found")
# print(guest)

# a = 10
# numbers = (10,15,22,33,48,57,60)
# while a <= 60:
#     if a % 2 == 0:
#      print(numbers)
# a = a + 1



# a=0
# numbers = [5, 8, 11, 20, 13]
# while a < len(numbers):
#     print(numbers[a])
#     a = a + 1

# i = 10
 
# while i >= 1:
#     print(i)     #reverse number i keep forgetting basics its -1
#     i = i - 1   #like 10-1 9-1 8-1

# i = 20
# while i >= 10:
#     print(i)
#     i = i - 2

# i = 1
# while i <= 15:
#     print(i)
#     i = i + 2

# numbers = [5, 8, 11, 20, 13]

# i = 0

# while i < len(numbers):
#     print(numbers[i])
#     i = i + 1

# numbers = [5, 8, 11, 20, 13]
# i=0
# while i < 3:        #stuggle is real i overthinked and when they asked give first 3 i didnt write 3 but tried like len(numbers[3]) etc etc 
#     print(numbers[i])
#     i = i + 1


# numbers = [10, 7, 14, 9, 20, 5]
# i = 0
# while i < len(numbers):
#     if number[i] % 2 == 0:
#         print(numbers[i])
#     i = i + 1

# numbers = [12, 7, 18, 25, 30, 9]

# i = 0
# count = 0
# while i < len(numbers):
#     if numbers[i] > 15:
#         print(numbers[i])
#         count = count + 1   # count part i forgot again 
#     i = i + 1

# print("Total numbers printed:", count)

# numbers = [15, 28, 9, 42, 17, 6]
# i=0
# while i < len(numbers):
#     if numbers[i] % 2 == 0:
#         print(numbers[i])
#         break
#     i = i + 1

# numbers = [12, 25, 18, 41, 30, 9, 50]
# i = 0 
# count = 0
# while i < len(numbers):
#     if numbers[i] % 2 == 1:
#         print(numbers[i])
#         count = count + 1
#     i = i + 1
# print("Total odd numbers =" , count)

# numbers = [15, 11, 35, 8, 42, 18, 60]
# i = 0
# while i < len(numbers):
#     if numbers[i] % 2 == 1:
#         print(numbers[i])
#     elif numbers[i] % 2 == 0:
#         break
#     i = i + 1

# names = ["Rakesh", "Rahul", "John"]

# for index, name in enumerate(names):   #Suppose you want both the index and the value.
#     print(index, name)

# numbers = [10, 15, 22, 33, 48, 57, 60]
# i=0
# while i < len(numbers):
#     if numbers[i] % 2 == 0:
#         print(numbers[i])
#     i = i + 1

# students = []
# i = 0
# count = 0
# a = int(input("how many students :"))
# while i < a:
#     name = input("name :")
#     students.append(name)
#     i = i + 1
# cr = input("CR name :")
# students.insert(0, cr)
# rem = input("Remove :  ")
# if rem in students :
#     students.remove(rem)
# else:
#     print("Student not found")
# # total = int(input(""))

# for student in students:
#     print(student)

#     if len(student) > 5:
#         count = count + 1
# print("\nNames with more than 5 letters :", count)

# if count > 2 :
#     print("Large class")
# else:
#     print("Small class")  #what a crazy question uff i got 80% right what i learnt , but last count names have more than 5 letters uff and remembering the pattern which should come firt and later crazyyy


# students = []
# a = int(input("how many students :"))
# for i in range (a):
#     c = input("name :")
#     students.append(c)
# b = int(input("remove student position :"))
# students.pop(b)
# for student in students:
#     print(student)


# students = []
# # a = int(input("how many students :")) removee this if yoy know range is 5 students is 5
# for i in range (5):
#     c = input("name :")
#     students.append(c)
# b = int(input("remove student position :"))
# students.pop(b)
# for student in students:
#     print(student)


# students = []
# a = int(input("how many students :"))
# for i in range (a):
#     c = input("name :")
#     students.append(c)
# cr = int(input("student position for CR :"))
# ex = students.pop(cr)
# students.insert(0, ex)
# lev = input("Which student wants to leave the class :")
# students.remove(lev)
# print(students)

m = []
for i in range (5):
    a = input("Names : ")
    m.append(a)
    
for name in m:
    if len(name) > 5:
        print("larger", name)


# student = []
# for i in range (8):
#     a = input(" name :")
#     student.append(a)

# see = input("search :")
# print(student.count(see))

# students = []
# for i in range (6):
#     a = input("name :")
#     students.append(a)
# find = input("Find :")
# print(students.index(find))

# students = []
# for i in range (7):
#     a = input("name :")
#     students.append(a)
# students.sort()
# print(students)

# students = []
# for i in range (6):
#     a = input("name :")
#     students.append(a)
# students.reverse()
# print(students)