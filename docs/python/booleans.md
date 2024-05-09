#### [Return Back](../../python_for_testers.md)

# Booleans

Boolean values represent truth values and are used to perform logical operations in Python. There are two Boolean values in Python: `True` and `False`. Booleans are commonly used in conditional statements, loops, and logical operations.

## Boolean Data Type

- **True**: Represents true or on.
- **False**: Represents false or off.

```python
is_student = True
has_account = False
```

## Boolean Operations

Python supports several operations to work with Boolean values:

1. **Logical AND (`and`)**: Returns `True` if both operands are `True`, otherwise returns `False`.

    ```python
    print(True and True)    # Output: True
    print(True and False)   # Output: False
    print(False and False)  # Output: False
    ```

2. **Logical OR (`or`)**: Returns `True` if at least one operand is `True`, otherwise returns `False`.

    ```python
    print(True or True)     # Output: True
    print(True or False)    # Output: True
    print(False or False)   # Output: False
    ```

3. **Logical NOT (`not`)**: Returns the opposite of the operand's Boolean value.

    ```python
    print(not True)     # Output: False
    print(not False)    # Output: True
    ```

## Comparison Operators

Comparison operators also return Boolean values:

- **Equal to (`==`)**: Returns `True` if both operands are equal.
- **Not equal to (`!=`)**: Returns `True` if operands are not equal.
- **Greater than (`>`)**: Returns `True` if the left operand is greater than the right operand.
- **Less than (`<`)**: Returns `True` if the left operand is less than the right operand.
- **Greater than or equal to (`>=`)**: Returns `True` if the left operand is greater than or equal to the right operand.
- **Less than or equal to (`<=`)**: Returns `True` if the left operand is less than or equal to the right operand.

```python
print(10 == 10)   # Output: True
print(10 != 5)    # Output: True
print(10 > 5)     # Output: True
print(10 < 5)     # Output: False
print(10 >= 10)   # Output: True
print(10 <= 5)    # Output: False
```

## Conversion to Boolean

In Python, certain objects can be evaluated as `True` or `False`. For example, empty sequences (lists, tuples, strings) and numeric zero values evaluate to `False`, while non-empty sequences and non-zero numeric values evaluate to `True`.

```python
print(bool([]))    # Output: False
print(bool([1, 2])) # Output: True
print(bool(0))      # Output: False
print(bool(10))     # Output: True
```

Understanding Booleans is fundamental for writing conditionals and logical operations in Python, enabling you to control the flow of your program based on certain conditions.
