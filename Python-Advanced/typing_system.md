## Type System

Type system can be classified into two types:

- **Static typing**
- **Dynamic typing**

Java is statically typed. Once you assign a variable as a string, you cannot assign an integer.

Python is dynamically typed. You can assign a string to a variable and later assign an integer to the same variable.

- The type is not associated with the variable.
- It is associated with the value.

Another way of looking at this is:

- **Nominal typing**
- **Structural typing**

Python is more of a structural type but not exactly. It is called **"Duck Typing"**.

---

### Duck Typing in Python

**Duck typing** is a programming concept in Python where the type or class of an object is less important than the methods and properties it defines. The name comes from the saying:

> "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."

In the context of Python, this means that you don’t check the type of an object explicitly. Instead, you check for the presence of certain methods or behaviors. If the object behaves as expected (implements the required methods or attributes), it is considered valid.

---

### Key Principles

1. **Behavior over Type**: Focus on what an object _can do_ rather than what type it is.
2. **Dynamic Typing**: Python allows dynamic typing, enabling duck typing to thrive. Objects are treated based on their runtime behavior rather than predefined types.

---

### Example of Duck Typing

```python
class Duck:
    def quack(self):
        print("Quack quack!")

    def swim(self):
        print("I can swim!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")

    def swim(self):
        print("I'm swimming!")

def interact_with_duck(duck_like):
    duck_like.quack()
    duck_like.swim()

# Both instances can be passed to the function
duck = Duck()
person = Person()

interact_with_duck(duck)    # Works because Duck has quack and swim
interact_with_duck(person)  # Works because Person has quack and swim
```

Here, the `interact_with_duck` function does not care whether it receives a `Duck` or a `Person`. As long as the object passed has the `quack` and `swim` methods, it will work.

---

### Advantages of Duck Typing

1. **Flexibility**: It allows you to write more generic and reusable code.
2. **Polymorphism**: Encourages polymorphism without requiring inheritance or implementing interfaces.
3. **Ease of Use**: Reduces boilerplate and makes the code more concise and Pythonic.

---

### Drawbacks of Duck Typing

1. **Runtime Errors**: Errors related to missing methods or attributes are discovered only at runtime, not during static analysis.
2. **Hard to Debug**: Debugging issues caused by incompatible objects can be challenging.
3. **Less Explicit**: The code might be harder to understand for those unfamiliar with duck typing.

---

### Example: Why Use Duck Typing?

#### Without Duck Typing

```python
def process_string(s: str):
    print(s.upper())

process_string("hello")  # Works
process_string(123)      # Error
```

#### With Duck Typing

```python
def process_string(s):
    print(s.upper())

class CustomString:
    def __init__(self, value):
        self.value = value

    def upper(self):
        return self.value.upper()

process_string("hello")                # Works
process_string(CustomString("hello"))  # Works, as CustomString defines upper()
```

In this example, you’re relying on the presence of the `upper` method rather than the type of the object, making the code more flexible.

---

### Summary

Duck typing leverages Python's dynamic nature to enable flexible, behavior-based programming. It’s a powerful concept when used appropriately but requires careful handling to avoid runtime errors and ensure maintainable code.
