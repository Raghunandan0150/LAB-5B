


N = int(input("Enter a number: "))

count = 0

for i in range(1, N + 1):
    if N % i == 0:
        print(i)
        count += 1

print("Total divisors =", count)

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")