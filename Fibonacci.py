def fibonacci(n):
    """Generates the Fibonacci sequence up to the nth term.

    Args:
        n: The number of terms to generate.

    Returns:
        A list containing the Fibonacci sequence up to the nth term.
    """

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequence = [0, 1]
    for i in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)

    return sequence

# Example usage:
num_terms = 10
fibonacci_sequence = fibonacci(num_terms)
print(fibonacci_sequence)