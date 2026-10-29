# 3. Write a Python program to create a tuple containing at least ten values, including repeated
# numeric values. Perform the following operations:
# a) Display the tuple and access its elements using positive indexing, negative indexing,
# and slicing.
# b) Perform tuple concatenation using + and repetition using *.
# c) Check whether a specified element exists using in and not in.
# d) Find the maximum, minimum, and length using max(), min(), and len().
# e) Accept a value from the user and count its occurrences using count().
# f)
# Search for a specified element using index(), displaying an appropriate message if it
# is not found

# Create a tuple containing repeated numeric values
numbers = (10, 20, 30, 20, 40, 50, 10, 60, 70, 20)

# (a) Display tuple and access elements
print("Original Tuple:", numbers)

print("Positive Indexing (index 2):", numbers[2])
print("Negative Indexing (index -1):", numbers[-1])
print("Slicing (index 2 to 6):", numbers[2:7])

# (b) Tuple concatenation and repetition
tuple2 = (80, 90)
print("Concatenation (+):", numbers + tuple2)
print("Repetition (*):", numbers * 2)

# (c) Check element using in and not in
search_value = int(input("Enter a number to check: "))

print("Element exists (in):", search_value in numbers)
print("Element does not exist (not in):", search_value not in numbers)

# (d) Maximum, minimum, and length
print("Maximum Value:", max(numbers))
print("Minimum Value:", min(numbers))
print("Length of Tuple:", len(numbers))

# (e) Count occurrences of a value
count_value = int(input("Enter a number to count: "))
print("Occurrences of", count_value, ":", numbers.count(count_value))

# (f) Search for an element using index()
index_value = int(input("Enter a number to find its index: "))

if index_value in numbers:
    print("First occurrence of", index_value,
          "is at index:", numbers.index(index_value))
else:
    print("Element not found in the tuple.")
