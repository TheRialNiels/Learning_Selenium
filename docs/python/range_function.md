#### [Return Back](../../python_for_testers.md)

# Range Function

The `range()` function in Python is used to generate a sequence of numbers. It's commonly used in `for` loops to iterate over a sequence of numbers. The `range()` function can take one, two, or three arguments:

1. `range(stop)`: Generates numbers from 0 up to (but not including) the specified `stop` value.
2. `range(start, stop)`: Generates numbers from the specified `start` value up to (but not including) the specified `stop` value.
3. `range(start, stop, step)`: Generates numbers from the specified `start` value up to (but not including) the specified `stop` value, with the specified `step` value between each number.

## Basic Syntax

The basic syntax of the `range()` function is as follows:

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

### Examples:

```python
# Example 1: range(stop)
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

# Example 2: range(start, stop)
for i in range(2, 5):
    print(i)  # Output: 2, 3, 4

# Example 3: range(start, stop, step)
for i in range(0, 10, 2):
    print(i)  # Output: 0, 2, 4, 6, 8
```

## Key Points:

- The `range()` function generates a sequence of numbers.
- It is commonly used with `for` loops to iterate over a sequence of numbers.
- By default, `range()` starts from 0 and increments by 1, but you can specify the starting value and the step size.
- The `stop` value is exclusive, meaning it generates numbers up to, but not including, the `stop` value.
- If the `start` value is not specified, it defaults to 0.
- If the `step` value is not specified, it defaults to 1.

Understanding how to use the `range()` function allows you to generate sequences of numbers efficiently, especially when working with loops and iterating over a specific range of values.
