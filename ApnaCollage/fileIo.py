#file input and output in python
#Python can be used to perform operation on a file. (read and write data)
# Types of files 
# ! => Text files : .txt, .docx, .log, etc.
# ! => Binary files : .mp4 , .mov, .png, .jpeg etc.


# open , read and close file
# we have to open a file before reading and writing

# f= open("demo.txt","r")
# data = f.read()
# f.close()
# data1 = f.readline()
# data2 = f.readline()
# print(data)
# print(data1)
# print(data2)

# f.close()

# f = open("demo.txt","w")
# f.write("i am writing in python. 7653456875")
# f.close()
# f = open("sample.txt","a")

# f.close()


# f = open("sample.txt","r+")
# f.write("abc")
# print(f.read())
# f.close()

# f = open("sample.txt", "w+")
# print(f.read())

# f.write("hello world")


# With Syntax 


# with open("demo.txt", "r")as f:
#     data = f.read()
#     print(data)
# with open("demo.txt","w") as f:
#     data1 = f.write("new data")
#     print(data1)
    


# # deleting a file 
# import os
# os.remove("sample.txt") 

# f = open("sample.txt", "w+")
# f.write("hi Everyone " \
# " we are learning File I/O" \
# "using python." \
# "i like programming in python"
# )

# with open("practice.txt","w") as f:
#     f.write("hi everyone\nwe are learning file i/o \n")
#     f.write("using java.\ni like programming in java.")


# with open("practice.txt","r") as f:
#     data = f.read()
# new_data = data.replace("java", "Python")
# print(new_data)
# with open("practice.txt","w") as f:
#     f.write(new_data)


#Try to find "learning" in practice.txt

# with open("practice.txt","r") as f:
#     data = f.read()
#     if(data.find("learning") >=0):
#         print("found")
#     else:
#         print("not found")



# Waf to find in which line of the file does the word "learning" occur first
# print -1 if word not found


