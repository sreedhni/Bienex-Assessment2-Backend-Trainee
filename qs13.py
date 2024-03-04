# 13. Implement a program that simulates a basic calculator, allowing users to perform arithmetic operations (addition, subtraction
# multiplication, division) on two numbers. 
def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operand = input("Enter the operator (+, -, *, /): ")

        if operand == "+":
            return F"{num1} + {num2} = {num1+num2}"
        elif operand == "-":
            return F"{num1} - {num2} = {num1-num2}"
        elif operand == "*":
            return F"{num1} * {num2} = {num1*num2}"
        elif operand == "/":
            if num2 != 0:
                return F"{num1} /{num2} = {num1/num2}"
            else:
                return "Error: Division by zero!"
        else:
            return "Error: Invalid operator!"

    except ValueError:
        return "Error: Invalid input! Please enter valid numbers."

result = calculator()
print(result)

#===========================OUTPUT=================================
# Enter the first number: 2
# Enter the second number: 1
# Enter the operator (+, -, *, /): +
# 2.0 + 1.0 = num1+num2
# Enter the first number: 1
# Enter the second number: 2
# Enter the operator (+, -, *, /): +
# 1.0 + 2.0 = 3.0
# Enter the first number: 1
# Enter the second number: 2
# Enter the operator (+, -, *, /): +
# 1.0 + 2.0 = 3.0
# Enter the first number: 1
# Enter the second number: 2
# Enter the operator (+, -, *, /): -
# 1.0 - 2.0 = -1.0
# Enter the first number: 1
# Enter the second number: *2
# Error: Invalid input! Please enter valid numbers.
# Enter the first number: 1
# Enter the second number: 2
# Enter the operator (+, -, *, /): *
# 1.0 * 2.0 = 2.0
# Enter the first number: 1 
# Enter the second number: 2
# Enter the operator (+, -, *, /): /
# 1.0 /2.0 = 0.5
# Enter the first number: 1
# Enter the second number: 0
# Enter the operator (+, -, *, /): /
# Error: Division by zero!
