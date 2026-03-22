#Find the product of all digit of given number
num = int(input("Enter a number : "))
product=1
while num >0:
    digit = num % 10
    product*= digit
    # print(digit)
    num//=10
print(product)