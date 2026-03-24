# Keep taking numbers from the user untill a negative number is entered , then count  how many positve number is added
count = 0
while True:
    n = int(input("Enter a number : "))

    if n < 0:
        break
    elif n != 0:
        count+=1
    else:pass
print("Total +ve number is ", count)
    