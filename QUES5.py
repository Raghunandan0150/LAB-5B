
#Take two positive integers as input. Check whether the second number is the exact reverse ofthe first one. Do not use any inbuilt reverse functions.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

temp = num1
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

if reverse == num2:
    print("Yes, second number is the reverse of first number")
else:
    print("No, second number is not the reverse of first number")
