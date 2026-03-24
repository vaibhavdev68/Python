# Print all numbers between a and b that are divisible by 7

a = int(input("Enter a number : "))
b = int(input("Enter a number : "))

i = min(a, b)
n = max(a, b)
for j in range(i,n+1 ):
    if j % 7 == 0:
      print(j)