#### [Return Back](../python_for_testers.md)

# While Loop

The `while` loop is used in Python to repeatedly execute a block of code as long as a specified condition evaluates to `True`. It allows you to create loops with indeterminate iterations, meaning the number of iterations is not predetermined but depends on the condition.

## Basic Syntax

The basic syntax of the `while` loop is as follows:

```python
while condition:
    # Execute this block of code as long as the condition is True
    statement(s)
```

### Example:

```python
x = 0

while x < 5:
    print(x)
    x += 1
```

## Infinite Loop

Be cautious when using `while` loops, as they can lead to an infinite loop if the condition never becomes `False`. An infinite loop will continue executing indefinitely, potentially causing the program to become unresponsive.

```python
# Infinite loop
while True:
    print("This is an infinite loop")
```

## Exiting the Loop

You can exit a `while` loop prematurely using the `break` statement. When encountered, `break` immediately exits the loop, regardless of the loop condition.

```python
x = 0

while True:
    print(x)
    if x == 3:
        break
    x += 1
```

## Skipping Iterations

You can skip the rest of the current iteration and continue to the next iteration of the loop using the `continue` statement.

```python
x = 0

while x < 5:
    x += 1
    if x == 3:
        continue
    print(x)
```

## else Clause

A `while` loop can also have an `else` clause, which is executed when the loop terminates normally (i.e., when the condition becomes `False`).

```python
x = 0

while x < 5:
    print(x)
    x += 1
else:
    print("Loop completed normally")
```

## Nested While Loops

You can nest `while` loops within other `while`, `for`, or `if` blocks to handle more complex scenarios.

```python
x = 0
y = 0

while x < 3:
    while y < 3:
        print(f"x: {x}, y: {y}")
        y += 1
    x += 1
    y = 0
```

## Indentation

Indentation is crucial in Python as it defines the block of code associated with the `while` loop. All statements within the same block must be indented by the same amount.

```python
x = 0

while x < 5:
    print(x)   # Correct indentation
  x += 1       # Incorrect indentation (not part of the while loop block)
```

Understanding how to use `while` loops effectively allows you to create loops that run until a specific condition is met, enabling you to perform repetitive tasks and control the flow of your program.
