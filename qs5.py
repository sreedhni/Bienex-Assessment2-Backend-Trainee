#5. Implement a program that reads a text file and counts the occurrences of each word, ignoring case sensitivity. 


import string

file_name = input("Enter the file name: ")
word_count = {}

try:
    with open(file_name, 'r') as opened_file:
        for line in opened_file:
            words = line.split()
            for word in words:
                word = word.strip().lower()
                word = word.translate(str.maketrans('', '', string.punctuation))  
                if word:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1

    for word, count in word_count.items():
        print(f"{word} repeats: {count} times")

except FileNotFoundError:
    print("File not found. Please enter a valid file name.")
except Exception as e:
    print("An error occurred:", e)

#=====================OUTPUT=====================
# Enter the file name: C:\Users\user\OneDrive\Desktop\bienex\day16\Assessment\m.txt
# hello repeats: 2 times
# good repeats: 2 times
# afternoon repeats: 1 times
# vibe repeats: 1 times