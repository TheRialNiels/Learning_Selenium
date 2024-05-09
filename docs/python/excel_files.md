#### [Return Back](../../python_for_testers.md)

# Excel Files

To read and write data to an Excel file in Python, you can use the `openpyxl` library, which is a powerful and easy-to-use library for working with Excel files. First, make sure to install the library using pip:

```bash
pip install openpyxl
```

## Writing Data to an Excel File

```python
from openpyxl import Workbook

# Create a new Workbook object
workbook = Workbook()

# Select the active worksheet
sheet = workbook.active

# Write data to cells
sheet["A1"] = "Name"
sheet["B1"] = "Age"
sheet["A2"] = "Alice"
sheet["B2"] = 30
sheet["A3"] = "Bob"
sheet["B3"] = 25

# Save the workbook to a file
workbook.save(filename="example.xlsx")
```

## Reading Data from an Excel File

```python
from openpyxl import load_workbook

# Load the workbook from a file
workbook = load_workbook(filename="example.xlsx")

# Select the active worksheet
sheet = workbook.active

# Read data from cells
name = sheet["A2"].value
age = sheet["B2"].value

print(f"Name: {name}, Age: {age}")
```

## Iterating over Rows and Columns

```python
for row in sheet.iter_rows(values_only=True):
    name, age = row
    print(f"Name: {name}, Age: {age}")

for column in sheet.iter_cols(min_row=2, max_row=3, min_col=1, max_col=2, values_only=True):
    print(column)
```

## Creating and Selecting Worksheets

```python
# Create a new worksheet
workbook.create_sheet("Sheet2")

# Select a specific worksheet by its name
sheet = workbook["Sheet2"]

# Change the title of a worksheet
sheet.title = "NewSheet"
```

## Key Points

- Use `openpyxl` library to work with Excel files in Python.
- Use `Workbook()` to create a new workbook and `load_workbook()` to load an existing workbook.
- Use `active` attribute to select the active worksheet in the workbook.
- Write data to cells using the cell indices like `"A1"`, `"B1"`, etc.
- Read data from cells using the cell indices and the `value` attribute.
- Use `iter_rows()` and `iter_cols()` to iterate over rows and columns in a worksheet.

With `openpyxl`, you can perform various operations such as creating, reading, and writing Excel files, manipulating worksheets, formatting cells, and much more. It's a powerful tool for working with Excel files in Python.
