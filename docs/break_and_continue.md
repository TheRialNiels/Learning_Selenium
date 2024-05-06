#### [Return Back](../python_for_testers.md)

# Break Statement

The `break` statement is used to exit the loop prematurely. When the `break` statement is encountered inside a loop, the loop is immediately terminated, and the program continues executing from the statement immediately following the loop.

### Example:

```python
# Using break to exit a loop prematurely
x = 0

while True:
    print(x)
    if x == 3:
        break
    x += 1
```

In this example, the loop will print numbers from 0 to 3, and then the `break` statement will terminate the loop when `x` equals 3.

## Continue Statement

The `continue` statement is used to skip the rest of the current iteration of the loop and continue with the next iteration. When the `continue` statement is encountered inside a loop, the remaining statements in the loop are skipped, and the loop proceeds with the next iteration.

### Example:

```python
# Using continue to skip iterations
x = 0

while x < 5:
    x += 1
    if x == 3:
        continue
    print(x)
```

In this example, the loop will print numbers from 1 to 5, skipping the number 3. When `x` equals 3, the `continue` statement is encountered, causing the loop to skip printing that number and move to the next iteration.

## Key Points:

- `break` and `continue` are control flow statements used within loops to alter the flow of execution.
- `break` is used to exit the loop prematurely, terminating the loop when a specific condition is met.
- `continue` is used to skip the rest of the current iteration of the loop and continue with the next iteration.
- Both `break` and `continue` are useful for controlling the flow of execution within loops and handling specific conditions efficiently.

Understanding how to use `break` and `continue` statements allows you to write more flexible and efficient code, especially when dealing with loops and repetitive tasks.
