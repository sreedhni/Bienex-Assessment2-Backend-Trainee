# 10. Write a Python function that takes a list of numbers as input and returns 
# the sum of all the numbers divisible by 3 or 5.
def sum_of_3_5_divisible_number(input_list):
    try:
        return sum(num for num in input_list if num % 3 == 0 or num % 5 == 0)
    except TypeError:
        print("Error: Input list contains non-numeric values.")
        return None

try:
    user_input = input("Enter numbers separated by commas or spaces: ")
    user_list = [float(x) for x in user_input.replace(",", " ").split()]
    result = sum_of_3_5_divisible_number(user_list)
    if result is not None:
        print("Sum of numbers divisible by 3 or 5:", result)
except ValueError:
    print("Error: Please enter valid numbers separated by commas or spaces.")
except Exception as e:
    print("An error occurred:", e)

#==================================OUTPUT================================
    
# Enter numbers separated by comma or space: 1 2 3 4 5 10
# Sum of numbers divisible by 3 or 5: 18.0
# Enter numbers separated by commas or spaces: 1 2 7
# Sum of numbers divisible by 3 or 5: 0
    
#======================OR=========================


def sum_of_3_5_divisible_number(input_list):
    sum_of_number_divisibleby_3or5 = 0
    for num in input_list:
        if num % 3 == 0 or num % 5 == 0:
            sum_of_number_divisibleby_3or5 += num
    return sum_of_number_divisibleby_3or5

try:
    user_input = input("Enter numbers separated by comma or space: ")
    user_list = [float(x) for x in user_input.replace(",", " ").split()]
    result = sum_of_3_5_divisible_number(user_list)
    print("Sum of numbers divisible by 3 or 5:", result)
except ValueError:
    print("Please enter valid numbers separated by comma or space.")
except Exception as e:
    print("An error occurred:", e)


