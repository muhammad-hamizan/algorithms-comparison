"""
This script generates a list of 20 random integers between 0 and 20 and prints them.
"""

import random

# Generate and print a random list of 20 integers between 0 and 20
a = [random.randint(0, 20) for _ in range(20)]

for num in a:
    print(num)
