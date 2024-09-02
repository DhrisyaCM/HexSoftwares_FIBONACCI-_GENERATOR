Fibonacci Sequence Generator
This script generates the Fibonacci sequence up to the specified number of terms.

Description
The script defines a function fibonacci(n) that generates the Fibonacci sequence up to the nth term. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.

How It Works
The function takes an integer n as input, representing the number of terms to generate.
It returns a list containing the Fibonacci sequence up to the nth term.
If n is less than or equal to 0, an empty list is returned.
For n = 1, it returns [0].
For n = 2, it returns [0, 1].
For values greater than 2, the function computes the sequence iteratively.
Example Usage
python
Copy code
# Number of terms to generate
num_terms = 10

# Generate the Fibonacci sequence
fibonacci_sequence = fibonacci(num_terms)

# Print the sequence
print(fibonacci_sequence)
Output
csharp
Copy code
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
Requirements
Python 3.x
