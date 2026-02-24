# Python 

# 1. Easy to learn and analyse.
print('hi')
# 2. High level language.
# 3. Dynamically typed  language.
a = 56
b = "hello"
# 4. Multi-paradigm
# 5. It is open source.
# 6. It is Platform independent.
# 7. It has extensive libraries.


# keywords
# they are universaly standard words which are predefined by developer, to perform specific task.
# ther are 35 keywords out of 35 keywords 3 are special keywords


# keywords.kwlist => it give all keyword in id.

# 3 special keyword are => False, None, True.
# => why they are special 
# => we can assign them as value to variable.
# => first character of these keyword are in upper case.



# Variable

# => it is a container which is used to store the address of the value .

# variable = value

# memory allocation to variable 
# variable store loction of memory address.
# main space and metohod space


# id() function 
#it is used to get  actual address of the value stored in memory.
#syntax
# id(var/value)
a = 80
print(id(a)) 
print(id(80))


# Multiple variable creation
#Creating multiple variables in a single line is known as multiple variable creation (MVC).
#Syntax
#var1, var2, var3 = val1, val2, val3

name, age, fruit = "vaibhav", 24, "apple"
print(name, age, fruit)

#what hapen in memory allocation if two variable have same value 


d, e, f= 11, 22, 11
print(id(d))
print(id(e))
print(id(f))


p, q, r = 33, 22, 33
print(id(p))
print(id(q))
print(id(r))







