"""
Question 6: Count Vowels
Write a program that counts the number of vowels in a sentence.
eg " Hello World " => returns 2
"""

def count_the_vowels(sentence):
    count = 0
    vowels = "aeiouAEIOU"
    
    for letter in sentence:
        if letter in vowels:
            count += 1
            
    return count

try:
    the_input_sentence = input("Enter a sentence: ")
    print(count_the_vowels(the_input_sentence))
except Exception as e:
    print("An error occurred:", e)
