# def under_attack(col, queens):
#     left = right = col

#     for r, c in reversed(queens):
#         left, right = left - 1, right + 1

#         if c in (left, col, right):
#             return True
#     return False

# def solve(n):
#     if n == 0:
#         return [[]]

#     smaller_solutions = solve(n - 1)

#     return [solution+[(n,i+1)]
#         for i in range(BOARD_SIZE)
#             for solution in smaller_solutions
#                 if not under_attack(i+1, solution)]
# for answer in solve(BOARD_SIZE):
#     print (answer)





class Parrot:

    # class attribute
    name = ""
    age = 0

# create parrot1 object
parrot1 = Parrot()
parrot1.name = "Blu"
parrot1.age = 10

# create another object parrot2
parrot2 = Parrot()
parrot2.name = "Woo"
parrot2.age = 15

# access attributes
print(f"{parrot1.name} is {parrot1.age} years old")
print(f"{parrot2.name} is {parrot2.age} years old")