""""We First start by planning how the user will find the programe;
Step  1 : Greeting the User
Step 2: Asking user to pick an operation
Step 3: Ask for two numbers
Step 4:Perfome the Operations
Step 5: Show the Results
Step 6: Offer to quit or repeat
"""
#Step 1: Greeting User
print('Welcome to Kasq Calculator')

while True:
    #Step 2: Showing the menu
    print("Choose an operation")
    print("1. Addition (+)")
    print("2. Subtraction")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    #Step 3: getting User's choice
    choice = input("Enter the number of the operation you'd like to perfome:")

    #Step 4: Handling the Exit
    if choice == "5":
        print("Thank you for using the Kasq Simple calculator")
        break

    #Step 5: Checking if the choice is valid
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid Choice. please try again.")
        continue

    #Step 6: Getting two numbers from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("invalid Input! Please enter numbers only.")
        continue 

    #Step 7: Perfome teh choosen operation
    if choice == "1":
        result = num1 + num2
        print(f"The Result of {num1} + {num2} is {result}.")
    elif choice =="2":
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}.")
    elif choice == "3":
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}.")
    elif choice == "4":
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}.")
        else:
            print("Division by zero is not allowed.")
    

    #Step 8: Ask if the user wants to perfome another operation
    repeat = input("Would you like to perform another calculation? (yes/no):"). lower()
    if repeat != "yes":
        print("Thank you for using the Simlpe Kasq Calculator. Goodbye!")
        break

        
        
