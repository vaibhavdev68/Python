# Print the fibonacci series up to  the required number of terms
# 0 1 1 2 3 5 8 13 

n = int(input("Enter a number : "))
a = 0
b = 1
while True:
    print(a)
    c = a+b
    a = b
    b = c
    
    if a > n :
        break
