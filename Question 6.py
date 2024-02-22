"""
Question 6: Count Vowels
Write a program that counts the number of vowels in a sentence.
eg " Hello World " => returns 2
"""

def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in sentence:
        if char in vowels:
            vowel_count += 1

    return vowel_count

# Test case
print(count_vowels("Hello World"))  # Output: 3
