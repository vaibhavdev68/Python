# #del keyword 
# #used to delete object and their properties'


# class Student:
#     def  __init__(self, name):
#         self.name = name
# s1 = Student("Khushi")
# print(s1.name)

# del s1.name
# print(s1)



# Private(like)


class Account: 
    def __init__(self, acc_no, acc_pas):
        self.acc_no = acc_no
        self.__acc_pas = acc_pas
        