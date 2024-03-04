#22 Write a Python program input and add two integers only and handle the exceptions. 

def add_and_divide():
    while True:
        try:
            first_value = int(input("Enter First Value: "))
            second_value = int(input("Enter Second Value: "))

            sum_result = first_value + second_value
            try:
                division_result = first_value / second_value
                print("Division result:", division_result)
            except ZeroDivisionError as e:
                print("Division error:", e)

            print("Sum of the two numbers:", sum_result)
            break  

        except ValueError:
            print("Input Integer Only: Invalid literal for int() with base 10")

add_and_divide()

#========================OUTPUT=========================
# Enter First Value: 3
# Enter Second Value: 2
# Division result: 1.5
# Sum of the two numbers: 5

# Enter First Value: 3
# Enter Second Value: 0
# Division error: division by zero
# Sum of the two numbers: 3
# Enter First Value: hy
# Input Integer Only: Invalid literal for int() with base 10
# Enter First Value:
