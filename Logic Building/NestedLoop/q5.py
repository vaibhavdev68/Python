# Printing the fibonacci patter row by row , where each row print the next fibonacci numberz

n = int(input("Enter a number : "))
a = 0
b = 1
for i in  range(1, n+1):
  
    for j in range(1, i+1):
        print(a, end=" ")
        c = a+b
        a = b
        b = c 
    print()