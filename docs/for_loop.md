#### [Return Back](../python_for_testers.md)

# For Loop

The `for` loop in Python is used to iterate over a sequence (such as a list, tuple, string, or range) or any iterable object. It allows you to execute a block of code repeatedly for each item in the sequence.

## Basic Syntax

The basic syntax of the `for` loop is as follows:

```python
for item in sequence:
    # Execute this block of code for each item in the sequence
    statement(s)
```

### Example

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

## Iterating over a Range

You can use the `range()` function to generate a sequence of numbers to iterate over.

```python
for i in range(5):
    print(i)
```

## Using Enumerate

The `enumerate()` function can be used to iterate over a sequence along with its index.

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
```

## Using Zip

The `zip()` function can be used to iterate over multiple sequences simultaneously.

```python
fruits = ["apple", "banana", "cherry"]
prices = [1.0, 0.5, 1.5]

for fruit, price in zip(fruits, prices):
    print(f"{fruit}: ${price}")
```

## Nested For Loops

You can nest `for` loops within other `for`, `if`, or `while` blocks to handle more complex scenarios.

```python
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")
```

## Using Break and Continue

You can use `break` and `continue` statements within `for` loops to alter the flow of execution, similar to `while` loops.

## Iterating Over Dictionaries

You can iterate over dictionaries using the `items()` method to access both keys and values.

```python
person = {"name": "Alice", "age": 30, "city": "New York"}

for key, value in person.items():
    print(f"{key}: {value}")
```

## Key Points:

- The `for` loop is used to iterate over a sequence or any iterable object.
- It allows you to execute a block of code repeatedly for each item in the sequence.
- You can use `range()`, `enumerate()`, `zip()`, and other functions to generate sequences or iterate over multiple sequences simultaneously.
- `break` and `continue` statements can be used to alter the flow of execution within `for` loops.
- `for` loops are versatile and commonly used in Python for various tasks such as iterating over lists, tuples, strings, dictionaries, and other iterable objects.

Understanding how to use `for` loops effectively allows you to iterate over sequences and perform repetitive tasks efficiently in Python.
