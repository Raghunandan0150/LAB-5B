

n = int(input("Enter a number: "))
D = int(input("Enter a digit (0-9): "))

count = 0

while n > 0:
    digit = n % 10

    if digit == D:
        count += 1

    n = n // 10

print("Count =", count)
