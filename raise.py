# Define a function to calculate the factorial of a non-negative integer
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Test the function
try:
    print("Factorial of 5 is:", factorial(5))
    print("Factorial of -2 is:", factorial(-2))  # This will raise an exception
    print("Factorial of 0 is:", factorial(0))
except ValueError as e:
    print("Error:", e)
