# Print the multiplication tabel of a given number

n = int(input("Enter a number : "))
i = 1
while True: 
    print(f"{n} * {i} = {n*i}")
    i+=1
    if i > 10: 
        break
