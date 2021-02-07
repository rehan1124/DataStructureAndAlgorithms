"""
Example: Factorial
"""


def factorial(n):
    assert (n >= 1) and (int(n) == n), "Number should be positive integer!"
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


print(factorial(-6))
