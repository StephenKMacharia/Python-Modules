"""Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
Perform the operation based on the user's input and print the result.
Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15."""

print("Hello! Welcome to My Week 1 Assignment")

while True:
    #I want to create a Menu
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    choice = input("Where User Chooses which operation to perfome:")

    num1 = float(input("input the first number:"))
    num2 = float(input("input the second number:"))

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid Choice. Try Again!")

    if choice == "1":
        result= num1 + num2 
        print(f"{num1} + {num2} ={result} ")
    elif choice == "2":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif choice == "3":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif choice == "4":
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid operation")
            break

        
        













