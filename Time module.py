# ---------------------------------Time Module-------------------------------

import time


# Recursive implementation (inefficient for large n)
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Memoization implementation (improved recursive version)
def fibonacci_memoization(n, memo={}):
    if n <= 1:
        return n

    if n not in memo:
        memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)

    return memo[n]


# Iterative implementation
def fibonacci_iterative(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


# Time measurement function
def measure_execution_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time


# Test the implementations and measure execution time
n = 30  # You can adjust the value of n

# Recursive
result_recursive, time_recursive = measure_execution_time(fibonacci_recursive, n)
print(f"Recursive Result: {result_recursive}, Time: {time_recursive:.6f} seconds")

# Memoization
result_memoization, time_memoization = measure_execution_time(fibonacci_memoization, n)
print(f"Memoization Result: {result_memoization}, Time: {time_memoization:.6f} seconds")

# Iterative
result_iterative, time_iterative = measure_execution_time(fibonacci_iterative, n)
print(f"Iterative Result: {result_iterative}, Time: {time_iterative:.6f} seconds")
