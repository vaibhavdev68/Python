# Find and print the sum of all odd numbers from 1 up to n.

n = int(input("Enter a number : "))
sum = 0
for i in range(1, n+1):
    if i % 2 != 0:
        sum+=i
print(sum)





n = int(input("Enter a number : "))
sum = 0
for i in range(1, n+1):
    if i % 2 != 0:
        sum+=i
print(sum)