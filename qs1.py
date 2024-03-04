# 1. Read and Print the Contents of a Text File

file_name = input("Enter the file name to be opened:") #hy.txt

try:
    with open(file_name, 'r') as file_opened:
        contents = file_opened.read()
        if contents:
            print(contents)
        else:
            print("The file is empty.")
except FileNotFoundError:
    print("File not found or the file is not located in the specified directory.")

#========================OUTPUT===============
# Enter the file name to be opened:C:\Users\user\OneDrive\Desktop\bienex\day16\Assessment\hy.txt
# Beinex is a global firm with businesses in 5 continents specializing in Data, AI, and Digital Transformation.
# A pioneering enterprise, Beinex has established a powerful presence in the regions it serves by delivering comprehensive solutions to address diverse business challenges in the spheres of Advisory, Technology & Software Development, and Systems Integration. Beinex Consulting caters to a broad spectrum of industries and departments, offering tailored solutions to meet their specific requirements.
# PS C:\Users\user\OneDrive\Desktop\bienex\day16\Assessment> 