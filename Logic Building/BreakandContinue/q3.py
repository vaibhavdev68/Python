# take 5 numbers as input , skip any number that is 0 using continue , and calculate the sum of the remaining numbers
sum = 0
for i in range(1, 6):
 
  n = int(input("Enter a number: "))
  if n == 0:
    continue
  sum+=n
print(sum)