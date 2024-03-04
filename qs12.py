# 12. Write a function that takes a sentence as input and returns a new sentence  with the words reversed, while keeping the order of the
# words in the sentence. 

def sentence_reverse(sentence):
    if not sentence:
        raise ValueError("Input sentence is empty")
    words = sentence.replace('.', ' ').replace(',', ' ').split()
    reversed_words = [word[::-1] for word in words]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

try:
    input_sentence = input("Enter the sentence: ")
    result = sentence_reverse(input_sentence)
    print("Reversed sentence:", result)
except ValueError as ve:
    print("Error:", ve)
except Exception as e:
    print("An unexpected error occurred:", e)

#=====================OUTPUT===============
# Enter the sentence: hello,what are you doing.
# Reversed sentence: olleh tahw era uoy gniod