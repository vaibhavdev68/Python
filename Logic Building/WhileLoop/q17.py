# Print all prime numbers between 1 and 100.
# number have only two factor 1 and itself is known is prime number

n = 100
j = 2
while j <= n/2:
    i = 2
    isPrime = True
    while i < j:
        if j % i == 0:
            isPrime = False
            break
        i += 1
    if isPrime:
        print(j, " - Prime number ")
    
    j+=1
    