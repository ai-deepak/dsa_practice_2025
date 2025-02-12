# Understanding Partial Function Application in Python

## Introduction

Partial function application is a powerful concept that allows you to fix certain arguments of a function, producing a new function with a modified signature. This is particularly useful in cases where you want to adapt functions for use in different contexts while keeping your code clean and modular.

## Problem Statement

Consider a scenario where we need to determine whether customers are eligible for a promotion based on their age. The eligibility criteria should be adjustable. Initially, our function has a hardcoded cutoff age, limiting its flexibility. We need a way to allow dynamic cutoff values while ensuring compatibility with other functions.

## Initial Implementation

We have a function `is_eligible_for_promotion` that determines whether a customer qualifies for a promotion.

```python
from dataclasses import dataclass
from typing import Callable, List
import functools

@dataclass
class Customer:
    name: str
    age: int

def send_email_promotion(customers: List[Customer], is_eligible: Callable[[Customer], bool]):
    for customer in customers:
        print(f"Checking {customer.name}")
        if is_eligible(customer):
            print(f"{customer.name} is eligible for promotion")
        else:
            print(f"{customer.name} is not eligible for promotion")

def is_eligible_for_promotion(customer: Customer, cutoff_age: int = 50) -> bool:
    return customer.age > cutoff_age

def main() -> None:
    customers = [
        Customer("Alice", 34),
        Customer("Bob", 55),
        Customer("Charlie", 45),
        Customer("David", 61),
        Customer("Eve", 25),
        Customer("Frank", 40)
    ]
    send_email_promotion(customers, is_eligible_for_promotion)

if __name__ == "__main__":
    main()
```

## Issues with the Initial Approach

1. **Hardcoded cutoff age**: The function `is_eligible_for_promotion` has a default cutoff age, making it difficult to modify dynamically.
2. **Function signature mismatch**: The function `is_eligible_for_promotion` expects two arguments (`customer` and `cutoff_age`), but `send_email_promotion` expects a function that takes only one argument (`Customer`). Passing `is_eligible_for_promotion` directly causes an argument mismatch.
3. **Limited reusability**: Without a way to preset values, every function call requires explicitly passing `cutoff_age`.

## Solution: Partial Function Application

Python's `functools.partial` provides an elegant solution by allowing us to fix certain arguments of a function, returning a new function with a modified signature.

```python
from dataclasses import dataclass
from typing import Callable, List
import functools

@dataclass
class Customer:
    name: str
    age: int

def send_email_promotion(customers: List[Customer], is_eligible: Callable[[Customer], bool]):
    for customer in customers:
        print(f"Checking {customer.name}")
        if is_eligible(customer):
            print(f"{customer.name} is eligible for promotion")
        else:
            print(f"{customer.name} is not eligible for promotion")

def is_eligible_for_promotion(customer: Customer, cutoff_age: int) -> bool:
    return customer.age > cutoff_age

def main() -> None:
    customers = [
        Customer("Alice", 34),
        Customer("Bob", 55),
        Customer("Charlie", 45),
        Customer("David", 61),
        Customer("Eve", 25),
        Customer("Frank", 40)
    ]
    is_eligible_60 = functools.partial(is_eligible_for_promotion, cutoff_age=60)
    send_email_promotion(customers, is_eligible_60)

if __name__ == "__main__":
    main()
```

### How `functools.partial` Works

`functools.partial` creates a new function where specific arguments of the original function are pre-applied.

**Syntax:**

```python
functools.partial(function, arg1, arg2, ...)
```

**Example Usage:**

```python
is_eligible_60 = functools.partial(is_eligible_for_promotion, cutoff_age=60)
```

Here, we create a new function `is_eligible_60`, which behaves like `is_eligible_for_promotion`, but with `cutoff_age` fixed at `60`.

## Key Benefits of `functools.partial`

1. **Enhances reusability**: Functions can be pre-configured and reused in different contexts.
2. **Ensures compatibility**: The transformed function maintains the expected signature for `send_email_promotion`.
3. **Improves readability**: Code remains concise, avoiding repeated argument passing.

## Expected Output

When running the script, the output will show customers over the age of 60 being eligible for promotion:

```
Checking Alice
Alice is not eligible for promotion
Checking Bob
Bob is not eligible for promotion
Checking Charlie
Charlie is not eligible for promotion
Checking David
David is eligible for promotion
Checking Eve
Eve is not eligible for promotion
Checking Frank
Frank is not eligible for promotion
```

## Conclusion

Partial function application is a useful technique for improving function flexibility while maintaining clear and modular code. By using `functools.partial`, we can effectively preset function arguments, making them adaptable for various use cases without changing the function's definition.

---

By structuring the code and explanation, we ensure clarity and correctness while demonstrating the concept with a practical example.
