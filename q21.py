#21. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range
def list_operation(lst, index):
    try:
        result = lst[index]
        return result
    except IndexError as e:
        print(f"Error: {e}")
        return None

my_list = ["beinex", 10, "hy", 90, 89]
user_index = int(input("Enter the index to perform the operation on: "))
result = list_operation(my_list, user_index)
if result is not None:
    print("Result:", result)
