#### [Return Back](../../python_for_testers.md)

# Zip Function

The `zip()` function in Python is used to combine multiple iterable objects (such as lists, tuples, or strings) into a single iterator of tuples. Each tuple contains the corresponding elements from all the input iterables. If the input iterables are of different lengths, `zip()` will stop when the shortest iterable is exhausted.

## Basic Syntax

The basic syntax of the `zip()` function is as follows:

```python
zip(iterable1, iterable2, ...)
```

### Example:

```python
fruits = ["apple", "banana", "cherry"]
prices = [1.0, 0.5, 1.5]

combined = zip(fruits, prices)
print(list(combined))  # Output: [('apple', 1.0), ('banana', 0.5), ('cherry', 1.5)]
```

## Using `zip()` with `for` Loop

You can use `zip()` with a `for` loop to iterate over multiple iterables simultaneously.

```python
fruits = ["apple", "banana", "cherry"]
prices = [1.0, 0.5, 1.5]

for fruit, price in zip(fruits, prices):
    print(f"{fruit}: ${price}")
```

## Unzipping a Sequence

You can use the `zip()` function along with the unpacking operator (`*`) to "unzip" a sequence of tuples into separate lists.

```python
zipped = [('apple', 1.0), ('banana', 0.5), ('cherry', 1.5)]
fruits, prices = zip(*zipped)

print(fruits)   # Output: ('apple', 'banana', 'cherry')
print(prices)   # Output: (1.0, 0.5, 1.5)
```

## Key Points:

- The `zip()` function is used to combine multiple iterable objects into a single iterator of tuples.
- Each tuple contains corresponding elements from all the input iterables.
- If the input iterables are of different lengths, `zip()` will stop when the shortest iterable is exhausted.
- You can use `zip()` with a `for` loop to iterate over multiple iterables simultaneously.
- `zip()` can also be used to "unzip" a sequence of tuples into separate lists using the unpacking operator (`*`).

Understanding how to use the `zip()` function allows you to work with multiple iterables more efficiently, especially when iterating over them simultaneously or combining their elements in various ways.
