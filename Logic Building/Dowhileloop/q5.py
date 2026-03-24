# Count  and print the factorial of the given number

n = int(input("enter a number : "))
count = 0

while True:
    digit = n % 10
    count+=1
    n = n // 10
    if n == 0:
        break
print(count)
