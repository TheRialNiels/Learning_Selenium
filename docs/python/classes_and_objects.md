#### [Return Back](../../python_for_testers.md)

# Classes

A class is a blueprint for creating objects. It defines the attributes (data) and methods (functions) that the objects of the class will have.

### Defining a Class

You define a class using the `class` keyword followed by the class name:

```python
class MyClass:
    # Class definition
    pass
```

### Constructor Method (`__init__`)

The `__init__` method is a special method called the constructor. It is executed automatically when a new object is created and is used to initialize the object's attributes.

```python
class MyClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
```

### Attributes and Methods

- **Attributes**: Variables associated with objects (also called instance variables).
- **Methods**: Functions associated with objects (also called instance methods).

```python
class MyClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def method1(self):
        return self.attribute1 + self.attribute2
```

# Objects

An object is an instance of a class. It represents a specific realization of the class blueprint, with its own unique data and behavior.

### Creating Objects

You create objects by calling the class name followed by parentheses `()`:

```python
obj1 = MyClass(10, 20)
```

### Accessing Attributes and Calling Methods

You can access object attributes and call methods using the dot (`.`) notation:

```python
print(obj1.attribute1)   # Output: 10
print(obj1.method1())    # Output: 30
```

## Inheritance

Inheritance is a feature of OOP that allows a class (subclass) to inherit attributes and methods from another class (superclass). The subclass can then extend or override the functionality of the superclass.

```python
class ChildClass(ParentClass):
    # Class definition
    pass
```

## Encapsulation

Encapsulation is the bundling of data (attributes) and methods that operate on the data into a single unit (class). It hides the internal implementation details of the class from the outside world, and only exposes a public interface for interacting with the class.

## Polymorphism

Polymorphism is the ability of objects to take on different forms or behaviors based on the context. It allows different classes to be treated as instances of the same class through inheritance and method overriding.

## Abstraction

Abstraction is the process of hiding the complex implementation details of a class and exposing only the necessary features and functionalities to the user. It helps in managing complexity and enhancing code readability.

## Key Points

- Classes are blueprints for creating objects, while objects are instances of classes.
- Classes encapsulate data (attributes) and behavior (methods) into a single unit.
- Inheritance allows classes to inherit attributes and methods from other classes.
- Encapsulation, polymorphism, and abstraction are key principles of OOP that help in designing modular, maintainable, and reusable code.

Understanding objects and classes is essential for building complex and scalable applications in Python using the principles of OOP.
