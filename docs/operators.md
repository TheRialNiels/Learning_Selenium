#### [Return Back](../python_for_testers.md)

# Operators in Python

Operators in Python are special symbols or keywords that perform operations on operands (variables or values). Python supports various types of operators, including:

## Arithmetic Operators

Arithmetic operators perform mathematical operations on numeric operands.

- **Addition (+):** Adds two operands.
- **Subtraction (-):** Subtracts the second operand from the first.
- **Multiplication (*):** Multiplies two operands.
- **Division (/):** Divides the first operand by the second.
- **Modulus (%):** Returns the remainder of the division.
- **Exponentiation ()\**:** Raises the first operand to the power of the second.
- **Floor Division (//):** Returns the quotient of the division, discarding any fractional part.

```python
a = 10
b = 3

print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333...
print(a % b)  # Output: 1
print(a ** b) # Output: 1000
print(a // b) # Output: 3
```

## Assignment Operators

Assignment operators are used to assign values to variables.

- **Assignment (=):** Assigns the value on the right to the variable on the left.
- **Compound Assignment (+=, -=, \*=, /=, %=, //=, =):** Performs the operation and assigns the result to the variable.

```python
x = 10
y = 5

x += 5  # Equivalent to x = x + 5
y **= 2 # Equivalent to y = y ** 2

print(x)  # Output: 15
print(y)  # Output: 25
```

## Comparison Operators

Comparison operators compare the values of two operands and return a Boolean value (True or False).

- **Equal to (==)**
- **Not equal to (!=)**
- **Greater than (>)**
- **Less than (<)**
- **Greater than or equal to (>=)**
- **Less than or equal to (<=)**

```python
a = 10
b = 20

print(a == b)  # Output: False
print(a != b)  # Output: True
print(a > b)   # Output: False
print(a < b)   # Output: True
print(a >= b)  # Output: False
print(a <= b)  # Output: True
```

## Logical Operators

Logical operators perform logical operations on Boolean values.

- **Logical AND (and):** Returns True if both operands are True.
- **Logical OR (or):** Returns True if at least one operand is True.
- **Logical NOT (not):** Returns the opposite of the operand's Boolean value.

```python
x = True
y = False

print(x and y)  # Output: False
print(x or y)   # Output: True
print(not x)    # Output: False
```

## Identity Operators

Identity operators compare the memory locations of two objects.

- **Identity (is):** Returns True if both operands refer to the same object.
- **Non-identity (is not):** Returns True if both operands refer to different objects.

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)   # Output: False
print(a is c)   # Output: True
print(a is not b)  # Output: True
```

## Membership Operators

Membership operators test for membership in a sequence (e.g., lists, tuples, strings).

- **Membership (in):** Returns True if a value exists in the sequence.
- **Not Membership (not in):** Returns True if a value does not exist in the sequence.

```python
my_list = [1, 2, 3, 4]

print(1 in my_list)   # Output: True
print(5 not in my_list)  # Output: True
```

## Operators Precedence

Operator precedence determines the order in which operations are performed in an expression. In Python, as in many programming languages, certain operators have higher precedence than others, meaning they are evaluated first. Here's a summary of the operator precedence in Python, from highest to lowest:

- **Parentheses:** Expressions within parentheses are evaluated first.
- **Exponentiation (**):** Exponentiation is performed next.
- **Unary Arithmetic Operations:** Unary positive (+) and unary negation (-) are applied to operands.
- **Multiplication, Division, and Modulus (*, /, %):** Multiplication, division, and modulus operations are performed next, from left to right.
- **Addition and Subtraction (+, -):** Addition and subtraction operations are performed next, from left to right.
- **Logical NOT (not):** Logical NOT operation is performed next.
- **Logical AND (and):** Logical AND operation is performed next.
- **Logical OR (or):** Logical OR operation is performed next.
- **Assignment Operators (=, +=, -= etc.):** Assignment operations are performed last.

Here's an example demonstrating operator precedence:

```python
result = 5 + 2 * 3 ** 2 - 1
# First, 3 ** 2 is evaluated: 9
# Then, 2 * 9 is evaluated: 18
# Next, 5 + 18 is evaluated: 23
# Finally, 23 - 1 is evaluated: 22

print(result)  # Output: 22
```

To override the precedence and force a particular order of evaluation, you can use parentheses. Expressions within parentheses are always evaluated first. For example:

```python
result = (5 + 2) * (3 ** 2 - 1)
# First, 3 ** 2 is evaluated: 9
# Then, 9 - 1 is evaluated: 8
# Next, 5 + 2 is evaluated: 7
# Finally, 7 * 8 is evaluated: 56

print(result)  # Output: 56
```

Understanding operator precedence is crucial for writing expressions that behave as intended and avoiding errors caused by unexpected evaluation order.