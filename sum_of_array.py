"""
This script generates a list of 100 random integers between 1 and 100, then computes the sum of 
next greater elements using 'robin' and 'batman' algorithms for comparison.
"""

import random

# Robin algorithm: Finds the next greater element for each item in the array and sums those values.
def robin(a):
    total = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] < a[j]:
                total += a[j]
                break
    return total

# Batman algorithm: Uses a stack to efficiently find the next greater element for each item and sums them.
def batman(arr):
    n = len(arr)
    next_greater = [0] * n
    stack = []

    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            next_greater[idx] = arr[i]
        stack.append(i)

    return sum(next_greater) % 1000000001

# Generate a random list of 100 integers between 1 and 100
a = [random.randint(1, 100) for _ in range(100)]

# Print the generated array
for i, num in enumerate(a):
    print(f"Data Array ke-{i + 1}: {num}")

print()

# Calculate and print results using 'robin' and 'batman'
print("Hasil Solusi Robin: ", robin(a))
print("Hasil Solusi Batman: ", batman(a))
