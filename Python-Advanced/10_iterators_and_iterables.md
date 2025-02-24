# Understanding Iterators in Python

## What is an Iterator?

An **iterator** is an object that allows iteration over a sequence of values. It follows the **iterator protocol**, which means it implements two special methods:

- `__iter__()`: Returns the iterator object itself.
- `__next__()`: Returns the next value in the sequence. If no more values are available, it raises a `StopIteration` exception.

## Iterators vs. Iterables

- An **iterable** is an object that provides an iterator when `iter()` is called on it.
- An **iterator** is an object that produces elements one by one using `next()`.

### Example:

```python
my_list = [1, 2, 3]
iterator = iter(my_list)  # Calling iter() on a list returns an iterator
print(next(iterator))  # Outputs: 1
print(next(iterator))  # Outputs: 2
print(next(iterator))  # Outputs: 3
print(next(iterator))  # Raises StopIteration
```

## Common Iterables in Python

The following built-in types are **iterables**, meaning they can provide an iterator:

- Lists
- Tuples
- Dictionaries
- Sets
- Strings

## Creating and Using an Iterator Manually

Instead of using `for` loops, you can manually get an iterator and traverse through its elements using `next()`:

```python
inventory = ["laptop", "book", "phone"]
iterator = iter(inventory)
print(next(iterator))  # Outputs: laptop
print(next(iterator))  # Outputs: book
print(next(iterator))  # Outputs: phone
print(next(iterator))  # Raises StopIteration
```

## Handling StopIteration Exception

Instead of manually calling `next()`, you can handle the `StopIteration` exception:

```python
iterator = iter(inventory)
while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break
```

## Using Iterators with For Loops

A `for` loop automatically:

1. Calls `iter()` on the iterable to get an iterator.
2. Calls `next()` repeatedly until `StopIteration` is raised.

```python
for item in inventory:
    print(item)
```

## Custom Iterators

You can create your own iterator by defining a class that implements the `__iter__()` and `__next__()` methods.

### Example:

```python
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

counter = CountDown(3)
for num in counter:
    print(num)
# Output:
# 3
# 2
# 1
```

## Using Sentinel Values with Iterators

You can use `iter()` with a **sentinel value** to indicate the end of iteration.

### Example: Reading a File Line-by-Line Until End

```python
with open("countries.txt") as file:
    for line in iter(file.readline, ""):
        print(line, end="")
```

Here, `iter(file.readline, "")` reads lines until an empty string is encountered, indicating the end of the file.

## Final Code Example

```python
from dataclasses import dataclass
import os

@dataclass
class Item:
    name: str
    weight: float

def main() -> None:
    inventory = [
        Item("laptop", 1.5),
        Item("book", 0.3),
        Item("phone", 0.5),
        Item("charger", 0.2),
        Item("headphone", 0.1),
        Item("mouse", 0.2),
    ]

    # Using for loop
    for item in inventory:
        print(item)

    # Reading a file using iter() with a sentinel value
    file_path = os.path.join(os.path.dirname(__file__), "countries.txt")
    if os.path.exists(file_path):
        with open(file_path) as file:
            for line in iter(file.readline, ""):
                print(line, end="")
    else:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    main()
```

## Summary

- Iterators implement `__iter__()` and `__next__()`.
- Iterables provide an iterator when `iter()` is called.
- `for` loops automatically use the iterator protocol.
- Custom iterators allow us to define controlled iteration behavior.
- `iter()` with a sentinel value helps handle streams of data efficiently.

This structured approach ensures a better understanding of iterators in Python!
