# Reverse the given number and print the reversed value

n = int(input("Enter a number : "))
reverse = 0

while True:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
    if n == 0 :
        break
print(reverse)
