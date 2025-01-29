## System Specifications
- CPU: Intel Core i5-11400H @ 2.70GHz
- RAM: 8 GB DDR4  

2.Argument for Selection Sorting's Correctness
- We employ mathematical induction and loop invariants to demonstrate the correctness of Selection Sort.

1. Comprehending Selection Sort 
- Choosing In order to sort, the smallest element from the unsorted portion is repeatedly chosen and positioned correctly in the sorted portion. Two portions of the array are preserved by the algorithm: 
A section that is sorted (left side). 
The right side is an unsorted section. 
The leftmost unsorted element is switched out for the smallest element from the unsorted section at each stage.

2. Selection Sort Loop Invariant 
A condition that holds true both before and after a loop iteration is referred to as a loop invariant. 
Invariant Loop: 
At the start  
The smallest i elements in the array are arranged in the first i elements of the array in the 𝑖𝑡h iteration of the outer loop.

3. Proof by Induction
Using mathematical induction on the number of iterations, we demonstrate that Selection Sort is correct.
Base Situation (Initialization) 
Since the sorted part is empty at the beginning (i=0), the invariant is trivially satisfied. 

The Inductive Step 
Suppose that at iteration I's start,  at the first 
The smallest elements are among the sorted i elements. 
The element at index i is swapped out for the smallest element in the remaining unsorted section in the ith iteration. 
After iteration I, the sorted portion still contains the smallest i+1 elements because we always choose the smallest element that is available. 
This loop invariant, by induction, holds for all i, guaranteeing that the entire array is sorted at the conclusion of the algorithm.

4. Correctness and Termination
When every element is in its proper place and the array as a whole is sorted, Selection Sort comes to an end. Selection Sort successfully sorts the array, as seen by the accuracy that results from the loop invariant.

5. Final Thought
The reason Selection Sort is accurate is
At each stage, the smallest element is chosen methodically.
The loop invariant guarantees that the sorted section always contains the smallest elements in the correct order.
Upon termination, mathematical induction demonstrates that the full array is sorted.
Selection Sort thus appropriately sorts an input array in accordance with its specifications.

3.Benchmarking sorting algorithms
![WhatsApp Image 2025-01-28 at 22 08 23_dea9ad90](https://github.com/user-attachments/assets/84207424-b0d9-47e8-8cea-cf1d67a73331)
