import random
import time

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
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
    sorted_selection = selection_sort(array.copy())
    end_time = time.time()
    selection_time = end_time - start_time
    print("Sorted Array (Selection Sort):", sorted_selection)
    print(f"Execution Time for Selection Sort: {selection_time:.6f} seconds")
