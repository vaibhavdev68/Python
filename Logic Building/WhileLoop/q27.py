#Find the LCM of two numbers

a = int(input("Enter a number : "))
b = int(input("Enter a number : "))

i = max(a,b)


while i >0:
    if a % i == 0 and b % i == 0:
        print("Lcm is  : " , i)
        break
    i-=1
