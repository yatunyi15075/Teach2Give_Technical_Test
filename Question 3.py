"""
Question 3: Power of Two
Write a program that takes an integer as input and returns true if the input is a power of two.
Examples:
8=> returns true
6=> returns false
"""

def is_power_of_two(num):
    if num <= 0:  # Zero and negative numbers are not powers of two
        return False
    elif num & (num - 1) == 0:  # Using bitwise AND operation to check if it's a power of two
        return True
    else:
        return False

# Test cases
print(is_power_of_two(8))  # Output: True
print(is_power_of_two(6))  # Output: False

