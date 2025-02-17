# Single Dispatch in Python

## Introduction

Single dispatch is a feature in Python that allows function overloading based on the type of the first argument. This is achieved using the `@singledispatch` decorator from the `functools` module. It enables the registration of different implementations of a function that handle different data types while maintaining a single function interface.

## Concept and Usage

### Basic Example

The core idea of single dispatch is to define a **generic function** and then **register** multiple specialized versions for different data types.

```python
from functools import singledispatch

@singledispatch
def add(x: int, y: int) -> int:
    return x + y
```

Here, `add` is a generic function that by default takes two integers and returns their sum.

### Registering Other Types

We can register other versions of the function for different data types.

#### String Concatenation with Space

```python
@add.register
def _(x: str, y: str) -> str:
    return f"{x} {y}"
```

This version of `add` concatenates two strings with a space in between.

#### Handling Lists and Sets

```python
@add.register
def _(x: list | set, y: list | set) -> list:
    return [*x, *y]
```

This version allows `add` to concatenate lists or sets into a single list.

#### Registering with Functional Form

Instead of using the decorator syntax, we can register a function using the `register()` method.

```python
add.register(tuple, lambda x, y: (*x, *y))
```

This registers a version of `add` that takes tuples and returns a concatenated tuple.

## Full Example

```python
from functools import singledispatch

@singledispatch
def add(x: int, y: int) -> int:
    return x + y

@add.register
def _(x: str, y: str) -> str:
    return f"{x} {y}"

@add.register
def _(x: list | set, y: list | set) -> list:
    return [*x, *y]

add.register(tuple, lambda x, y: (*x, *y))

def main() -> None:
    print(add(1, 2))           # Output: 3
    print(add("Hello", "World")) # Output: "Hello World"
    print(add([1, 2, 3], [4, 5, 6])) # Output: [1, 2, 3, 4, 5, 6]
    print(add({1, 2, 3}, {4, 5, 6})) # Output: [1, 2, 3, 4, 5, 6]
    print(add((1, 2, 3), (4, 5, 6))) # Output: (1, 2, 3, 4, 5, 6)

main()
```

## Explanation

- The `@singledispatch` decorator marks `add` as a generic function.
- The `@add.register` decorator registers alternative implementations for different data types.
- The `register()` method provides an alternative way to register functions.
- The main function tests the different cases and demonstrates the expected outputs.

## Advantages of Single Dispatch

- **Improves code organization** by allowing multiple implementations of a function under a single name.
- **Enhances readability** by keeping related logic in one place rather than using multiple `if-elif` checks.
- **Encourages type-specific behavior** without modifying the original function.

## When to Use Single Dispatch

Single dispatch is useful when you need to apply different operations based on the data type while keeping function names consistent. However, it may not be necessary for simple cases and should be used when it significantly improves code clarity.
