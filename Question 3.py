"""
Question 3: Power of Two
Write a program that takes an integer as input and returns true if the input is a power of two.
Examples:
8=> returns true
6=> returns false
"""

def is_power_of_two(num):
    if num <= 0: 
        return False
    elif num & (num - 1) == 0: 
        return True
    else:
        return False

print(is_power_of_two(8)) 
print(is_power_of_two(6))

