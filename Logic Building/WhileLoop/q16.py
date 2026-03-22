# Check whether  the given number is perfect number.
# perfect number is number that is equal to the sum of its proper divisors(excluding the number itself).
# ex. 6 = 1+2+3

num = int(input("Enter a number : "))
i=1
sum = 0
while num>i:
    if num % i ==0:
          sum+=i
    i += 1
if sum==num:
     print(num, "number is perfect number")
else:
     print(num, "number is not perfect number")