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

## String Functions

Python provides a rich set of built-in functions for working with strings efficiently. Here are some of the most commonly used string functions:

- `len()`

  Returns the length of the string.

  ```python
  s = "Hello, World!"
  print(len(s))  # Output: 13
  ```

- `str()`

  Converts the specified value into a string.

  ```python
  x = 10
  print(str(x))  # Output: '10'
  ```

- `upper()`

  Converts all characters in the string to uppercase.

  ```python
  s = "Hello, World!"
  print(s.upper())  # Output: HELLO, WORLD!
  ```

- `lower()`

  Converts all characters in the string to lowercase.

  ```python
  s = "Hello, World!"
  print(s.lower())  # Output: hello, world!
  ```

- `count()`

  Returns the number of occurrences of a substring in the string.

  ```python
  s = "Hello, World!"
  print(s.count('l'))  # Output: 3
  ```

- `isupper()`

  Returns `True` if all characters in the string are uppercase, otherwise `False`.

  ```python
  s = "HELLO"
  print(s.isupper())  # Output: True
  ```

- `islower()`

  Returns `True` if all characters in the string are lowercase, otherwise `False`.

  ```python
  s = "hello"
  print(s.islower())  # Output: True
  ```

- `split()`

  Splits the string into a list of substrings based on the specified delimiter.

  ```python
  s = "Hello, World!"
  print(s.split(','))  # Output: ['Hello', ' World!']
  ```

- `rsplit()`

  Splits the string into a list of substrings, starting from the right.

  ```python
  s = "Hello, World!"
  print(s.rsplit(',', 1))  # Output: ['Hello', ' World!']
  ```

- `strip()`, `lstrip()`, `rstrip()`

  Removes leading and trailing whitespace from the string.

  ```python
  s = "   Hello, World!   "
  print(s.strip())   # Output: "Hello, World!"
  print(s.lstrip())  # Output: "Hello, World!   "
  print(s.rstrip())  # Output: "   Hello, World!"
  ```

- `replace()`

  Replaces occurrences of a substring with another substring.

  ```python
  s = "Hello, World!"
  print(s.replace("World", "Python"))  # Output: Hello, Python!
  ```

- `find()`

  Returns the lowest index of the substring if found in the string, otherwise returns -1.

  ```python
  s = "Hello, World!"
  print(s.find("World"))  # Output: 7
  print(s.find("Python"))  # Output: -1
  ```

- `index()`

  Similar to `find()`, but raises a ValueError if the substring is not found.

  ```python
  s = "Hello, World!"
  print(s.index("World"))  # Output: 7
  # print(s.index("Python"))  # Raises ValueError
  ```

These functions provide powerful tools for manipulating and analyzing strings in Python, enabling you to perform a wide range of tasks efficiently.

## Formatting Strings

### Using the `%` Operator

The `%` operator allows you to format strings using placeholders. The `%` operator is followed by a format specifier, such as `%s` for strings, `%d` for integers, `%f` for floating-point numbers, etc.

```python
name = "Alice"
age = 30

# Using % operator
formatted_string = "Name: %s, Age: %d" % (name, age)
print(formatted_string)  # Output: Name: Alice, Age: 30
```

### Using the `format()` Method

The `format()` method allows you to format strings using placeholders within curly braces `{}`. You can specify the order of variables using positional arguments or use keyword arguments for more clarity.

```python
name = "Alice"
age = 30

# Using format() method with positional arguments
formatted_string = "Name: {}, Age: {}".format(name, age)
print(formatted_string)  # Output: Name: Alice, Age: 30

# Using format() method with keyword arguments
formatted_string = "Name: {n}, Age: {a}".format(n=name, a=age)
print(formatted_string)  # Output: Name: Alice, Age: 30
```

### Using f-strings (Formatted String Literals)

f-strings provide a more concise and readable way to format strings since they allow you to embed expressions directly within strings. Simply prefix the string with `f` or `F` and embed variables or expressions within curly braces `{}`.

```python
name = "Alice"
age = 30

# Using f-strings
formatted_string = f"Name: {name}, Age: {age}"
print(formatted_string)  # Output: Name: Alice, Age: 30
```

### Formatting Numeric Values

You can specify formatting options for numeric values, such as precision for floating-point numbers, padding, and alignment.

```python
pi = 3.141592653589793

# Formatting floating-point numbers with specific precision
formatted_pi = "Value of pi: {:.2f}".format(pi)
print(formatted_pi)  # Output: Value of pi: 3.14

# Padding and alignment
formatted_number = "{:<10}".format(123)  # Left-aligned with width 10
print(formatted_number)  # Output: 123

formatted_number = "{:>10}".format(123)  # Right-aligned with width 10
print(formatted_number)  # Output:        123

formatted_number = "{:^10}".format(123)  # Center-aligned with width 10
print(formatted_number)  # Output:   123
```
