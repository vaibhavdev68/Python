#Print numbers from 1 to 100 and stop the loop as soon as numbers is divisible by 17 is encountered

for i in range(1, 101):
    print(i)
    if i % 17 == 0:
        break
