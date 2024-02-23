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

def reverse_integer(n):
    if n == 0:
        return 0

    sign = -1 if n < 0 else 1
    num_str = str(abs(n))

    reversed_str = num_str[::-1]
    reversed_num = int(reversed_str) * sign

    return reversed_num

print(reverse_integer(500)) 
print(reverse_integer(-56)) 
print(reverse_integer(-90)) 
print(reverse_integer(91))   

