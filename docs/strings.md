#### [Return Back](../python_for_testers.md)

# Strings

Strings are sequences of characters, represented within single quotes (`'`) or double quotes (`"`). They are immutable, meaning once created, their contents cannot be changed. Python provides a rich set of methods to manipulate and work with strings efficiently.

## Creating Strings

You can create strings using single quotes, double quotes, or triple quotes for multi-line strings.

```python
# Single quotes
single_quoted = 'Hello, World!'

# Double quotes
double_quoted = "Hello, World!"

# Triple quotes for multi-line strings
multi_line = '''This is a
multi-line string.'''
```

## Accessing Characters

You can access individual characters of a string using indexing. Python uses zero-based indexing.

```python
s = "Hello"

print(s[0])    # Output: H
print(s[-1])   # Output: o
```

## String Slicing

You can extract substrings from a string using slicing.

```python
s = "Hello, World!"

print(s[1:5])   # Output: ello
print(s[:5])    # Output: Hello
print(s[7:])    # Output: World!
print(s[::2])   # Output: HloWrd
```

## String Concatenation

You can concatenate strings using the `+` operator or the `+=` compound assignment operator.

```python
s1 = "Hello"
s2 = "World!"

concatenated = s1 + ", " + s2
print(concatenated)  # Output: Hello, World!

s1 += " "
s1 += s2
print(s1)            # Output: Hello World!
```

## String Methods

Python provides a wide range of methods for working with strings, including:

- **`len()`:** Returns the length of the string.
- **`lower()`, `upper()`:** Converts the string to lowercase or uppercase.
- **`strip()`, `lstrip()`, `rstrip()`:** Removes leading and trailing whitespace.
- **`replace(old, new)`:** Replaces occurrences of a substring with another substring.
- **`split(sep)`:** Splits the string into a list of substrings using the specified separator.
- **`join(iterable)`:** Concatenates strings from an iterable with the string as a separator.

```python
s = " Hello, World! "

print(len(s))          # Output: 15
print(s.lower())       # Output:  hello, world!
print(s.strip())       # Output: Hello, World!
print(s.replace("o", "X"))  # Output: HellX, WXrld!
print(s.split(","))    # Output: [' Hello', ' World! ']
print("-".join(["Hello", "World"]))  # Output: Hello-World
```

## String Formatting

Python provides several methods for string formatting:

- **`%` Operator**: C-style string formatting.
- **`format()` Method**: String formatting using placeholders.
- **Formatted String Literals (f-strings)**: Introduced in Python 3.6, allows embedding expressions directly within strings.

```python
name = "John"
age = 30

# Using % operator
print("Name: %s, Age: %d" % (name, age))

# Using format() method
print("Name: {}, Age: {}".format(name, age))

# Using f-strings
print(f"Name: {name}, Age: {age}")
```

## String Operations

Python supports various string operations, including:

- **Membership (`in`, `not in`)**: Checks if a substring exists in a string.
- **Concatenation (`+`)**: Concatenates strings.
- **Repetition (`*`)**: Repeats a string a specified number of times.

```python
s = "Hello, World!"

print("World" in s)    # Output: True
print("Python" not in s)  # Output: True

print(s + " Python")   # Output: Hello, World! Python
print(s * 3)           # Output: Hello, World!Hello, World!Hello, World!
```

Sure! Here's an addition to the guide covering multiline strings:

## Multiline Strings

Multiline strings in Python allow you to define strings that span multiple lines. They are often used for docstrings, writing SQL queries, or defining large blocks of text.

### Creating Multiline Strings

You can create multiline strings using triple quotes (`'''` or `"""`).

```python
# Using triple quotes
multi_line = '''This is a
multi-line string.'''

# Using triple quotes with double quotes inside
multi_line_with_quotes = """This is a
multi-line string with "quotes" inside."""

# Using parentheses for multiline strings
multi_line_parentheses = (
    "This is a\n"
    "multi-line string using parentheses.\n"
    "It's useful for long strings."
)
```

### Accessing Multiline Strings

Multiline strings behave like regular strings and support all string operations, including indexing, slicing, concatenation, and string methods.

```python
print(multi_line[0])    # Output: T
print(multi_line[:4])   # Output: This
```

### Multiline Strings in Functions and Docstrings

Multiline strings are commonly used for writing docstrings for functions and classes.

```python
def my_function():
    """
    This function does something.

    Parameters:
    None

    Returns:
    None
    """
    pass
```

## String Functions in Python

Python provides a rich set of built-in functions for working with strings efficiently. Here are some of the most commonly used string functions:

### 1. `len()`

Returns the length of the string.

```python
s = "Hello, World!"
print(len(s))  # Output: 13
```

### 2. `str()`

Converts the specified value into a string.

```python
x = 10
print(str(x))  # Output: '10'
```

### 3. `upper()`

Converts all characters in the string to uppercase.

```python
s = "Hello, World!"
print(s.upper())  # Output: HELLO, WORLD!
```

### 4. `lower()`

Converts all characters in the string to lowercase.

```python
s = "Hello, World!"
print(s.lower())  # Output: hello, world!
```

### 5. `count()`

Returns the number of occurrences of a substring in the string.

```python
s = "Hello, World!"
print(s.count('l'))  # Output: 3
```

### 6. `isupper()`

Returns `True` if all characters in the string are uppercase, otherwise `False`.

```python
s = "HELLO"
print(s.isupper())  # Output: True
```

### 7. `islower()`

Returns `True` if all characters in the string are lowercase, otherwise `False`.

```python
s = "hello"
print(s.islower())  # Output: True
```

### 8. `split()`

Splits the string into a list of substrings based on the specified delimiter.

```python
s = "Hello, World!"
print(s.split(','))  # Output: ['Hello', ' World!']
```

### 9. `rsplit()`

Splits the string into a list of substrings, starting from the right.

```python
s = "Hello, World!"
print(s.rsplit(',', 1))  # Output: ['Hello', ' World!']
```

### 10. `strip()`, `lstrip()`, `rstrip()`

Removes leading and trailing whitespace from the string.

```python
s = "   Hello, World!   "
print(s.strip())   # Output: "Hello, World!"
print(s.lstrip())  # Output: "Hello, World!   "
print(s.rstrip())  # Output: "   Hello, World!"
```

### 11. `replace()`

Replaces occurrences of a substring with another substring.

```python
s = "Hello, World!"
print(s.replace("World", "Python"))  # Output: Hello, Python!
```

### 12. `find()`

Returns the lowest index of the substring if found in the string, otherwise returns -1.

```python
s = "Hello, World!"
print(s.find("World"))  # Output: 7
print(s.find("Python"))  # Output: -1
```

### 13. `index()`

Similar to `find()`, but raises a ValueError if the substring is not found.

```python
s = "Hello, World!"
print(s.index("World"))  # Output: 7
# print(s.index("Python"))  # Raises ValueError
```

These functions provide powerful tools for manipulating and analyzing strings in Python, enabling you to perform a wide range of tasks efficiently.
