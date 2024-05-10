#### [Return Back](../../pytest.md)

# Parametrizing Fixtures and Functions

In Pytest, you can parameterize fixtures and test functions to run them with different input values or configurations. This allows you to write concise and expressive tests that cover various scenarios using a single test function or fixture. Here's how to parametrize fixtures and functions in Pytest:

## Parametrizing Fixtures

You can parametrize fixtures using the `@pytest.fixture(params=...)` decorator. This allows you to define a fixture that produces multiple instances based on different parameter values.

```python
# conftest.py

import pytest

@pytest.fixture(params=[1, 2, 3])
def input_value(request):
    return request.param
```

In this example, the `input_value` fixture is parametrized with three different values: 1, 2, and 3. When tests use this fixture, Pytest will automatically invoke the test function multiple times, each time with a different parameter value.

## Parametrizing Test Functions

You can parametrize test functions using the `@pytest.mark.parametrize` decorator. This allows you to specify multiple sets of input values and expected outcomes for a single test function.

```python
# test_example.py

import pytest

@pytest.mark.parametrize("input_value, expected_output", [
    (1, 2),
    (2, 4),
    (3, 6)
])
def test_multiply_by_two(input_value, expected_output):
    assert input_value * 2 == expected_output
```

In this example, the `test_multiply_by_two` test function is parametrized with three sets of input values (`input_value`) and expected outcomes (`expected_output`). Pytest will execute the test function three times, once for each parameterized set, and report the result for each set independently.

## Combining Fixture Parametrization with Test Parametrization

You can also combine fixture parametrization with test parametrization to create complex test scenarios.

```python
# conftest.py

import pytest

@pytest.fixture(params=["apple", "banana"])
def fruit(request):
    return request.param

# test_example.py

import pytest

@pytest.mark.parametrize("num", [1, 2, 3])
def test_fruit_count(fruit, num):
    assert len(fruit) * num == 6
```

In this example, the `fruit` fixture is parametrized with two different fruits: "apple" and "banana". The `test_fruit_count` test function is parametrized with three different numbers: 1, 2, and 3. Pytest will execute the test function six times, combining each fruit with each number.

## Conclusion

Parametrizing fixtures and test functions in Pytest allows you to write concise and expressive tests that cover various scenarios using a single test function or fixture. By defining multiple parameter values and expected outcomes, you can easily test different input configurations and ensure the correctness of your code under different conditions. Experiment with fixture and test parametrization to create versatile and comprehensive test suites in Pytest.
