# Using `@cached_property` from `functools`

## Introduction

The `functools` module in Python provides a useful decorator called `@cached_property`. It allows us to cache the computed value of a property, avoiding repeated expensive calculations.

## Problem Statement

Consider a scenario where we have a computed property that derives its value dynamically. Every time the property is accessed, the value gets recomputed. This can be inefficient when:

- The computation is expensive (e.g., involves complex calculations or database queries).
- The computed value does not change frequently.

### Example: Without Caching

Suppose we have a `Dataset` class that calculates the **standard deviation** of a given sequence of numbers.

```python
import statistics
from typing import Iterable

class Dataset:
    def __init__(self, sequence_of_numbers: Iterable[float]):
        self.data = tuple(sequence_of_numbers)

    @property
    def stdev(self):
        print('Calculating standard deviation...')
        return statistics.stdev(self.data)

def main():
    data = Dataset([1, 2, 3, 4, 5])
    print(data.stdev)  # Computation occurs
    print(data.stdev)  # Computation occurs again
    print(data.stdev)  # Computation occurs again

main()
```

### Output:

```
Calculating standard deviation...
1.58
Calculating standard deviation...
1.58
Calculating standard deviation...
1.58
```

Every time `data.stdev` is accessed, the standard deviation is recalculated, which is inefficient.

## Solution: Using `@cached_property`

To avoid unnecessary recomputation, we can use `@cached_property`, which **computes the property once and caches the result** for future accesses.

```python
import statistics
from functools import cached_property
from typing import Iterable

class Dataset:
    def __init__(self, sequence_of_numbers: Iterable[float]):
        self.data = tuple(sequence_of_numbers)

    @cached_property
    def stdev(self):
        print('Calculating standard deviation...')
        return statistics.stdev(self.data)

def main():
    data = Dataset([1, 2, 3, 4, 5])
    print(data.stdev)  # Computation occurs
    print(data.stdev)  # Uses cached value
    print(data.stdev)  # Uses cached value

main()
```

### Output:

```
Calculating standard deviation...
1.58
1.58
1.58
```

Now, `stdev` is computed only **once**, and subsequent accesses **reuse the cached result**.

## Why Use `@cached_property`?

1. **Performance Improvement**: Prevents redundant calculations.
2. **Works with Immutable Objects**: If using a frozen dataclass or immutable instance, caching avoids modifying object state.
3. **Simplifies Code**: No need to manually manage caching logic.

## Key Differences: `@property` vs `@cached_property`

| Feature           | `@property`                                     | `@cached_property`                                  |
| ----------------- | ----------------------------------------------- | --------------------------------------------------- |
| Computation       | Every access                                    | Computed once and cached                            |
| Performance       | Inefficient for expensive operations            | Optimized                                           |
| Storage of Result | Not stored, recalculated                        | Stored in instance dictionary                       |
| Example Use Case  | Dynamic computations (e.g., fetching live data) | Expensive calculations (e.g., ML models, API calls) |

## Summary

- Use `@cached_property` when a computed property is expensive and does not change.
- Avoid using it if the property depends on frequently changing data.
- It behaves like a normal property but caches its value after the first computation.

By using `@cached_property`, we can **optimize performance and improve code efficiency** in Python applications.
