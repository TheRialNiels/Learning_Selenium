#### [Return Back](../../python_for_testers.md)

# Dictionaries

A dictionary is an unordered collection of key-value pairs. It is a mutable data type that allows you to store and retrieve data efficiently using keys. Dictionaries are commonly used for mapping unique keys to corresponding values and are often referred to as associative arrays or hashmaps in other programming languages.

## Creating Dictionaries

You can create dictionaries by enclosing comma-separated key-value pairs within curly braces `{}`.

```python
# Creating an empty dictionary
empty_dict = {}

# Creating a dictionary with elements
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
```

## Accessing Elements

You can access elements of a dictionary using square brackets `[]` and providing the key.

```python
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

print(my_dict["name"])   # Output: Alice
print(my_dict["age"])    # Output: 30
```

## Modifying Dictionaries

Dictionaries are mutable, so you can add, update, or remove key-value pairs.

```python
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# Adding a new key-value pair
my_dict["email"] = "alice@example.com"

# Updating an existing value
my_dict["age"] = 31

# Removing a key-value pair
del my_dict["city"]
```

## Dictionary Methods

Python provides several built-in methods for working with dictionaries, such as `keys()`, `values()`, `items()`, `get()`, `pop()`, `popitem()`, `clear()`, and more.

```python
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

keys = my_dict.keys()        # Returns a view of keys
values = my_dict.values()    # Returns a view of values
items = my_dict.items()      # Returns a view of key-value pairs

age = my_dict.get("age")     # Returns the value for the specified key, or None if the key is not found
my_dict.pop("city")          # Removes the specified key and returns its value
key, value = my_dict.popitem()   # Removes and returns an arbitrary key-value pair
my_dict.clear()              # Removes all key-value pairs from the dictionary
```

## Dictionary Comprehensions

Similar to list comprehensions, you can also create dictionaries using dictionary comprehensions.

```python
keys = ["a", "b", "c"]
values = [1, 2, 3]

my_dict = {k: v for k, v in zip(keys, values)}
```

## Advantages of Dictionaries

- **Fast Lookup**: Dictionaries provide fast lookups based on keys.
- **Flexible Key Types**: Keys can be of various immutable types, such as strings, numbers, or tuples.
- **Easy Data Retrieval**: Dictionaries make it easy to retrieve values based on keys without needing to know their positions.

## When to Use Dictionaries

- **Mapping**: Use dictionaries to store key-value mappings, such as user information, configurations, or any data with a unique identifier.
- **Data Aggregation**: Dictionaries are useful for aggregating data with named attributes.

Dictionaries are a powerful and versatile data structure in Python, offering efficient storage and retrieval of data based on keys. Understanding dictionaries and their operations is essential for writing clean and efficient Python code.
