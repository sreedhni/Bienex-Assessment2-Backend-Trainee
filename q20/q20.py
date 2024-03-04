#20. Create a Python library with the function to input the values with expectation handling and demonstrate with the example. 

def get_input(prompt, data_type, error_message="Invalid input. Please try again."):
    while True:
        try:
            user_input = data_type(input(prompt))
            return user_input
        except ValueError:
            print(error_message)
def get_positive_integer(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input > 0:
                return user_input
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

#example is given in example.py file