# Skip all odd numbers in a loop and stop the loop when the sum becomes greater than 100

n = int(input("Enter a number : "))
for i in range(1, n):
    if i % 2 !=0:
        continue
    print(i)
