# Thayer Yang
# 08 OCT 2024
# Basic Calculator

def getNumber(message):
    # (String) Message: string text prompted for the input message.
    number = 0
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print("Invalid number.")


print("""Hello, welcome to my Basic Calculator!
This script will prompt you to enter two numbers
and then add, subract, multiply, or divide the numbers
depending on the menu option you select.
      
Choose a math operation to perform:
    1. Addition (+)
    2. Subtraction (-)
    3. Multiplication (*)
    4. Division (/)""")

# Gets wanted operation
while True:
    operation = int(getNumber("Enter your choice (1-4): "))
    if operation >=1 and operation <=4:
        break
    else:
        print("Invalid input. Please enter the integers 1-4 for wanted operation.")

#User inputs numbers
num1 = getNumber("Please enter your first number: ")
num2 = getNumber("Please enter your second number: ")

if operation == 1: # Addition
    answer = num1 + num2
    print(f'{num1} plus {num2} equals: {answer}')

elif operation == 2: # Subtraction
    answer = num1 - num2
    print(f'{num1} minus {num2} equals: {answer}')

elif operation == 3: # Multiplication
    answer = num1*num2
    print(f'{num1} times {num2} equals: {answer}')

elif operation == 4: # Division
    if num2 == 0: #Checks if user is dividing by 0
        print("ERROR: Cannot divide by zero.")
    else:
        answer = num1/num2
        print(f'{num1} divide by {num2} equals: {answer}')

