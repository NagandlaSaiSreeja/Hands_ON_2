import time
import random
import matplotlib.pyplot as plt

# 1. Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# 2. Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# 3. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Benchmarking Function
def benchmark_sorting_algorithms():
    input_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 5000, 10000]
    insertion_times = []
    selection_times = []
    bubble_times = []

    for size in input_sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]

        # Benchmark Insertion Sort
        start = time.time()
        insertion_sort(arr[:])  # Use a copy to avoid in-place sorting issues
        insertion_times.append(time.time() - start)

        # Benchmark Selection Sort
        start = time.time()
        selection_sort(arr[:])
        selection_times.append(time.time() - start)

        # Benchmark Bubble Sort
        start = time.time()
        bubble_sort(arr[:])
        bubble_times.append(time.time() - start)

    # Plot the Results
    plt.figure()
    plt.plot(input_sizes, insertion_times, label="Insertion Sort")
    plt.plot(input_sizes, selection_times, label="Selection Sort")
    plt.plot(input_sizes, bubble_times, label="Bubble Sort")
    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.title("Benchmark: Sorting Algorithms")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    benchmark_sorting_algorithms()
