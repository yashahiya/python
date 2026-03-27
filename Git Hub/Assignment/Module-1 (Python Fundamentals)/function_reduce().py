from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using reduce() to find product
product = reduce(lambda x, y: x * y, numbers)

# Print result
print("Product of list:", product)