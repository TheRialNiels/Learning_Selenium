#### [Return Back](../python_for_testers.md)

# Variable Scope

Variable scope refers to the visibility and accessibility of variables within different parts of a program. In Python, variables can have either local scope, meaning they are accessible only within a specific block of code, or global scope, meaning they are accessible throughout the entire program. Understanding variable scope is essential for writing clear and maintainable code.

## Local Scope

Variables defined within a function have local scope. They are accessible only within the function where they are defined. Once the function execution completes, local variables are destroyed, and their memory space is reclaimed.

```python
def my_function():
    x = 10  # Local variable
    print(x)

my_function()  # Output: 10
print(x)       # Error: NameError: name 'x' is not defined
```

## Global Scope

Variables defined outside any function have global scope. They are accessible throughout the entire program, including within functions. Global variables persist until the program terminates or until they are explicitly deleted.

```python
x = 10  # Global variable

def my_function():
    print(x)

my_function()  # Output: 10
print(x)       # Output: 10
```

## Global Keyword

The `global` keyword is used inside a function to declare that a variable is defined in the global scope, rather than creating a new local variable with the same name.

```python
x = 10  # Global variable

def my_function():
    global x
    x = 20
    print(x)

my_function()  # Output: 20
print(x)       # Output: 20
```

## LEGB Rule

Python follows the LEGB rule to determine the scope of a variable:

- **Local (L)**: Variables defined within a function have local scope.
- **Enclosing (E)**: Variables defined in the enclosing function (if any) have enclosing scope.
- **Global (G)**: Variables defined at the global level have global scope.
- **Built-in (B)**: Predefined names in Python, such as `print()` and `len()`, have built-in scope.

```python
x = 10  # Global variable

def outer_function():
    y = 20  # Enclosing variable

    def inner_function():
        z = 30  # Local variable
        print(x)   # Accessible (global scope)
        print(y)   # Accessible (enclosing scope)
        print(z)   # Accessible (local scope)

    inner_function()

outer_function()
```

Understanding variable scope and the LEGB rule is crucial for writing clean and efficient code in Python, as it allows you to manage the visibility and accessibility of variables effectively.
