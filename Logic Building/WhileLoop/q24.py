#print all the factor of given number
# if number from 1 to n is completely divide the numbe that is factor of n.

n = int(input("Enter a number : "))
i = 1
while i <= n/2: 
    if n%i==0:
        
        print(i, end=" ")
    i += 1 



