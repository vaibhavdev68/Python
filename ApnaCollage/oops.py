# # # def under_attack(col, queens):
# # #     left = right = col

# # #     for r, c in reversed(queens):
# # #         left, right = left - 1, right + 1

# # #         if c in (left, col, right):
# # #             return True
# # #     return False

# # # def solve(n):
# # #     if n == 0:
# # #         return [[]]

# # #     smaller_solutions = solve(n - 1)

# # #     return [solution+[(n,i+1)]
# # #         for i in range(BOARD_SIZE)
# # #             for solution in smaller_solutions
# # #                 if not under_attack(i+1, solution)]
# # # for answer in solve(BOARD_SIZE):
# # #     print (answer)





# # class Parrot:

# #     # class attribute
# #     name = ""
# #     age = 0

# # # create parrot1 object
# # parrot1 = Parrot()
# # parrot1.name = "Blu"
# # parrot1.age = 10

# # # create another object parrot2
# # parrot2 = Parrot()
# # parrot2.name = "Woo"
# # parrot2.age = 15

# # # access attributes
# # print(f"{parrot1.name} is {parrot1.age} years old")
# # print(f"{parrot2.name} is {parrot2.age} years old")


# # start, end = -5, 0  
# # for i in range(start, end + 1):  
# #     if i < 0:  # Check if the number is negative
# #         print(i)














# x, y = input("Enter two values: ").split()
# print("Number of boys: ", x)
# print("Number of girls: ", y)




def greet(name: str, times: int = 1) -> str:
    """
    Generate a greeting message.

    Args:
        name: The person's name.
        times: How many times to repeat the greeting.

    Returns:
        The greeting string.
    """
    return f"Hello, {name}! " * times

hi = greet("vaibahv")
print(hi)
