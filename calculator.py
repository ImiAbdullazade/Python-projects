def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero"
    else:
        return x / y

def calculator_game():
    while True:
        print("\nOptions")
        print("Enter 'add' to add two numbers")
        print("Enter 'subtract' to subtract two numbers")
        print("Enter 'multiply' to multiply two numbers")
        print("Enter 'divide' to divide two numbers")

        user_input = input("Enter your choice ").lower()

        if user_input == "quit":
            print("Thanks for playing!")
            break
        elif user_input in ('add', 'subtract', 'multiply', 'divide'):
            num1 = float(input('enter first number:  '))
            num2 = float(input('enter second number:  '))

            if user_input == 'add':
                print(f"the result is {add(num1, num2)}")
            elif user_input == 'subtract':
                print(f"the result is {subtract(num1, num2)}") 
            elif user_input == 'multiply':
                print(f"the result is {multiply(num1, num2)}")
            elif user_input == 'divide':
                print(f"the result is {divide(num1, num2)}")
                
        else:
            print("unknown input, please try again")

calculator_game()
