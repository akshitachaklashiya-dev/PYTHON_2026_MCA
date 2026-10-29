# 2. Write a Python program to create a list containing the names of five students (list1)and a
# nested list containing the names and marks of at least five students(list2). Perform the
# following operations:
# a) Accept a student name from the user and search for it in the student list. Display its
# index if found; otherwise, display an appropriate message.
# b) Sort student names in ascending and descending alphabetical order using sort() and
# sorted().
# c) Add a new student name, insert a name at a specified position, and remove a student
# name.
# d) Display all student records using a loop(list2).
# e) Find the student who obtained the highest marks and calculate the average
# marks(list2).
# f)
# Display the number of student records using len()(list2)

# Create list1 containing names of five students
list1 = ["Amit", "Priya", "Rahul", "Neha", "Karan"]

# Create list2 containing student names and marks
list2 = [
    ["Amit", 85],
    ["Priya", 92],
    ["Rahul", 78],
    ["Neha", 95],
    ["Karan", 88]
]

print("Original Student List:", list1)

# (a) Search for a student name
search_name = input("Enter student name to search: ")

if search_name in list1:
    print(search_name, "found at index:", list1.index(search_name))
else:
    print("Student name not found in the list.")

# (b) Sort names in ascending and descending order
list1.sort()
print("Ascending Order using sort():", list1)

list1.sort(reverse=True)
print("Descending Order using sort():", list1)

print("Ascending Order using sorted():", sorted(list1))
print("Descending Order using sorted():", sorted(list1, reverse=True))

# (c) Add, insert, and remove student names
list1.append("Pooja")
print("After adding a student:", list1)

name = input("Enter a student name to insert: ")
position = int(input("Enter position (index) to insert at: "))

if 0 <= position <= len(list1):
    list1.insert(position, name)
    print("After inserting a student:", list1)
else:
    print("Invalid position!")

remove_name = input("Enter student name to remove: ")

if remove_name in list1:
    list1.remove(remove_name)
    print("After removing a student:", list1)
else:
    print("Student name not found; cannot remove.")

# (d) Display all student records using a loop
print("\nAll Student Records:")
for student in list2:
    print("Name:", student[0], "| Marks:", student[1])

# (e) Find student with highest marks and calculate average
highest_student = max(list2, key=lambda student: student[1])
print("\nStudent with Highest Marks:", highest_student[0])
print("Highest Marks:", highest_student[1])

total_marks = sum(student[1] for student in list2)
average_marks = total_marks / len(list2)

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

# (f) Display number of student records
print("\nNumber of Student Records:", len(list2))
