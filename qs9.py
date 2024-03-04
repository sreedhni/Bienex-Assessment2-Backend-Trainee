# 9. Write a Python function that takes a list of integers as input and returns a 
# new list with only the numbers that are perfect squares. 
def perfect_squares(input_list):
    return [num for num in input_list if (num >= 0) and (int(num ** 0.5) ** 2 == num)]

try:
    input_numbers = input("Enter numbers separated by spaces: ")
    input_list = [int(x) for x in input_numbers.split()]
    result = perfect_squares(input_list)
    print("Perfect squares in the list:", result)
except ValueError:
    print("Please enter valid integers separated by spaces.")
except Exception as e:
    print("An error occurred:", e)

#===========================OUTPUT===================
# Enter numbers separated by spaces: 1 3 6 9 16 -9
# Perfect squares in the list: [1, 9, 16]




#===================================OR=========================================






def is_perfect_square(n):
    if n < 0:
        return False
    sqrt_n = int(n ** 0.5)
    return sqrt_n * sqrt_n == n

def perfect_squares(input_list):
    square_list = []
    for num in input_list:
        if is_perfect_square(num):
            square_list.append(num)
    return square_list

try:
    input_numbers = input("Enter numbers separated by spaces: ")
    input_list = [int(x) for x in input_numbers.split()]
    result = perfect_squares(input_list)
    print("Perfect squares in the list:", result)
except ValueError:
    print("Please enter valid integers separated by spaces.")
except Exception as e:
    print("An error occurred:", e)
