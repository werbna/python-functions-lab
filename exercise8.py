# Exercise 8: Calculate Product of Numbers
#
# Write a function named `product` that takes an arbitrary number of numbers, multiplies them, and returns the product.
# Review your notes on *args for handling an arbitrary number of arguments.
#
# Examples:
# product(-1, 4) should return -4.
# product(2, 5, 5) should return 50.
#
# Define the function and call it with different sets of numbers to test.
def product(*args):
    result = 1
    for num in args:
        result *= num
    return result


print('Exercise 8:', product(2, 5, 5))
print('Exercise 8:', product(-1, 4))
