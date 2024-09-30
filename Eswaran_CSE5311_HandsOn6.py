import time
import random
import numpy as np
import matplotlib.pyplot as plt
import sys

# QuickSort with a fixed pivot (iterative version to avoid recursion depth issues)
def quicksort_iterative(arr):
    stack = [(0, len(arr) - 1)]
    
    while stack:
        left, right = stack.pop()
        if left < right:
            pivot = arr[right]
            i = left - 1
            for j in range(left, right):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[right] = arr[right], arr[i + 1]
            pivot_index = i + 1
            
            stack.append((left, pivot_index - 1))  # Left side
            stack.append((pivot_index + 1, right))  # Right side
    return arr

# QuickSort with a random pivot (recursive version)
def quicksort_random(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        arr.remove(pivot)
        left = [x for x in arr if x <= pivot]
        right = [x for x in arr if x > pivot]
        return quicksort_random(left) + [pivot] + quicksort_random(right)

# Benchmarking function
def benchmark_quicksort():
    sizes = [100, 500, 1000, 2000, 5000, 10000]  # Array sizes to test
    best_times = []
    worst_times = []
    average_times = []
    
    for n in sizes:
        print(f"Running benchmarks for array size {n}...")
        
        # Best case: already sorted array
        best_case = list(range(n))
        start_time = time.time()
        quicksort_iterative(best_case)
        best_times.append(time.time() - start_time)
        
        # Worst case: reverse sorted array
        worst_case = list(range(n, 0, -1))
        start_time = time.time()
        quicksort_iterative(worst_case)
        worst_times.append(time.time() - start_time)
        
        # Average case: random array
        average_case = np.random.randint(0, 10000, size=n)
        start_time = time.time()
        quicksort_iterative(average_case)
        average_times.append(time.time() - start_time)
    
    # Plotting the results
    plt.plot(sizes, best_times, label='Best Case')
    plt.plot(sizes, worst_times, label='Worst Case')
    plt.plot(sizes, average_times, label='Average Case')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.title('Iterative QuickSort Performance (Non-Random Pivot)')
    plt.show()

# Call the benchmark function
benchmark_quicksort()
