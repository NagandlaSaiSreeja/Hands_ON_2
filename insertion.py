import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
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
    sorted_insertion = insertion_sort(array.copy())
    end_time = time.time()
    insertion_time = end_time - start_time
    print("Sorted Array (Insertion Sort):", sorted_insertion)
    print(f"Execution Time for Insertion Sort: {insertion_time:.6f} seconds")
