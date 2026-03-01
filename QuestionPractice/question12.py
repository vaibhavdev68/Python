#Write a program to check number is odd or even

num = int(input("Enter a number: " ))
if(num==0):
    print(f"{num} is zero, is not even")
elif(num%2==0):
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")    
    