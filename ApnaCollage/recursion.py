# # # Recursion 

# # # when function call itself repeatedly






# def show(n):
#     if(n==0):  #base case is use to stop or not
#        return 
#     print(n)
    
#     show(n-1)

# show(6)






# # def print_numbers(n):
    
# #     if n > 5:   # Base case
# #         return
    
# #     print(n)
    
# #     print_numbers(n + 1)   # Recursive call


# # print_numbers(1)




# # def factorial(n):
    
# #     if n == 1:   # Base case
# #         return 1
    
# #     return n * factorial(n-1)


# # print(factorial(5))



# # def sum_numbers(n):
    
# #     if n == 1:
# #         return 1
    
# #     return n + sum_numbers(n-1)


# # print(sum_numbers(5))




# # #RecursionError: maximum recursion depth exceeded
# # def test():
# #     print("Hello")
# #     test()

# # test()





# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     return fact(n-1)*n
# print(fact(6))
 

# write a recursive function to calculate the sum of first n natural numbers.


# def cal_sum(n):
#     if(n==1):
#         return 1
#     return cal_sum(n-1)+n

# print(cal_sum(5))


# write a recursive function to print an element in a list
# use list and index as a parameter




def p_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    p_list(list,idx+1)
list = ["apple", 5, "banana", 6, "mango", "cherry", "lemon"]
p_list(list)

