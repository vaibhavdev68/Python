# Check  wether the given number  is a palindrome

n = int(input("Enter a number : "))
reverse = 0
temp = n
while True:
    
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp// 10
    if temp == 0:
        break
if n == reverse:
    print( n , "is palindrome number")
else:
    print(n, "is not palindrome")