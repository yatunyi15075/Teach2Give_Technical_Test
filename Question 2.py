"""
Question 2: Fibonacci Sequence
Write a program to generate the Fibonacci sequence up to 100.
"""

def generate_fibonacci(limit):
    fib_sequence = [0, 1]  # Initial sequence: 0 and 1

    while fib_sequence[-1] + fib_sequence[-2] <= limit:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence

# Generate Fibonacci sequence up to 100
fibonacci_sequence = generate_fibonacci(100)

# Print the Fibonacci sequence
print("Fibonacci sequence up to 100:")
print(fibonacci_sequence)
