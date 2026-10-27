

N = int(input())

large = 0
small = 0

while True:
    bill = int(input())

    if bill == -999:
        break

    if bill > N:
        large += 1
    else:
        small += 1

print(large)
print(small)