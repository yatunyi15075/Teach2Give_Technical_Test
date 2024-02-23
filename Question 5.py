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

def reverse_int(n):
    if n == 0:
        return 0

    sign = -1 if n < 0 else 1
    num_str = str(abs(n))

    the_reversed_str = num_str[::-1]
    the_reversed_num = int(reversed_str) * sign

    return the_reversed_num

print(reverse_int(500)) 
print(reverse_int(-56)) 
print(reverse_int(-90)) 
print(reverse_int(91))   

