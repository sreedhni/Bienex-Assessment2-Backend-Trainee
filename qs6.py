# 6. Write a Python function that takes a list of strings as input and returns a new list with the strings sorted in descending order of their
# lengths.  

def sort_strings_by_length_desc(strings):
    return sorted(strings, reverse=True, key=lambda s: len(s))
try:
    user_input = input("Enter a list of strings separated by spaces if you separate the string by comma it consider as a single word: ")
    input_list = user_input.split()
    if not input_list:
        raise ValueError("Empty input list. Please enter at least one string.")
    sorted_list = sort_strings_by_length_desc(input_list)
    print("Sorted list:", sorted_list)

except ValueError as ve:
    print("Error:", ve)
except Exception as e:
    print("An unexpected error occurred:", e)
#=====================================OUTPUT======================================
# Enter a list of strings separated by spaces if you separate the string by comma it consider as a single word: hello kakkanad kasargod kochi a ab abcdefghi
# Sorted list: ['abcdefghi', 'kakkanad', 'kasargod', 'hello', 'kochi', 'ab', 'a']