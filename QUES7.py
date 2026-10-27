

n = int(input("Enter a number: "))

if n <= 0:
    print("Invalid Input")

elif n == 1:
    print("Not a Perfect Number")

else:
    total = 1
    i = 2

    while i * i <= n:
        if n % i == 0:
            total = total + i

            if i != n // i:
                total = total + (n // i)

        i += 1

    if total == n:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")