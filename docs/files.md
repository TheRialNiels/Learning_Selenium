#### [Return Back](../python_for_testers.md)

# Files

Reading from and writing to files is a common task in Python for handling data persistence. Python provides built-in functions and methods for working with files. Here's how you can write and read files in Python:

## Writing to a File

You can write data to a file using the `open()` function with the mode `'w'` (write mode) or `'a'` (append mode).

```python
# Open a file in write mode
with open("example.txt", "w") as file:
    # Write data to the file
    file.write("Hello, world!\n")
    file.write("This is a sample text.")
```

## Appending to a File

You can append data to an existing file using the mode `'a'` (append mode).

```python
# Open a file in append mode
with open("example.txt", "a") as file:
    # Append data to the file
    file.write("\nAppending more text to the file.")
```

## Reading from a File

You can read data from a file using the `open()` function with the mode `'r'` (read mode).

```python
# Open a file in read mode
with open("example.txt", "r") as file:
    # Read data from the file
    data = file.read()
    print(data)
```

## Reading Lines from a File

You can read lines from a file using the `readline()` method to read one line at a time, or the `readlines()` method to read all lines at once and return a list.

```python
# Open a file in read mode
with open("example.txt", "r") as file:
    # Read one line at a time
    line1 = file.readline()
    print(line1)

    # Read all lines at once
    lines = file.readlines()
    print(lines)
```

## Iterating over Lines

You can iterate over lines in a file using a `for` loop.

```python
# Open a file in read mode
with open("example.txt", "r") as file:
    # Iterate over lines
    for line in file:
        print(line)
```

## Handling File Paths

You can specify the path to the file when opening it using a relative or absolute file path.

```python
# Open a file using a relative file path
with open("folder/example.txt", "r") as file:
    # Read data from the file
    data = file.read()
    print(data)
```

## Error Handling

You should handle errors that may occur when working with files, such as `FileNotFoundError` when the file does not exist.

```python
try:
    with open("example.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File not found.")
```

## Closing Files Automatically

Using the `with` statement ensures that files are automatically closed when you're done with them, even if exceptions occur during file operations.

```python
with open("example.txt", "r") as file:
    data = file.read()
    print(data)
```

## Key Points

- Use the `open()` function to open files in different modes (write, append, read).
- Use the `with` statement to automatically close files after reading or writing.
- Use methods like `write()` to write data to files and `read()` to read data from files.
- You can read lines from files using `readline()`, `readlines()`, or iterate over lines using a `for` loop.
- Handle errors using `try` and `except` blocks to prevent crashes when working with files.

File handling in Python is flexible and versatile, allowing you to work with different types of files and handle various data manipulation tasks efficiently.
