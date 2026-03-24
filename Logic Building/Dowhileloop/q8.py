# Check wether the given number is armstrong 
n = int(input("Enter a number "))
temp = n 
sum = 0
counts = len(str(n))
while True:
    digit = temp % 10
    sqr = digit ** counts
    sum+=sqr
    temp = temp// 10
    if temp == 0:
        break
if sum == n :
    print(n, "is armstrong number ")
else:
    print(n, " is not a armstrong number")
