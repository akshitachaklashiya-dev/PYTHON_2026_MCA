#22. find a sum of 15 + 25 +………+n5.

n = int(input("Enter n: "))
sum = 0

for i in range(1, n + 1):
    sum = sum + (i * 10 + 5)

print("Sum =", sum)