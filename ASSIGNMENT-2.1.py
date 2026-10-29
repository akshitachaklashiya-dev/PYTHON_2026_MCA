# 1. Write a Python program to create a list of ten integers using the range() function. Perform
# the following operations:
# a) Display the list and access its elements using positive indexing, negative indexing,
# and slicing.
# b) Update an element at a specified index entered by the user.
# c) Perform list concatenation using + and repetition using *.
# d) Check whether a number exists in the list using in and not in.
# e) Perform the following list methods: append(), insert(), remove(), pop(), reverse(),
# and count().
# f)Display the list in ascending and descending order using sort() and sorted().
# g) Create an alias and a clone of the list, modify one element, and demonstrate the
# difference between aliasing and cloning.
# h) Display the maximum, minimum, and length of the list using max(), min(), and
# len()
# Create a list of ten integers using range()
numbers = list(range(1, 11))

# (a) Display list and access elements
print("Original List:", numbers)

print("Positive Indexing (index 2):", numbers[2])
print("Negative Indexing (index -1):", numbers[-1])
print("Slicing (index 2 to 6):", numbers[2:7])

# (b) Update an element at a user-specified index
index = int(input("Enter index to update (0-9): "))
if 0 <= index < len(numbers):
    value = int(input("Enter new value: "))
    numbers[index] = value
    print("Updated List:", numbers)
else:
    print("Invalid index!")

# (c) List concatenation and repetition
print("Concatenation (+):", numbers + [11, 12])
print("Repetition (*):", numbers * 2)

# (d) Membership operators
num = int(input("Enter a number to search: "))
print("Number exists (in):", num in numbers)
print("Number does not exist (not in):", num not in numbers)

# (e) List methods
numbers.append(20)
print("After append(20):", numbers)

numbers.insert(2, 30)
print("After insert(2, 30):", numbers)

numbers.remove(30)
print("After remove(30):", numbers)

removed = numbers.pop()
print("Popped Element:", removed)
print("After pop():", numbers)

numbers.reverse()
print("After reverse():", numbers)

count_num = int(input("Enter a number to count: "))
print("Count of", count_num, ":", numbers.count(count_num))

# (f) Sort in ascending and descending order
numbers.sort()
print("Ascending Order using sort():", numbers)

numbers.sort(reverse=True)
print("Descending Order using sort():", numbers)

print("Ascending using sorted():", sorted(numbers))
print("Descending using sorted():", sorted(numbers, reverse=True))

# (g) Aliasing and cloning
alias = numbers
clone = numbers.copy()

alias[0] = 100
print("After modifying alias:")
print("Original List:", numbers)
print("Alias List:", alias)
print("Clone List:", clone)

# (h) Maximum, minimum, and length
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Length:", len(numbers))
