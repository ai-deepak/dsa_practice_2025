# Difference Between My Solution and the Optimized Solution

## Key Differences

1. **Time Complexity in Practice**:

   - **Your Solution**:
     - Involves unnecessary **swaps** during the loop.
     - Swapping elements increases the constant factors of the \(O(n)\) complexity.
     - Modifies the array in-place, making it less efficient.
   - **Optimized Solution**:
     - Only compares values and updates a single variable.
     - Avoids the overhead of swaps, making it faster in practice despite having the same \(O(n)\) complexity.

2. **Algorithm Design**:
   - **Your Solution**:
     - Implements a partial **bubble sort**, which is unnecessary for finding the maximum value.
     - Bubble sort inherently modifies the array and performs additional operations.
   - **Optimized Solution**:
     - Uses a direct and efficient approach to find the largest value.
     - Does not modify the array.

## Complexity Analysis

|                      | Your Solution | Optimized Solution |
| -------------------- | ------------- | ------------------ |
| **Time Complexity**  | \(O(n)\)      | \(O(n)\)           |
| **Space Complexity** | \(O(1)\)      | \(O(1)\)           |

### Why Does Your Code Cause TLE?

- While both solutions have \(O(n)\) time complexity, your solution's **swaps** increase the constant factors of runtime.
- Platforms like GeeksforGeeks expect efficient solutions with minimal operations.

## Optimized Solution Code

```python
def largest(arr):
    max_value = arr[0]  # Assume the first element is the largest
    for num in arr:     # Iterate through the array
        if num > max_value:
            max_value = num  # Update the largest value
    return max_value
```
