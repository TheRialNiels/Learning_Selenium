#### [Return Back](../../python_for_testers.md)

# If Conditional Statement

The `if` statement is used in Python for conditional execution of code. It allows you to execute a block of code if a specified condition evaluates to `True`.

## Basic Syntax

The basic syntax of the `if` statement is as follows:

```python
if condition:
    # Execute this block if the condition is True
    statement(s)
```

## Example:

```python
x = 10

if x > 5:
    print("x is greater than 5")
```

## Conditional Expressions

The condition in an `if` statement can be any expression that evaluates to a Boolean value (`True` or `False`). Common conditional expressions include comparisons (`==`, `!=`, `<`, `>`, `<=`, `>=`), logical operators (`and`, `or`, `not`), and membership (`in`, `not in`).

```python
x = 10
y = 5

if x > y:
    print("x is greater than y")

if x != 0 and y != 0:
    print("Both x and y are non-zero")

if 'a' in ['a', 'b', 'c']:
    print("a is in the list")
```

## elif and else Clauses

You can use `elif` (short for "else if") and `else` clauses to specify additional conditions and fallback behavior.

```python
x = 10

if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")
```

## Nested if Statements

You can nest `if` statements within other `if`, `elif`, or `else` blocks to handle more complex conditions.

```python
x = 10
y = 5

if x > 5:
    if y > 2:
        print("Both x and y are greater than their respective thresholds")
    else:
        print("x is greater than 5, but y is not greater than 2")
else:
    print("x is not greater than 5")
```

## Ternary Conditional Operator

Python also supports a ternary conditional operator, which provides a concise way to express conditional expressions.

```python
x = 10

result = "x is greater than 5" if x > 5 else "x is not greater than 5"
print(result)
```

## Indentation

Indentation is crucial in Python as it defines the block of code associated with the `if` statement. All statements within the same block must be indented by the same amount.

```python
x = 10

if x > 5:
    print("Inside the if block")  # Correct indentation
print("Outside the if block")     # Incorrect indentation (not part of the if block)
```

Understanding how to use `if` statements effectively allows you to control the flow of your program based on specific conditions, making your code more flexible and powerful.
