#4. Merge Multiple Text Files into One 

def merge_text_files(output_file, *input_files):
    try:
        with open(output_file, 'w') as output:
            for input_file in input_files:
                with open(input_file, 'r') as input:
                    output.write(input.read())
                    output.write('\n')
    except FileNotFoundError:
        print("One of the input files does not exist.")
    except PermissionError:
        print("Permission denied. Check if you have the necessary permissions to read/write files.")
    except Exception as e:
        print("An error occurred:", str(e))

input_files = []
output_file = input("Enter the output file name: ")
length = int(input("Total number of files wanted to merge: "))

for i in range(length):
    file_name_want_to_merge = input("Enter the file name: ")
    input_files.append(file_name_want_to_merge)

merge_text_files(output_file, *input_files)
print("Files merged successfully. Output saved to", output_file)
