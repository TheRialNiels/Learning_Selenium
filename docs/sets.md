#### [Return Back](../python_for_testers.md)

# Sets

A set is an unordered collection of unique elements. Sets are mutable, meaning you can add or remove elements from them, but they do not support indexing or slicing like lists. Sets are commonly used for membership testing and eliminating duplicate entries.

## Creating Sets

You can create sets by enclosing comma-separated elements within curly braces `{}`.

```python
# Creating an empty set
empty_set = set()

# Creating a set with elements
my_set = {1, 2, 3, 4, 5}

# Creating a set from a list
my_set_from_list = set([1, 2, 3, 4, 5])
```

## Accessing Elements

Since sets are unordered, you cannot access elements by index. However, you can check for membership using the `in` operator.

```python
my_set = {1, 2, 3, 4, 5}

print(3 in my_set)  # Output: True
print(6 in my_set)  # Output: False
```

## Modifying Sets

Sets are mutable, so you can add or remove elements from them using methods like `add()`, `remove()`, `discard()`, and `clear()`.

```python
my_set = {1, 2, 3, 4, 5}

my_set.add(6)       # Adds an element to the set
my_set.remove(3)    # Removes the specified element
my_set.discard(4)   # Removes the specified element if present
my_set.clear()      # Removes all elements from the set
```

## Set Operations

Sets support various operations such as union, intersection, difference, and symmetric difference.

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set = set1 | set2           # Union
intersection_set = set1 & set2    # Intersection
difference_set = set1 - set2      # Difference
symmetric_difference_set = set1 ^ set2  # Symmetric difference
```

## Set Methods

Python provides several built-in methods for working with sets, such as `add()`, `remove()`, `discard()`, `clear()`, `union()`, `intersection()`, `difference()`, `symmetric_difference()`, and more.

```python
my_set = {1, 2, 3}

my_set.add(4)                   # Adds an element to the set
my_set.remove(2)                # Removes the specified element
my_set.discard(3)               # Removes the specified element if present
my_set.clear()                  # Removes all elements from the set
union_set = my_set.union({4, 5})    # Returns the union of two sets
intersection_set = my_set.intersection({3, 4, 5})  # Returns the intersection of two sets
```

## Set Comprehensions

Similar to list comprehensions, you can also create sets using set comprehensions.

```python
numbers = {1, 2, 3, 4, 5}

squared_numbers = {x**2 for x in numbers}
even_numbers = {x for x in numbers if x % 2 == 0}
```

Sets are useful for various tasks such as removing duplicates from a list, testing membership, and performing set operations efficiently. Understanding sets and their operations is important for writing clean and efficient Python code.
