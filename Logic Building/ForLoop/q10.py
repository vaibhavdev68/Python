# Print the Fibonacci series up to the required number of terms


n = int(input("Enter a number : "))
a = 0
b = 1

for i in range(1 , n+1):
    c = a+b
    print(a)
    a = b
    b = c
    
