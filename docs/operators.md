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

Understanding and mastering these operators are essential for writing efficient and concise Python code. They enable you to perform a wide range of operations, from simple arithmetic to complex logical manipulations and bitwise operations.
