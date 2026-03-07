# Recursion 

# when function call itself repeatedly

def print_numbers(n):
    
    if n > 5:   # Base case
        return
    
    print(n)
    
    print_numbers(n + 1)   # Recursive call


print_numbers(1)




def factorial(n):
    
    if n == 1:   # Base case
        return 1
    
    return n * factorial(n-1)


print(factorial(5))



def sum_numbers(n):
    
    if n == 1:
        return 1
    
    return n + sum_numbers(n-1)


print(sum_numbers(5))




#RecursionError: maximum recursion depth exceeded
def test():
    print("Hello")
    test()

test()