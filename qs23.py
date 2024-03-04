# 23. The program takes input from the user and checks if whether the input value is an integer or not, if the input value is not an integer then the 
# program will through a Type exception. 

def check_type():
    while True:
        try:
            user_input = input("Enter your input value : ")
            integer_value = int(user_input)
            print(f"it is integer value.({integer_value})")
            break
        except ValueError:
            print("Invalid Input. Please Input an Integer Only.")

check_type()
#========================OUTPUT=====================
# Enter your input value: huui
# Invalid Input. Please Input an Integer Only.
# Enter your input value: hju78
# Invalid Input. Please Input an Integer Only.
# Enter your input value: 56
# it is integer value.(56)

# or

def check_type():
    while True:
        user_input = input("Enter your input value: ")
        if user_input.isdigit(): 
            integer_value = int(user_input)
            print(f"it is integer value.({integer_value})")
            break
        else:
            print("Invalid Input. Please Input an Integer Only.")

check_type()



# or

class TypeException(Exception):
    pass

def check_type():
    while True:
        try:
            user_input = input("Enter your input value: ")
            integer_value = int(user_input)
            print(integer_value)
            break
        except ValueError:
            raise TypeException("Invalid Input. Please Input an Integer Only.")

try:
    check_type()
except TypeException as e:
    print(e)

