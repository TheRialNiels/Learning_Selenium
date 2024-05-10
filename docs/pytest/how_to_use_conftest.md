#### [Return Back](../../pytest.md)

# How to Use `conftest.py` in Pytest

In Pytest, `conftest.py` is a special Python module that allows you to define fixtures, hooks, and other configurations that are shared across multiple test files within the same directory or its subdirectories. By placing fixture definitions and other shared configurations in `conftest.py`, you can avoid code duplication and ensure consistency across your test suite. Here's how to use `conftest.py` effectively:

## Creating a conftest.py File

To create a `conftest.py` file, simply create a Python file named `conftest.py` in the root directory of your test suite or in any directory where you want to share fixtures and configurations.

## Defining Fixtures

Inside `conftest.py`, you can define fixture functions using the `@pytest.fixture` decorator as you would in any other test module. These fixtures can then be used by test functions in any test file within the same directory or its subdirectories.

```python
# conftest.py

import pytest

@pytest.fixture
def setup_database():
    # Setup database connection
    db = Database()
    yield db  # Provide the fixture object
    # Teardown database connection
    db.close()
```

## Using Fixtures in Tests

Once fixtures are defined in `conftest.py`, they can be used in test functions across your test suite without needing to import them explicitly. Pytest automatically discovers and uses fixtures defined in `conftest.py` based on their names.

```python
# test_example.py

def test_fetch_data(setup_database):
    data = setup_database.fetch_data()
    assert len(data) > 0
```

## Sharing Fixtures Across Test Files

Fixtures defined in `conftest.py` are automatically available to all test files within the same directory or its subdirectories. This allows you to share fixture definitions and reuse them across multiple test files without duplicating code.

## Defining Hooks and Configurations

In addition to fixtures, `conftest.py` can also define hooks and other configurations using Pytest's plugin system. Hooks allow you to customize the test execution process, while configurations allow you to specify global settings for your test suite.

```python
# conftest.py

def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark test as slow to run")

def pytest_runtest_setup(item):
    if "slow" in item.keywords:
        item.parent.parent.parent.config.option.run_slow_tests = True
```

## Conclusion

`conftest.py` is a powerful tool in Pytest for sharing fixtures, hooks, and configurations across multiple test files within the same directory or its subdirectories. By centralizing fixture definitions and other shared configurations in `conftest.py`, you can improve code organization, reduce code duplication, and ensure consistency across your test suite. Experiment with `conftest.py` to optimize your testing workflow and create maintainable and scalable test suites in Pytest.
