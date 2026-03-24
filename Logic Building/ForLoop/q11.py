# Find and print the sum of the fibonacci series.
n  = int(input("Enter a number : "))
a = 0
b = 1
sum = 0
for i in range(1, n+1):
    c = a + b
    sum+=a
    print(a)
    a = b
    b = c
print("Sum of all fibonacci is ",sum)