# For every number from 1 to n  count and print the total number of its factors


n = int(input("Enter a number : "))

for i in range(1, n+1):
    print(f"factor of {i} = ", end=" ")
    for j in range(1, i+1):
        if i % j == 0:
            print(j, end=" ")
    print()
      