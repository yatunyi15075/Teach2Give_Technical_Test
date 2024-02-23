"""
Question 2: Fibonacci Sequence
Write a program to generate the Fibonacci sequence up to 100.
"""

def generate_fib_sequence(limit):
    sequence = [0, 1]

    while sequence[-1] + sequence[-2] <= limit:
        sequence.append(sequence[-1] + sequence[-2])

    return sequence

generated_fib_sequence = generate_fib_sequence(100)

print("Allthe fibonacci sequence up to 100: ")
print(generated_fib_sequence)

