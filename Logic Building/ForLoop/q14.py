# Find the HCF (Highest Common Factor) of the given number
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

i = min(a, b)
for i in range(i,0, -1):
    if a % i == 0 and b % i == 0:
         print(i , "is the highest comman factor")
         break
     