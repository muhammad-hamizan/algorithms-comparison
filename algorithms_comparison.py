"""
This script compares the performance of two algorithms: 'robin' and 'batman'.

- 'robin': Iterates over an array to find and sum the next greater element for each element.
- 'batman': Uses a stack-based approach to efficiently find the next greater element and sum them.
- The script measures the time performance of both algorithms on arrays of increasing size and plots the results.
"""

import timeit
import random
import matplotlib.pyplot as plt 

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

# Measure performance of both algorithms on increasing input sizes
x_size = []
y_robin = []
y_batman = []

for k in range(1, 100, 10):
    listr = [random.randint(1, 1000) for _ in range(k * 100)]
    listb = listr.copy()

    # Measure time for robin
    timer = timeit.timeit(lambda: robin(listr), number=10) / 10 
    # Measure time for batman
    timeb = timeit.timeit(lambda: batman(listr), number=10) / 10 

    print(f"Size: {k * 100}, Robin - Time: {timer}, Batman: {batman(listb)}, Time: {timeb}")

    x_size.append(k * 100)
    y_robin.append(timer)
    y_batman.append(timeb)

# Plot the performance comparison
plt.plot(x_size, y_robin, label="Robin", marker="o")
plt.plot(x_size, y_batman, label="Batman", marker="o")

plt.xlabel("Size")
plt.ylabel("Time")
plt.legend()
plt.show()
