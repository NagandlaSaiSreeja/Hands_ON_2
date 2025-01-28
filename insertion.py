def insertion(array):
    for a in range(1, len(array)):
        key = array[a]
        j = a - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array
import random
import time
import matplotlib.pyplot as plt
if __name__ == "__main__":
    while True:
        try:
            arr_siz = int(input("Size of the array: "))
            if arr_siz <= 0:
                raise ValueError("Array size must be positive integer.")
            break
        except ValueError as e:
            print("Invalid input. Please enter a positive integer.")

    if arr_siz <= 25:
        array = []
        print("Enter element of the array:")
        for a in range(arr_siz):
            while True:
                try:
                    element = int(input(f"Element {a + 1}: "))
                    array.append(element)
                    break
                except Error:
                    print("Invalid input. Please enter an integer.")
    else:
        array = [random.randint(0, 100) for _ in range(arr_siz)]

    print("Original Array:", array)

    start_time = time.time()
    sorted_insertion = insertion(array.copy())
    end_time = time.time()
    ins_time = end_time - start_time
    print("Sorted Array (Insertion Sort):", sorted_insertion)
    print(f"Execution Time for this algo: {ins_time:.18f} seconds")

    array_sizes = []
    execution_times = []

    for size in range(1, arr_siz + 1):  
        if size <= 25:
            test_array = [random.randint(-100, 100) for _ in range(size)]
        else:
            test_array = [random.randint(0, 100) for _ in range(size)]
       
        start_time = time.time()
        insertion(test_array.copy())
        end_time = time.time()
        execution_times.append(end_time - start_time)
        array_sizes.append(size)  

    print(f"Insertion Sort Execution Time: {end_time - start_time:.12f} seconds")    
    plt.plot(array_sizes, execution_times)
    plt.xlabel("Array Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Insertion Sort: Execution Time vs. Array Size")
    plt.show()
