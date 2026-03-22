# Check whether the given number is a prime number
n = int(input("Enter a number : "))
i = 2
isPrime = True
while i < n:
    if n % i==0 :
        isPrime = False
        break
    i+=1
if isPrime:
    print("Prime number")
else:
    print("Not a prime")
     

