# Calculate adn print the factorial of the given number

n = int(input("Enter a number : "))
fact = 1
i = 1
while True:
    fact = fact * i
    if i==n:
        break
    i+=1
print(fact)