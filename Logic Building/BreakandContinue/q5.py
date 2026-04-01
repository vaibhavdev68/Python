# Keep taking numbers from the user and print them untill a negative numbers appears , then stop the loop

while(True):
    n = int(input("Enter a number : "))
    
    if n < 0 :  
        break
    print(n)