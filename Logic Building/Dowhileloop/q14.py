#Find and print the sum of digits of the given number
n = int(input("Enter a number : "))
sum = 0
while True:
    digit = n % 10
    sum+=digit
    n = n // 10
    if n == 0:
        break
print("sum of digits in given numbers is ", sum)
