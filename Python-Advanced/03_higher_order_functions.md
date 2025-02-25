# Understanding Functions and Higher-Order Functions in Python

## Introduction

In this lesson, we will explore functions in Python and some of their powerful capabilities. Similar to our previous discussion on classes, functions in Python are objects, and they can be manipulated in various ways. This includes passing functions as arguments, returning functions, and using lambda functions.

## Functions as Objects

In Python, everything is an object—including functions. Functions are of type `callable`, meaning they can be invoked just like regular methods or objects with a `__call__` method. This allows for advanced functionalities such as passing functions to other functions or even returning functions as results.

## Basic Function Example

Let's start with a simple example where we define a `Customer` class and a function `send_email_promotion`, which iterates over a list of customers and determines their eligibility for a promotion based on their age.

### Code Example:

```python
from dataclasses import dataclass

@dataclass
class Customer:
    name: str
    age: int

def send_email_promotion(customers: list[Customer]):
    for customer in customers:
        print(f"checking {customer.name}")
        if customer.age < 50:
            print(f"{customer.name} is eligible for promotion")
        else:
            print(f"{customer.name} is not eligible for promotion")

def main() -> None:
    customers = [
        Customer("Alice", 34),
        Customer("Bob", 55),
        Customer("Charlie", 45),
        Customer("David", 60),
        Customer("Eve", 25),
        Customer("Frank", 40)
    ]
    send_email_promotion(customers)

if __name__ == "__main__":
    main()
```

### Explanation:

- We define a `Customer` class with attributes `name` and `age`.
- The function `send_email_promotion` loops through a list of customers and checks if their age is below 50 to determine eligibility.
- The `main` function creates a list of customers and calls `send_email_promotion`.

## Higher-Order Functions

A **higher-order function** is a function that takes another function as an argument or returns a function as a result. This allows us to decouple logic and make our code more flexible.

### Refactoring Using Higher-Order Functions

Instead of hardcoding the age check inside `send_email_promotion`, we can pass an external function that determines eligibility.

### Code Example:

```python
from dataclasses import dataclass
from typing import Callable, List

@dataclass
class Customer:
    name: str
    age: int

def send_email_promotion(customers: List[Customer], is_eligible: Callable[[Customer], bool]):
    for customer in customers:
        print(f"checking {customer.name}")
        if is_eligible(customer):
            print(f"{customer.name} is eligible for promotion")
        else:
            print(f"{customer.name} is not eligible for promotion")

def is_eligible_for_promotion(customer: Customer) -> bool:
    return customer.age > 50

def main() -> None:
    customers = [
        Customer("Alice", 34),
        Customer("Bob", 55),
        Customer("Charlie", 45),
        Customer("David", 60),
        Customer("Eve", 25),
        Customer("Frank", 40)
    ]
    send_email_promotion(customers, is_eligible_for_promotion)

if __name__ == "__main__":
    main()
```

### Explanation:

- The `send_email_promotion` function now accepts an additional argument, `is_eligible`, which is a function that determines if a customer qualifies for a promotion.
- Instead of directly checking the age inside the function, we call `is_eligible(customer)`, making the function more modular and reusable.
- We define `is_eligible_for_promotion`, which takes a `Customer` object and returns `True` if their age is above 50.

## Using Lambda Functions

Instead of defining a separate function like `is_eligible_for_promotion`, we can use a **lambda function**—an anonymous function defined inline.

### Code Example:

```python
def main() -> None:
    customers = [
        Customer("Alice", 34),
        Customer("Bob", 55),
        Customer("Charlie", 45),
        Customer("David", 60),
        Customer("Eve", 25),
        Customer("Frank", 40)
    ]
    send_email_promotion(customers, lambda c: c.age > 50)

if __name__ == "__main__":
    main()
```

### Explanation:

- Instead of passing `is_eligible_for_promotion`, we use `lambda c: c.age > 50`, which is an inline function that returns `True` if `age > 50`.
- This makes the code more concise and allows for quick modifications (e.g., changing the age condition dynamically).

## Benefits of Higher-Order Functions

1. **Improved Code Reusability** – The `send_email_promotion` function can now work with different eligibility criteria.
2. **More Readable & Maintainable** – Separating logic makes the code more readable and modular.
3. **Dynamic Behavior** – We can easily change the eligibility condition without modifying `send_email_promotion`.

## Conclusion

By treating functions as objects, Python allows for more flexible and powerful programming paradigms. Using **higher-order functions** and **lambda expressions**, we can write modular and reusable code that adapts to different conditions dynamically.

---
