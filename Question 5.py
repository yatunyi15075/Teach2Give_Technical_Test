"""
Question 5: Reverse Integer
Write a program that takes an integer as input and returns an integer with reversed digit
ordering.
Examples:
For input 500, the program should return 5.
For input -56, the program should return -65.
For input -90, the program should return -9.
For input 91, the program should return 19.

"""

def reverse_integer(num):
    if num == 0:
        return 0

    # Convert integer to string and handle sign separately
    sign = -1 if num < 0 else 1
    num_str = str(abs(num))

    # Reverse the string and convert it back to integer
    reversed_str = num_str[::-1]
    reversed_num = int(reversed_str) * sign

    return reversed_num

# Test cases
print(reverse_integer(500))   # Output: 5
print(reverse_integer(-56))   # Output: -65
print(reverse_integer(-90))   # Output: -9
print(reverse_integer(91))    # Output: 19

