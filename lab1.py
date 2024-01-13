# lab1.py

# Starter code for lab 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# NAME: Julia Bi
# EMAIL: qianranb@uci.edu
# STUDENT ID: 16903084

#https://github.com/QianranJuliaB/ICS32

def calculator():
    print("Welcome to ICS 32 PyCalc!")

    try:
        operand1 = float(input("Enter your first operand: "))
        operand2 = float(input("Enter your second operand: "))
        operator = input("Enter your desired operator (+, -, or x): ")

        if operator == '+':
            result = operand1 + operand2
        elif operator == '-':
            result = operand1 - operand2
        elif operator.lower() == 'x':
            result = operand1 * operand2
        else:
            print("Invalid operator.")
            return

        print(f"The result of your calculation is: {result}")

    except ValueError:
        print("Invalid input.")


calculator()

