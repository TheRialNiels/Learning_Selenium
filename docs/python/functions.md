#### [Return Back](../../python_for_testers.md)

# Functions

Functions are blocks of reusable code that perform a specific task. They allow you to break down your program into smaller, manageable parts, making your code more organized, easier to read, and reusable. In Python, functions are defined using the `def` keyword.

## Basic Syntax

The basic syntax of defining a function in Python is as follows:

```python
def function_name(parameters):
    """
    Docstring: Description of the function
    """
    # Function body: Code to perform a specific task
    statement(s)
```

- `def`: Keyword used to define a function.
- `function_name`: Name of the function, which should be descriptive and follow the naming conventions.
- `parameters`: Inputs to the function, which are optional. Multiple parameters can be separated by commas.
- `docstring`: Optional documentation string that describes the purpose and usage of the function.
- `statement(s)`: Body of the function, where the actual code to perform a specific task is written.

### Example:

```python
def greet(name):
    """
    This function greets the user.
    """
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
```

## Calling a Function

To execute a function and perform its task, you need to call it by its name followed by parentheses `()` containing the arguments (if any).

```python
function_name(arguments)
```

## Return Statement

Functions can return a value using the `return` statement. The return statement terminates the function execution and returns the specified value (if any) to the caller.

```python
def add(a, b):
    """
    This function adds two numbers and returns the result.
    """
    return a + b

result = add(3, 5)
print(result)  # Output: 8
```

## Default Arguments

You can specify default values for function parameters, which are used when the argument is not provided during the function call.

```python
def greet(name="World"):
    print(f"Hello, {name}!")

greet()       # Output: Hello, World!
greet("Alice")  # Output: Hello, Alice!
```

## Arbitrary Arguments

Functions can accept a variable number of arguments using the `*args` parameter, which collects all extra positional arguments into a tuple.

```python
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(2, 3, 4))  # Output: 24
```

## Keyword Arguments

You can pass arguments to a function by specifying the parameter names along with the values using the format `parameter_name=value`. These are called keyword arguments.

```python
def greet(name, message):
    print(f"{message}, {name}!")

greet(message="Good morning", name="Alice")  # Output: Good morning, Alice!
```

## Lambda Functions

Lambda functions, also known as anonymous functions, are small, one-line functions defined using the `lambda` keyword.

```python
square = lambda x: x ** 2
print(square(5))  # Output: 25
```

## Scope of Variables

Variables defined inside a function have local scope, meaning they are accessible only within that function. Variables defined outside any function have global scope, meaning they are accessible throughout the program.

## Docstrings

Docstrings are used to provide documentation for functions, classes, and modules. They are enclosed in triple quotes (`"""`) and are placed immediately after the function definition.

## Key Points:

- Functions are blocks of reusable code that perform a specific task.
- They are defined using the `def` keyword and can have parameters, a docstring, and a return statement.
- Functions can accept positional arguments, default arguments, arbitrary arguments, and keyword arguments.
- Lambda functions are small, one-line functions defined using the `lambda` keyword.
- Functions can have local variables with local scope and global variables with global scope.
- Docstrings are used to provide documentation for functions.

Understanding how to define, call, and work with functions allows you to write modular and reusable code, making your programs more efficient and maintainable.
