"""
Chose recursion if:
1) If we can divide the problems into similar sub-problems
2) Design an alogorithm to compute nth...
3) Write code to list n...
4) Implement a method to compute all.
5) Trees and recursions

Recursions mostly used in:
Divide and Conquer
Greedy and Dynamic programming
"""
"""
Example-1
"""


def russian_doll(x):
    if x == 1:
        print(f"All dolls are open")
    else:
        print(x)
        # Calling itself if condition is not satisfied and this is called as recursion
        russian_doll(x - 1)


russian_doll(7)

"""
Example-2
"""


def recursive_method(n):
    if n < 1:
        print("n is less than 1...")
    else:
        print(n)
        recursive_method(n - 1)  # recursion


recursive_method(10)


