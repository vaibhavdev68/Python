# # while loop

# count = 1
# while count<=5:
#     print('hello ')
#     count+=1
# print(count)           


# i = 1
# while i<=5:
#     print("heloo bhai")
#     i+=1
# print(i)    

# i = 1
# while i<=100:
#     print(i)
    # i+=1
# i = 100
# while i>=1:
#     print(i)
#     i-=1



# n = int(input(" Enter a number "))
# j=1
# while j<=10:
#      print(f"{n} * {j} = {j*n}")
#      j+=1




# l1 = [1,4,9,16,25,36,49, 64,81,100]
# index = 0
# while index<len(l1):
#     print(l1[index])
#     index +=1



# x = 4

# tup = ( 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 4)
# idx = 0
# while idx < len(tup):
   
#     if(tup[idx]== x):
#         print("found number is matched at index", idx)
           
    
#     else:
#         print("finding...")

#     idx+=1

# Break and continue
# i = 0
# while i <=5:
    
#     if(i==3):
#       i+=1

#       continue #skip
#     print(i)
#     i += 1



# i = 1
# while i<=10:
#     if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1

    

#for loop are used for sequential element
# list = [1, 2, 3, 4, 5]

# for num in list:
#     print(num)




# veg = ["potato", "mango", "brinjal", "ladyfinger", "cucumber", ["tomato", "pumpkin"]]
# for cook in veg:
#     print(cook)
#     print(type(cook))


# str = "apnacollage"
# for char in str:
#     print(char)
# # else:
# #     print("loop end")  optional 




#range 
# seq = range(5)


# print(seq[0])
# print(seq[1])
# print(seq[2])
# print(seq[3])
# print(seq[4])


# for i in range(1,101):
#     print(i)




# for i in range (100,0,-1):
#     print(i)

# n = 6

# for i in range (1,11):
#     print(f" {n} * {i} = {n*i}")




#pass state ment 

# for i in range(5):
#     pass 
#     #emty
# print("some use full work")    


# wap to find the sum of first n number using while

n = int(input("enter a number"))
i = 1
sum=0
while i<=n:
    sum+=i
    i+=1
print(sum)