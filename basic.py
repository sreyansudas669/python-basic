# using true and false keyword wap weather  a function is a even or odd

# Function to check if a number is even
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Function to check if a number is odd
def is_odd(number):
    if number % 2 != 0:
        return True
    else:
        return False

# Function to check if a number is divisible by both 2 and 3
def is_divisible_by_2_and_3(number):
    if number % 2 == 0 and number % 3 == 0:
        return True
    else:
        return False

# Testing the functions
test_number = 11

print("Is", test_number, "even?", is_even(test_number))
print("Is", test_number, "odd?", is_odd(test_number))
print("Is", test_number, "divisible by both 2 and 3?", is_divisible_by_2_and_3(test_number))

