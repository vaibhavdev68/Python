class Student:
    
    # constructor
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    # method
    def display(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


# creating objects
s1 = Student("Vaibhav", 21, "BCA")
s2 = Student("Rahul", 22, "B.Tech")

# calling method
s1.display()

print("---------------")

s2.display()


#oops 



class Bird:
    def sound(self):
        print("Bird makes sound")


class Sparrow(Bird):
    def sound(self):
        print("Sparrow chirps")


class Crow(Bird):
    def sound(self):
        print("Crow caws")


b1 = Sparrow()
b2 = Crow()

b1.sound()
b2.sound()



n = 5
sum = 0

for i in range(1, n + 1):
    res += i ** 3

print(res)