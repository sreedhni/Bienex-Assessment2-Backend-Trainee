# 15. Copy odd lines of one file to another file in Python 
# Open the input and output files
# Open the input and output files
input_file = input("Enter the input file path: ")
output_file = input("Enter the output file path: ")

try:
    with open(input_file, 'r') as inputfile, open(output_file, 'w') as outputfile:
        lines = inputfile.readlines()
        
        for i, line in enumerate(lines):
            if i % 2 == 0:
                outputfile.write(line)
    print("Odd lines of one file are copied to another file in Python.")
except FileNotFoundError:
    print("File not found. Please check the file paths.")
except Exception as e:
    print("An error occurred:", e)
