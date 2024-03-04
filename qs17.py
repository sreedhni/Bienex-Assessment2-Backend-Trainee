# 17. Python program to delay printing of line from a file using sleep function 
import time

def print_lines_with_delay(file_path, delay):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line.rstrip())
                time.sleep(delay)
    except FileNotFoundError:
        print("File not found.")
file_path = input("Enter the file path: ")
delay = float(input("enter the delay "))
print_lines_with_delay(file_path, delay)

#========================OUTPUT=================================
# Enter the file path: C:\Users\user\OneDrive\Desktop\bienex\day16\Assessment\hy.txt
# enter the delay 1
# Beinex is a global firm with businesses in 5 continents specializing in Data, AI, and Digital Transformation.
# A pioneering enterprise, Beinex has established a powerful presence in the regions it serves by delivering comprehensive solutions to address diverse business challenges in the spheres of Advisory, Technology & Software Development, and Systems Integration. Beinex Consulting caters to a broad spectrum of industries and departments, offering tailored solutions to meet their specific requirements.

# there had a 1 sec delay for printing