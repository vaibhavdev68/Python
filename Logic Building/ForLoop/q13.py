# Find and print the sum of all factors of the given number
n = int(input("Enter a number : "))
sum = 0
for i in range(1, n+1):
   if n % i == 0:
      sum+=i
print(sum, "is sum of all factors")

