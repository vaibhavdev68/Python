# Find the HCF (Highest Common Factor) of two given numbers.
# Highest common factor is the largest number that divides two or more numbers exactly (Without leaving a reaminder).

#Simple while loop => Starts from smaller number and go down

a = int(input("Enter a number : "))
b = int(input("Enter a number : "))

i = min(a,b)

while i > 0: 
    if i % a == 0 and i % b == 0:
        print("hcf is : ", i)
        break
    i+=1