#### [Return Back](../../pytest.md)

# Grouping Tests

In Pytest, you can mark test functions or classes using the `@pytest.mark` decorator to categorize or label them based on certain criteria. This allows you to selectively run tests based on their marks or apply specific behaviors or configurations to marked tests. Here's how you can use the `@pytest.mark` decorator to mark test cases with custom names:

## Marking Test Functions with Custom Names

You can mark test functions using the `@pytest.mark.<name>` decorator to assign custom marks to them.

```python
import pytest

@pytest.mark.math
def test_addition():
    assert 2 + 2 == 4

@pytest.mark.math
def test_subtraction():
    assert 5 - 3 == 2

@pytest.mark.string
def test_concatenation():
    assert "Hello, " + "World" == "Hello, World"

@pytest.mark.string
def test_uppercase():
    assert "hello".upper() == "HELLO"
```

In this example, the `@pytest.mark.math` decorator marks the `test_addition` and `test_subtraction` functions as belonging to the "math" category, while the `@pytest.mark.string` decorator marks the `test_concatenation` and `test_uppercase` functions as belonging to the "string" category.

## Running Marked Tests

To run tests based on their marks, you can use the `-m` option with Pytest and specify the mark names:

```
pytest -m math path/to/test_directory
```

This command will execute only the tests marked with the "math" mark. Similarly, you can run tests marked with other custom marks by specifying their names.

## Conclusion

Using the `@pytest.mark` decorator, you can mark test functions or classes with custom names to categorize or label them based on specific criteria. This allows you to selectively run tests based on their marks or apply configurations or behaviors to marked tests. Experiment with marking tests to organize your test suite effectively and enhance the flexibility and maintainability of your test codebase.
