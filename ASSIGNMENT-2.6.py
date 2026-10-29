# 6. Write a Python program using Python's array module to create an integer array containing
# at least eight elements. Perform the following operations:
# a) Display the array and access elements using indexing and slicing.
# b) Insert a new element at a specified position using insert().
# c) Remove a specified element using remove() and remove the last element using
# pop().
# d) Search for an element and display its index if found; otherwise, display an
# appropriate message.
# e) Check element membership using in and not in.
# f)
# Display the maximum, minimum, and length of the array.
# g) Reverse the array and display the final result

import array

# Create an integer array containing eight elements
numbers = array.array('i', [10, 20, 30, 40, 50, 60, 70, 80])

# (a) Display array and access elements using indexing and slicing
print("Original Array:", numbers)

print("Element at index 2:", numbers[2])
print("Last element using negative indexing:", numbers[-1])
print("Slicing (index 2 to 5):", numbers[2:6])

# (b) Insert a new element at a specified position
position = int(input("\nEnter position to insert (0 to 8): "))
value = int(input("Enter value to insert: "))

if 0 <= position <= len(numbers):
    numbers.insert(position, value)
    print("Array after insertion:", numbers)
else:
    print("Invalid position!")

# (c) Remove a specified element and the last element
remove_value = int(input("\nEnter element to remove: "))

if remove_value in numbers:
    numbers.remove(remove_value)
    print("Array after remove():", numbers)
else:
    print("Element not found; cannot remove.")

if len(numbers) > 0:
    removed_element = numbers.pop()
    print("Element removed by pop():", removed_element)
    print("Array after pop():", numbers)
else:
    print("Array is empty; cannot pop an element.")

# (d) Search for an element and display its index
search_value = int(input("\nEnter element to search: "))

if search_value in numbers:
    print("Element found at index:", numbers.index(search_value))
else:
    print("Element not found in the array.")

# (e) Check membership using in and not in
check_value = int(input("\nEnter element to check membership: "))

print("Element exists (in):", check_value in numbers)
print("Element does not exist (not in):", check_value not in numbers)

# (f) Display maximum, minimum, and length
if len(numbers) > 0:
    print("\nMaximum Element:", max(numbers))
    print("Minimum Element:", min(numbers))
    print("Length of Array:", len(numbers))
else:
    print("\nArray is empty.")

# (g) Reverse the array
numbers.reverse()
print("Reversed Array:", numbers)
