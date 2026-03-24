#Find the smallest digit in given number


n = int(input("Enter a number : "))

smallest = 9 # max possible digit

while n > 0:
    digit = n% 10
    if digit < smallest :
        smallest = digit
    n = n // 10
print("Smallest digit is ", smallest)
