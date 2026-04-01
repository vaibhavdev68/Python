# Continuously add numbers in loop and stop the loop when the sum becomes greater than 100
sum = 0
for i in range(1, 200):
    sum+=i
    print(sum)
    if sum > 100:
        break
    
   
    