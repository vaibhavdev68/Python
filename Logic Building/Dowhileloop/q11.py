# Find the HCF of the given numbers 

a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
i = min(a, b)
while True:
    if a % i == 0 and b % i == 0:
        print(i, " is hcf ")
        i -= 1
        break

