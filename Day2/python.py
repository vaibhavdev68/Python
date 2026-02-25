# # => Identifiers

# # Name given to variable is known as identifier.
# # Giving name uniquely to store the value.
# # or  the name given to the variable , function , class , objects or method


# # five rules of identifiers

# # 1. Identifier should not be a keywords.
# # Keywords are already predefined with some task. 

# # 1. Identifier should not start with number.
# name2 ="shivam"
# print(name2)

# a1a = "apple"
# print(a1a)

# # 3. Identifier should not contain any special character except _(uderscore).
# _name = "vaibhav"
# print(_name)

# # all the special character are predefined with some specific task except _. 

# # 4. Identifier should not contain any wide space (space) at the starting and in between
# # because of seprator



# # Industrial standard rules
# # => identifier name can't exceed more than 79 character.

# # Data types

# # => it is going to specify tyepes of data 
# # with the help of this we are able to know what kind of operation , we are going to perform.

# # data types

# # 1. single value data types
# # int
# # float
# # complex
# # bool

# #2. multi-Value
# # String 
# # list
# # tuple
# # set
# # dictionary


# # Single value data types
# # => it is going to store single value in variable
# # int=> it is a real number without decimal points.
# #it range from -infinty to + infinity.

# b = -84
# type(b)
# # type function => it will return the data type of the value.
# print(type(b))

# # default value(0 zero) => it is an initial value and  they are internally equal to false.
 

# # bool function  => it will return weather the value is default or not default.
# # bool(var/value)
# n = 0
# bool(n)
# print(bool(n))

# # float
# # It is a real number with decimal point. 
# d = 5.6
# print(type(d))
# # memory allcation of above in method space and main space.
# # default value for float is zero.zero
# # print(type(0.0))


# # complex number  
# # => it is combination of real number and imaginary number.
# # a+-bj
# #  where a = real and bj= imaginary

# # c = 5+6j
# # print(type(c)) 

# # => default value for complex
# # 0+oj are deafult ValueError
# # bool(0+0j)
# # except j we cannot pass any character as imaginary part.
# #  type(3+5J)

# #  memory allocation
# print(type(0-0j))
# print(bool(0-0j))


# boolean

# # it consits of two value.
# # it use as resultant.
# # default value of bool is false.
# # false is internally considered as zero.
# bool(False)

# # default value for boolean is false 


c = 0-0j
print(c)
print(type(c))
print(bool(c))