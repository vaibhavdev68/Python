# Create a menu_driven program that allows the user to choose and perform different operations.

while True:
    print("\n------ Menu -----")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    

    choice  = int(input("Enter your choice : c"))
    if choice == 5:
        print("Exiting the program .....")
        break
    a = int(input("Enter a first number : "))
    b = int(input("Enter a second number : "))
    
    if choice == 1:
        print("Result: ", a+b)
        break
    elif choice == 2:
        print("Result: ", a-b)
        break
    elif choice == 3:
        print("Result: ", a * b)
        break
    elif choice == 4:
        if b != 0:
            print("Result", a / b)
            
        else:
            print("Can not divide by zero")
        break
    else:
        print("Invalid input , Try Again")

        



