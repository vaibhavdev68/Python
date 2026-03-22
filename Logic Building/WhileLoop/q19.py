#Print the Fibonacci series up to n terms.
# The fibonacci series is a sequence of numbers where each number is the sum
# of the two previous number 
# 0 ,1 , 1, 2, 3 , 5, 8, 13 ,21 ,34, ...
 

# t1 = 0
# t2 = 1

# i = 1
# n = 11
# while i <= n :
#     t3 = t1+t2
#     print(t1)

#     t1 = t2
#     t2 = t3
#     i+=1 


n = int(input("Enter a number to check fibonacci : "))
a = 0
b=1
i=0
while i <n :
   print(a, end=" ")
   c = a+b
   a = b
   b=c
   i+=1







