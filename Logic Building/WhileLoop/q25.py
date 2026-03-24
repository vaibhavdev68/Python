#Find and print the sum of all factors of the given number
n = int(input("Enter a number : "))
i = 1
sumf=0
while i < n : 
    if n % i == 0:
        sumf+=i
    i+=1
print(sumf)
