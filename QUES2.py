

#Take a positive integer as input and display the product of its digits. The number can be of any length

n = int(input("Enter a number: "))

product = 1

while n > 0:
    digit = n % 10
    product = product * digit
    n = n // 10

print("Product of digits =", product)