#### [Return Back](../../python_for_testers.md)

# Inheritance

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (subclass) to inherit attributes and methods from another class (superclass). This enables code reusability and the creation of hierarchical relationships between classes. Here's an overview of inheritance in Python:

## Basic Inheritance Syntax

In Python, inheritance is achieved by passing the name of the superclass inside parentheses when defining a subclass.

```python
class ParentClass:
    # Superclass definition
    pass

class ChildClass(ParentClass):
    # Subclass definition
    pass
```

## Accessing Superclass Methods

A subclass inherits all attributes and methods of its superclass. It can access superclass methods using the `super()` function.

```python
class ParentClass:
    def greet(self):
        return "Hello from ParentClass"

class ChildClass(ParentClass):
    def greet(self):
        # Call superclass method
        return super().greet() + ", and also from ChildClass"

child_obj = ChildClass()
print(child_obj.greet())  # Output: Hello from ParentClass, and also from ChildClass
```

## Overriding Methods

A subclass can override superclass methods by redefining them in the subclass. This allows customization of behavior specific to the subclass.

```python
class ParentClass:
    def greet(self):
        return "Hello from ParentClass"

class ChildClass(ParentClass):
    def greet(self):
        # Override superclass method
        return "Hello from ChildClass"

child_obj = ChildClass()
print(child_obj.greet())  # Output: Hello from ChildClass
```

## Adding New Methods

A subclass can also define new methods that are not present in the superclass. These methods are specific to the subclass and do not affect the superclass.

```python
class ParentClass:
    def greet(self):
        return "Hello from ParentClass"

class ChildClass(ParentClass):
    def greet_child(self):
        return "Hello from ChildClass"

child_obj = ChildClass()
print(child_obj.greet_child())  # Output: Hello from ChildClass
```

## Multiple Inheritance

Python supports multiple inheritance, where a subclass can inherit attributes and methods from multiple superclasses. This is achieved by passing multiple superclass names inside parentheses when defining the subclass.

```python
class SuperClass1:
    # Superclass 1 definition
    pass

class SuperClass2:
    # Superclass 2 definition
    pass

class SubClass(SuperClass1, SuperClass2):
    # Subclass definition inheriting from SuperClass1 and SuperClass2
    pass
```

## Key Points

- Inheritance allows a subclass to inherit attributes and methods from a superclass.
- A subclass can access superclass methods using `super()` and override superclass methods by redefining them.
- New methods can be added to a subclass, which are specific to the subclass.
- Python supports multiple inheritance, where a subclass can inherit from multiple superclasses.
- The Method Resolution Order (MRO) defines the order in which Python searches for methods and attributes in classes.

Understanding inheritance is essential for creating modular and reusable code in Python, as it promotes code reuse and enhances maintainability.
