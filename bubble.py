import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    while True:
        try:
            array_size = int(input("Enter the size of the array: "))
            if array_size <= 0:
                raise ValueError("Array size must be a positive integer.")
            break
        except ValueError as e:
            print("Invalid input. Please enter a positive integer.")

    if array_size <= 25:
        array = []
        print("Enter the elements of the array:")
        for i in range(array_size):
            while True:
                try:
                    element = int(input(f"Element {i + 1}: "))
                    array.append(element)
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")
    else:
        array = [random.randint(0, 100) for _ in range(array_size)]

    print("Original Array:", array)

    start_time = time.time()
    sorted_bubble = bubble_sort(array.copy())
    end_time = time.time()
    bubble_time = end_time - start_time
    print("Sorted Array (Bubble Sort):", sorted_bubble)
    print(f"Execution Time for Bubble Sort: {bubble_time:.6f} seconds")
