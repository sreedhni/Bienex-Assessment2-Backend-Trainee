# 25. Quiz Game in Python
import random

class Question:
    def __init__(self, prompt, options, correct_answer):
        self.prompt = prompt
        self.options = options
        self.correct_answer = correct_answer

    def display_question(self):
        print(self.prompt)
        for i, option in enumerate(self.options):
            print(f"{i+1}. {option}")
        print()

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer

    def get_correct_option(self):
        return self.options[self.correct_answer - 1]

def run_quiz(questions):
    score = 0
    random.shuffle(questions)
    for question in questions:
        question.display_question()
        user_answer = get_user_input(len(question.options))
        if user_answer == 'quit':
            print(f"Quiz ended. You got {score} out of {len(questions)} questions correct.")
            return
        if question.check_answer(user_answer):
            score += 1
            print("Correct!\n")
        else:
            correct_option = question.get_correct_option()
            print(f"Your answer is wrong. The correct option is: {correct_option}\n")

    print(f"You got {score} out of {len(questions)} questions correct.")

def get_user_input(num_options):
    while True:
        user_input = input(f"Enter your answer (1-{num_options}), or type 'quit' to end: ").lower()
        if user_input == 'quit':
            return 'quit'
        try:
            user_answer = int(user_input)
            if 1 <= user_answer <= num_options:
                return user_answer
            else:
                print("Invalid input. Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def main():
    questions = [
        Question("What is the result of the following expression: 3 * 4 + 5?",
         ["20", "17", "27", "Error"], 2),
        Question("What will be the output of the following code?"
         "print('Hello, ' + 'world!')",
         ["Hello, world!", "Hello", "world!", "Error"], 1),
         Question("What is the result of 2 + 2?",
         ["3", "4", "5", "6"], 2),
         Question("What is the keyword used to define a function in Python?",
         ["def", "func", "define", "function"], 1),
         Question("What data type is used to store a sequence of characters in Python?",
         ["String", "Integer", "Boolean", "List"], 1),
         Question("Which of the following data types is mutable in Python?",
         ["int", "str", "list", "tuple"], 3),
        Question("What is the largest mammal?",
         ["Elephant", "Blue Whale", "Giraffe", "Hippo"], 2),
        Question("Which is the northernmost district of Kerala?",
         ["Kozhikode", "Kasaragod", "Wayanad", "Malappuram"], 2),
        Question("Which of the following animals is known for its ability to change its color to blend with its surroundings?",
         ["Lion", "Tiger", "Chameleon", "Giraffe"], 3),
         Question("Which bird is known for its ability to mimic human speech?",
         ["Parrot", "Eagle", "Sparrow", "Penguin"], 1),
         Question("Which bird is the national bird of India?",
         ["Peacock", "Sparrow", "Crow", "Pigeon"], 1),
         Question("Who is the current Prime Minister of India?",
         ["Narendra Modi", "Rahul Gandhi", "Manmohan Singh", "Amit Shah"], 1),
         Question("Which country was the first to implement a nationwide lockdown in response to the COVID-19 pandemic?",
         ["China", "Italy", "Spain", "India"], 1),
         Question("What is the name of the virus responsible for the COVID-19 pandemic?",
         ["SARS-CoV", "H1N1", "SARS-CoV-2", "Ebola"], 3),]

    run_quiz(questions)

if __name__ == "__main__":
    main()


#==========================OUTPUT===========================
    
# Who is the current Prime Minister of India?
# 1. Narendra Modi
# 2. Rahul Gandhi
# 3. Manmohan Singh
# 4. Amit Shah
    
# Enter your answer (1-4), or type 'quit' to end: 1
# Correct!

# Which of the following data types is mutable in Python?
# 1. int
# 2. str
# 3. list
# 4. tuple

# Enter your answer (1-4), or type 'quit' to end: 2
# Your answer is wrong. The correct option is: list

# What is the largest mammal?
# 1. Elephant
# 2. Blue Whale
# 3. Giraffe
# 4. Hippo

# Enter your answer (1-4), or type 'quit' to end: 2
# Correct!

# Which is the northernmost district of Kerala?
# 1. Kozhikode
# 2. Kasaragod
# 3. Wayanad
# 4. Malappuram

# Enter your answer (1-4), or type 'quit' to end: quit
# Quiz ended. You got 2 out of 14 questions correct.