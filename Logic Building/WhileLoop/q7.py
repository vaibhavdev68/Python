#Calculate the sum of all even number from 1 to n 
n = int(input("Enter a number : "))
sum = 0
i = 1
while i<=n:
    if i%2==0:
        sum+=i
    i+=1
print(sum)