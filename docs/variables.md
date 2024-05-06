#### [Return Back](../python_for_testers.md)

# Variables

Variables are used to store data in a program. Unlike some other programming languages, Python is dynamically typed, which means you don't have to explicitly declare the data type of a variable. Here's how you can use variables in Python:

## Variable Assignment

You can assign a value to a variable using the equal (=) sign.

```python
# Assigning values to variables
x = 10
name = "John Doe"
```

## Variable Naming Rules

When naming variables in Python, it's essential to follow certain rules to ensure clarity and avoid errors. Here are the key rules to keep in mind:

- **Valid Characters:** Variable names can contain letters (a-z, A-Z), digits (0-9), and underscores (_). However, they cannot start with a digit.

    ```python
    # Valid variable names
    my_var = 10
    name_1 = "John"
    age = 30

    # Invalid variable names
    1_name = "Invalid"  # Cannot start with a digit
    $price = 100        # Special characters are not allowed
    ```

- **Case Sensitivity:** Variable names are case-sensitive, meaning my_var, My_Var, and MY_VAR are treated as different variables.

    ```python
    my_var = 10
    My_Var = 20
    MY_VAR = 30

    print(my_var, My_Var, MY_VAR)  # Output: 10 20 30
    ```

- **Reserved Keywords:** Avoid using Python keywords as variable names. These keywords are reserved for specific purposes and cannot be used as identifiers.

    ```python
    # Invalid variable names using keywords
    if = 10
    for = 20
    while = 30
    ```

- **Meaningful Names:** Choose variable names that reflect their purpose or the data they store. This enhances code readability and makes it easier for others (and yourself) to understand the code.

    ```python
    # Good variable names
    age = 30
    name = "John"
    total_amount = 100.50
    ```

- **Snake Case:** Python conventionally uses snake_case for variable names, where words are separated by underscores. This convention improves readability compared to other naming styles.

    ```python
    # Snake case variable names
    first_name = "John"
    last_name = "Doe"
    ```

- **Avoid Ambiguity:** Ensure variable names are descriptive enough to convey their purpose but not overly verbose. Aim for clarity and brevity.

    ```python
    # Ambiguous variable name
    x = 10

    # More descriptive variable name
    user_age = 10
    ```

Following these rules ensures consistency and clarity in your code, making it easier to understand, maintain, and collaborate on. Adhering to Python naming conventions promotes readability and helps you write cleaner and more maintainable code.

## Data Types

Python supports various data types such as integers, floats, strings, lists, tuples, dictionaries, etc. You don't need to specify the data type explicitly when declaring a variable.

```python
# Integer
age = 25

# Float
salary = 2500.50

# String
name = "John Doe"

# Boolean
is_student = True
```

## Variable Reassignment

You can change the value of a variable after it has been assigned.

```python
x = 10
print(x)  # Output: 10

x = 20
print(x)  # Output: 20
```

## Variable Scope

Variables in Python have scope, meaning they are only accessible within certain parts of the code.

- Global Variables: Defined outside of any function or block, they can be accessed from anywhere in the code.
- Local Variables: Defined inside a function or block, they can only be accessed within that function or block.

```python
# Global variable
global_var = 10

def my_function():
    # Local variable
    local_var = 20
    print(global_var)  # Accessing global variable
    print(local_var)   # Accessing local variable

my_function()
```
