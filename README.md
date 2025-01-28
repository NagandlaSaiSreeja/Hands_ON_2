## System Specifications
- CPU: Intel Core i5-11400H @ 2.70GHz
- RAM: 8 GB DDR4  

---

## Insertion Sort Implementation

### How It Works
1. **Overview of Insertion Sort:**
   - Insertion Sort progressively builds a sorted section of the array. For each element, it finds the correct position by comparing it with already sorted elements.
   - Larger elements are shifted to the right, creating space for the current element.
   - This process repeats until all elements are sorted.

2. User Input:
   - Users provide the array size.
   - Random numbers (0–100) are generated for sorting.

3. Sorting Steps:
   - Starting from the second element, compare it with elements in the sorted section.
   - Shift larger elements to the right.
   - Place the current element in its correct position.
   - Repeat until the array is fully sorted.

### Example Execution
#### Input:
```
Enter the size of array: 12
```

#### Original Array:
```
[13, 34, 39, 42, 37, 37, 97, 33, 84, 17, 73, 47]
```

#### Iterations:
1. Place `34` in the correct position: `[13, 34, 39, 42, 37, 37, 97, 33, 84, 17, 73, 47]`
2. Place `39` in the correct position: `[13, 34, 39, 42, 37, 37, 97, 33, 84, 17, 73, 47]`
3. Place `42` in the correct position: `[13, 34, 39, 42, 37, 37, 97, 33, 84, 17, 73, 47]`
4. Place `37` in the correct position: `[13, 34, 37, 39, 42, 37, 97, 33, 84, 17, 73, 47]`
5. Place `37` in the correct position: `[13, 34, 37, 37, 39, 42, 97, 33, 84, 17, 73, 47]`
6. Place `97` in the correct position: `[13, 34, 37, 37, 39, 42, 97, 33, 84, 17, 73, 47]`
7. Place `33` in the correct position: `[13, 33, 34, 37, 37, 39, 42, 97, 84, 17, 73, 47]`
8. Place `84` in the correct position: `[13, 33, 34, 37, 37, 39, 42, 84, 97, 17, 73, 47]`
9. Place `17` in the correct position: `[13, 17, 33, 34, 37, 37, 39, 42, 84, 97, 73, 47]`
10. Place `73` in the correct position: `[13, 17, 33, 34, 37, 37, 39, 42, 73, 84, 97, 47]`
11. Place `47` in the correct position: `[13, 17, 33, 34, 37, 37, 39, 42, 47, 73, 84, 97]`

#### Final Sorted Array:
```
[13, 17, 33, 34, 37, 37, 39, 42, 47, 73, 84, 97]
```

---

## Selection Sort Implementation

### How It Works
1. Overview of Selection Sort
   - Selection Sort scans the unsorted portion of the array to find the smallest element.
   - The smallest element is swapped with the leftmost unsorted element, gradually expanding the sorted portion of the array.
   - This process repeats until the entire array is sorted.

2. User Input:
   - Users specify the size of the array.
   - The program generates random integers (0–100) to populate the array.

3. Sorting Steps:
   - For each position in the array:
     - Identify the smallest element in the unsorted portion.
     - Swap it with the current position.
     - Repeat until all elements are sorted.

### Example Execution
#### Input:
```
Enter the size of array: 12
```

#### Original Array:
```
[29, 10, 14, 37, 13, 45, 56, 24, 12, 5, 8, 30]
```

#### Iterations:
1. Place `5` in the correct position: `[5, 10, 14, 37, 13, 45, 56, 24, 12, 29, 8, 30]`
2. Place `8` in the correct position: `[5, 8, 14, 37, 13, 45, 56, 24, 12, 29, 10, 30]`
3. Place `10` in the correct position: `[5, 8, 10, 37, 13, 45, 56, 24, 12, 29, 14, 30]`
4. Place `12` in the correct position: `[5, 8, 10, 12, 13, 45, 56, 24, 37, 29, 14, 30]`
5. Place `13` in the correct position: `[5, 8, 10, 12, 13, 45, 56, 24, 37, 29, 14, 30]`
6. Place `14` in the correct position: `[5, 8, 10, 12, 13, 14, 56, 24, 37, 29, 45, 30]`
7. Place `24` in the correct position: `[5, 8, 10, 12, 13, 14, 24, 56, 37, 29, 45, 30]`
8. Place `29` in the correct position: `[5, 8, 10, 12, 13, 14, 24, 29, 37, 56, 45, 30]`
9. Place `30` in the correct position: `[5, 8, 10, 12, 13, 14, 24, 29, 30, 56, 45, 37]`
10. Place `37` in the correct position: `[5, 8, 10, 12, 13, 14, 24, 29, 30, 37, 45, 56]`
11. Place `45` in the correct position: `[5, 8, 10, 12, 13, 14, 24, 29, 30, 37, 45, 56]`

#### Final Sorted Array:
```
[5, 8, 10, 12, 13, 14, 24, 29, 30, 37, 45, 56]
```

---

## Bubble Sort Implementation

### How It Works
1. Overview of Bubble Sort:
   - Bubble Sort compares adjacent elements and swaps them if they are in the wrong order.
   - Larger elements "bubble up" to their correct positions with each pass, reducing the unsorted portion of the array.
   - This process continues until no swaps are needed, and the array is fully sorted.

2. User Input
   - Users provide the desired array size.
   - The program generates random integers (0–100) for sorting.

3. Sorting Steps:
   - Compare adjacent elements in the array.
   - Swap them if necessary to place them in order.
   - Repeat until the largest unsorted element is moved to the end.
   - Continue until the entire array is sorted.

### Example Execution
#### Input:
```
Enter the size of array: 12
```

#### Original Array:
```
[34, 12, 25, 9, 78, 45, 56, 33, 15, 10, 50, 5]
```

#### Iterations:
1. Push `78` to the end: `[12, 25, 9, 34, 45, 56, 33, 15, 10, 50, 5, 78]`
2. Push `56` to its position: `[12, 9, 25, 34, 33, 45, 15, 10, 50, 5, 56, 78]`
3. Push `50` to its position: `[9, 12, 25, 33, 34, 15, 10, 45, 5, 50, 56, 78]`
4. Push `45` to its position: `[9, 12, 25, 33, 15, 10, 5, 34, 45, 50, 56, 78]`
5. Push `34` to its position: `[9, 12, 25, 15, 10, 5, 33, 34, 45, 50, 56, 78]`
6. Repeat until sorted.

#### Final Sorted Array:
```
[5, 9, 10, 12, 15, 25, 33, 34, 45, 50, 56, 78]
```

---

## Comparison of Sorting Algorithms

### Insertion Sort
- **Best for small datasets** or arrays that are partially sorted.
- Efficient due to minimal swaps.

### Selection Sort
- Finds the smallest element in the unsorted portion and places it in the correct position.
- Performs fewer swaps but more comparisons than Insertion Sort.


### Bubble Sort
- Repeatedly compares adjacent elements and swaps them if necessary.
- Slower than both Insertion and Selection Sort due to frequent swaps.


---

## Conclusion
For practical purposes, insertion Sort is the most efficient of the three for small or nearly sorted datasets. Selection Sort is predictable but less efficient due to its inability to leverage partially sorted data. Bubble Sort, though simple and educational, is the least efficient and is rarely used in real-world applications. For larger datasets, consider advanced algorithms like Merge Sort or Quick Sort for better performance and scalability.

