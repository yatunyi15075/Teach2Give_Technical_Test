"""
Question 4: Capitalize Words
Write a program that accepts a string as input, capitalizes the first letter of each word in the
string, and then returns the result string.
Examples:
"hi"=> returns "Hi"
"i love programming"=> returns "I Love Programming"
"""

def capitalize_the_words(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

try:
    the_input_sentence = input("Enter a sentence: ")
    print(capitalize_the_words(the_input_sentence))
except Exception as e:
    print("An error has occurred:", e)
