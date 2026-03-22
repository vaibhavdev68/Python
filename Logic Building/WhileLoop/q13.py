# Check whether the given number is a palindrome

num = int(input("Enter a number : "))
check = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
if check == reverse:
    print("this is palindrome number")
else:
    print("this in not palindrome")
    