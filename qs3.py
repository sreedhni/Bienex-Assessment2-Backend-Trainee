# 3. Search for a String in a Text File
file_name=input("enter the file name: ")
searching_string=input("enter the string:")
try:
    with open(file_name,'r') as opened_file:
        contents=opened_file.read()
        if searching_string in contents: #IT IS CASE SENSITIVE
            print(f"{searching_string} is present in the given text file {file_name}")
        else:
            print(f"{searching_string} is not present in the given text file {file_name}")
except FileNotFoundError:
    print("File not found or the file is not located in the specified directory.")
    exit()

    

