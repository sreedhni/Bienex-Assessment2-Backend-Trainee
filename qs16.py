# 16. Count the total number of uppercase characters in a file in Python
def count_uppercase_letter(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            uppercase_count = sum(1 for char in file_content if char.isupper())
            return uppercase_count
    except FileNotFoundError:
        print("File not found.")
        return -1  

file_path = input("enter the path: ")
uppercase_count = count_uppercase_letter(file_path)
if uppercase_count != -1:
    print("Total number of uppercase characters:", uppercase_count)
