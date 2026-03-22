#Check whether the given number is an Armstrong number
num = int(input("Enter a number : "))
temp = num
sum = 0 
count= len(str(num))
while temp > 0:
    
    digit = temp %10
    sum+= digit **count
    temp//=10
if num == sum:
    print("Number is palindrome")
else:
    print("Not a armstrong number")