#2. Count the Number of Lines, Words, and Characters in a Text File 
    
file_name = input("Enter the file path:")  # C:\Users\user\OneDrive\Desktop\bienex\day16\Assessment\hy.txt
no_of_lines = 0
no_of_words = 0
no_of_characters = 0

try:
    with open(file_name, 'r') as open_file:
        text = open_file.read()
        if not text:
            print("It is an empty file.")
            exit()

        for line in text.split('\n'):
            no_of_lines += 1
            words = line.replace(',', ' ').replace('.', ' ').split()
            no_of_words += len(words)
            no_of_characters += len(line)
except FileNotFoundError:
    print("File not found or the file is not located in the specified directory.")
    exit()

print("Number of lines:", no_of_lines)
print("Number of words:", no_of_words)
print("Number of characters:", no_of_characters)


#===================================or===================
def count_lines_words_characters(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            if not text:
                print("It is an empty file.")
                return 0, 0, 0

            lines = text.count('\n') + 1  
            words_with_delimiters = [word.strip() for word in text.replace(',', ' ').replace('.', ' ').split()]
            words = len(words_with_delimiters)
            characters = len(text)         

        return lines, words, characters
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return 0, 0, 0
    except Exception as e:
        print("An error occurred:", str(e))
        return 0, 0, 0

filename = input("Enter the file path:") 
lines, words, characters = count_lines_words_characters(filename)
print("Number of lines:", lines)
print("Number of words:", words)
print("Number of characters:", characters)
#=============================OUTPUT============================
# Enter the file path:C:\Users\user\OneDrive\Desktop\bienex\day16\Assessment\hy.txt
# Number of lines: 2
# Number of words: 71
# Number of characters: 507
