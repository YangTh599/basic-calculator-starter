print("""Hello, welcome to my Basic Calculator!
This script will prompt you to enter two numbers
and then add, subract, multiply, or divide the numbers
depending on the menu option you select.
      
Choose a math operation to perform:
    1. Addition (+)
    2. Subtraction (-)
    3. Multiplication (*)
    4. Division (/)""")

option = 0

while True:
    option = int(input("Enter your choice (1-4): "))
    if option >=1 and option <=4:
        break
    else:
        print("Invalid input.")

num1 = float(input("Please enter your first number: "))
num2 = float(input("Please enter your second number: "))

if option == 1:
    answer = num1 + num2
    print(f'{num1} plus {num2} equals: {answer}')
elif option == 2:
    answer = num1 - num2
    print(f'{num1} minus {num2} equals: {answer}')
elif option ==3:
    answer = num1*num2
    print(f'{num1} times {num2} equals: {answer}')
elif option ==4:
    if num2 == 0:
        print("ERROR: Cannot divide by zero.")
    else:
        answer = num1/num2
        print(f'{num1} divide by {num2} equals: {answer}')

