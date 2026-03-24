# Calculate and print the sum of even digits and the sum of odd digits of the given number separately

n = int(input("Enter a number : "))
sumEven = 0
sumOdd = 0
count = 0 
while True:
    count+=1
    digit = n % 10
    
    if digit % 2 == 0:
        sumEven += digit
    else:
        sumOdd +=digit
    n = n // 10

    if count == 5:
        break
print("Sum of even digit", sumEven)
print("sum of odd digit : ", sumOdd)
        





























# sumOfEven = 0
# sumOfOdd = 0
# count = 0
# while True :
#     n = int(input("Enter a number : "))
#     count+=1

    
#     if n % 2 == 0:
#         sumOfEven+=n
        
#     else:
#         n % 2 != 0
#         sumOfOdd += n
#     if count == 6:
#        break
  
# print("sum of even numbers are", sumOfEven)
# print("sum of odd is : ", sumOfOdd)

