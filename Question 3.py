"""
Question 3: Power of Two
Write a program that takes an integer as input and returns true if the input is a power of two.
Examples:
8=> returns true
6=> returns false
"""

def check_power_of_two(n):
    if n <= 0: 
        return False
    return n & (n - 1) == 0

try:
    number = int(input("Enter an integer: "))
    print(check_power_of_two(number))
except ValueError:
    print("Invalid input! Please enter an integer.")



