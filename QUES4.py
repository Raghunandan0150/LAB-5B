

# Take a positive integer N and a positive integer P as input and find the value of N raised to thepower P using a while loop. Do not use the ** operator or the pow() function. Handle invalidcases as well.

N = int(input("Enter N: "))
P = int(input("Enter P: "))

if N <= 0 or P <= 0:
    print("Invalid Input")
else:
    result = 1
    count = 0

    while count < P:
        result = result * N
        count += 1

    print("Answer =", result)