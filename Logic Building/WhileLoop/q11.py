#Count and print the total number of digit in a given number
num = int(input("Enter a number : "))
count=0
i = 1
while num>0:
    digit= num%10
    count+=1
    num//=10
print(count)
