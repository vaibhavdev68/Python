# find the lcm of the given number
a = int(input("Enter a number : "))
b = int(input("Enter a number : "))

maxnum = max(a, b)
n = (a*b)
for i in range(maxnum,n+1, 1):
    if i % a == 0 and i % b == 0:
        print(i,"is lcm")
        break