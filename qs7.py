# 7. Write a function that takes a list of numbers as input and returns the second-largest number.  
def second_largest_number():
    try:
        user_input = input("Enter a list of numbers separated by spaces or comma : ")
        input_list = [float(x) for x in user_input.replace(',', ' ').split()]
        
        if not all(isinstance(x, (int, float)) for x in input_list):
            return "Invalid input. Please ensure that your list contains only numbers"
        
        if len(input_list) < 2:
            return "List should contain at least two numbers"
        
        max_num = max(input_list)
        input_list.remove(max_num)
        second_largest = max(input_list)
        return second_largest
    except ValueError:
        return "Invalid input. Please enter a list of valid number."

result = second_largest_number()
print(result)
#=========================OUTPUT==========
# Enter a list of numbers separated by spaces or comma : 2 4 6 7 90 15
# 15.0
# Enter a list of numbers separated by spaces or comma : 3
# List should contain at least two numbers