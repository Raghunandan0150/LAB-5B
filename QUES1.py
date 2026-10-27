

X = int(input())
Y = int(input())
N = int(input())

count = 0

for i in range(X, Y):   # X ≤ i < Y
    if i % N != 0:
        print(i, end=" ")
        count += 1

print()
print(count)