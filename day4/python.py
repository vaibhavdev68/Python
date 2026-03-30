# # name ="vaibhav"
# # print(id(name))
# # q = "vaibhav"
# # print(id(q))


# #! list 
# #=> it is collection of homogeneous and hetrogenious data types enclosed between [] . (square braces)

# # l1 =[val1, val2, val3]
# example = [True,243545, "vaibahv", 45.67, 2-3j]
# print(example)
# #memory allocation of this in main space and method space
# #method space having block of memory to store value and collection value store in another block and method space store  address of that.

# # main space store memory address of method space.

# print(example[1::2])

# nesList = [3,5.6,'hi',55,[5, 6, 7],6.9]
# print(nesList[-2])

# print(nesList[4:5:])
# print(nesList[4][1])

# #! modification of element by indexing
# # todo => var[index] = new_value

# nesList[1]= 77
# print(nesList)

# nesList[-1] = 99
# print(nesList)

# # nesList[4] = "Jaduagar"
# nesList[4][1] = "ladle"

# print(nesList)

# nesList[3]="hello"
# print(nesList)
# # nesList[3][1] = "E"

# print(nesList[3][1].upper())

# #! String is immutable data types
# #! list is ordered data type 
# #! it allows duplicate value
# #! default value of list is empty list  list =[]
# list =[4]
# print(type(list))

# #! inbuilt function of list
# #! append => it will add the new element at the last position of the list. it will only append single value

# list.append("vaibahv")
# print(list)

# #! insert() => it will add new  element at specified index.
# #! syntax =>  var.insert(index,value).


# list = [3, True,'hi',33,8.9,[2,3,4],False]
# list.insert(2,'hello')
# print(list)
# list.insert(5,6564)
# print(list)
# list[-2].insert(3,999)
# print(list)




# #! pop => it will eliminate last value from the  list
# #! syntax => var.pop(value)
# list3 = [2, 3, 4 ,5,6 ,5,'']
# list3.pop(2)
# print(list3)

# # list.pop
# # print(list.pop())

# # print(list[-2].pop(1))


# #! remove=> it will remove th specified value from the list.

# # print(list.remove('hello'))
# # print(list)


# #! Tuple => 
# #! syntax => 

# # type(tup)  = it use to check type of variable

# tup=(3,4,4,543,'heloo',3.4, 8-9j, [4,4.6, 43])
# print(type(tup))
# #! tuple is ordered data type.
# #! it allows duplicate values.
# #! default value for tuple.
# #! to store single value in a tuple  tup = (4,)   => ,(comma) after value.
# #! tuple is immutable data types.

# oneTup =(5)
# print(type(oneTup))


# #! Set => it is collection of homogenious nd hetrogenion mixture of data enclosed with {}

# set1 = {3,5,5.6,(30,60,53),True}
# print(set1)

# print(set1)

# #! => set is unordered data types]
# # => it does not allow duplicates value.
# #= > set is mutable data type. but it does not accept mutable data types as value.
# #=> it does not support indexing.


# set5 ={2,1,True,2,1,3.5,False}








import random
import math
# Taking Inputs
lower = int(input("Enter Lower bound:- "))
 
# Taking Inputs
upper = int(input("Enter Upper bound:- "))
 
# generating random number between
# the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ", 
       round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")
 
# Initializing the number of guesses.
count = 0
 
# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1
 
    # taking guessing number as input
    guess = int(input("Guess a number:- "))
 
    # Condition testing
    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")
 
# If Guessing is more than required guesses,
# shows this output.
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")