# Keep taking numbers from the user untill 0 is entered, then print the sum of 
# all entered number
sum = 0

while True:
    
    n = int(input(" enter a number: "))
    sum += n
    if(n==0):
        break
    
print("sum of numbers are : " , sum)



