# class Student:
#     def __init__(self, name, marks):
#         self.name= name
#         self.marks= marks
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum+= val
#         print("hi",self.name, "Your avg score is: ", sum/3)
# s1 = Student("Vaibhav",[70, 80, 90])

# s1.name = "iron man"
# s1.get_avg()




#Static method are the method they dont use self parameter










#abstraction, Encapsulation, Inheritence, polymorphism



#abstraction

#hiding the implementation details of a class and only showing the essential features to the user
#Enscapsulation => 
#wrapping data and function into a single unit(object)


#quetion =>  1. Create a Account class with 2 attribute - balance & account no.
#quetion =>  2. Create method for debit , credit & printing the balance.


class Account:
    def __init__(self, bal, acc):
        self.balance= bal
        self.account_no = acc

        #debit method 
    def debit(self, amount):
            self.balance -= amount
            print("rs.", amount,"debited")
            print("total balance = ", self.get_balance())


            #credit method 
    def credit(self, amount):
            self.balance += amount
            print("rs.", amount,"credited")
            print("total balance = ", self.get_balance())




    def get_balance(self):
        return self.balance




acc1 = Account(10000, 12345)
print(acc1.balance)
print(acc1.account_no)

acc1.debit(1000)
acc1.credit(500)