#### [Return Back](../../python_for_testers.md)

# Exception Handling

Exception handling in Python allows you to gracefully handle errors and unexpected situations that may occur during program execution. By using try-except blocks, you can catch and handle exceptions, preventing your program from crashing. Here's an overview of exception handling in Python:

## Basic Syntax

Exception handling is done using the `try`, `except`, and optional `else` and `finally` blocks.

```python
try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle specific exception
    print("Division by zero error occurred!")
else:
    # Execute if no exception is raised
    print("No exception occurred.")
finally:
    # Execute always, whether exception occurs or not
    print("Finally block executed.")
```

## Catching Specific Exceptions

You can catch specific exceptions using multiple `except` blocks.

```python
try:
    # Code that may raise an exception
    result = int("abc")
except ValueError:
    # Handle ValueError
    print("ValueError occurred!")
except ZeroDivisionError:
    # Handle ZeroDivisionError
    print("ZeroDivisionError occurred!")
```

## Handling Multiple Exceptions

You can handle multiple exceptions in a single `except` block by specifying them as a tuple.

```python
try:
    # Code that may raise an exception
    result = int("abc") / 0
except (ValueError, ZeroDivisionError) as e:
    # Handle multiple exceptions
    print(f"Error occurred: {e}")
```

## Raising Exceptions

You can raise exceptions explicitly using the `raise` statement.

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")

try:
    validate_age(-5)
except ValueError as e:
    print(f"Error occurred: {e}")
```

## Custom Exception Classes

You can define custom exception classes by inheriting from the `Exception` class.

```python
class CustomError(Exception):
    pass

try:
    raise CustomError("Custom error message")
except CustomError as e:
    print(f"Custom error occurred: {e}")
```

## Accessing Exception Information

You can access information about the exception using the `as` keyword.

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")
```

## Key Points

- Exception handling in Python is done using `try`, `except`, `else`, and `finally` blocks.
- Use `try` to wrap code that may raise an exception, and `except` to catch and handle exceptions.
- Catch specific exceptions to handle different types of errors.
- Use `else` to execute code if no exception occurs, and `finally` to execute cleanup code regardless of whether an exception occurs.
- Raise exceptions explicitly using the `raise` statement.
- Define custom exception classes by inheriting from the `Exception` class.
- Access information about exceptions using the `as` keyword.

Exception handling allows you to write robust and resilient code by handling errors gracefully and providing feedback to users when something goes wrong.
