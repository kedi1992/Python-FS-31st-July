
# The Four Pillars of Object-Oriented Programming (OOP)

Object-Oriented Programming (OOP) is a programming paradigm that provides a way to structure and organize software using objects and classes. The four key concepts (pillars) of OOP are: **Encapsulation**, **Abstraction**, **Inheritance**, and **Polymorphism**.

---

## 1. Encapsulation

- **Encapsulation** refers to the practice of bundling data (attributes) and methods (functions) that operate on the data into a single unit, i.e., a class.
- It also involves restricting access to some of an object's components to protect the integrity of that data.

### Benefits of Encapsulation:
- **Data Protection**: It hides sensitive data and only exposes necessary parts.
- **Controlled Access**: Data is accessible only through public methods, known as **getters** and **setters**.
- **Modularity**: The class can be modified internally without affecting external code.

### Example:

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name          # Public attribute
        self.__salary = salary     # Private attribute

    def get_salary(self):
        return self.__salary       # Getter method for private attribute

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary # Setter method for private attribute
        else:
            print("Invalid salary!")

# Creating an object of Employee
emp = Employee("John", 5000)
print(emp.name)           # Public access
print(emp.get_salary())   # Access private attribute via getter

emp.set_salary(6000)      # Setting a new salary via setter
```

---

## 2. Abstraction

- **Abstraction** refers to showing only the essential details of an object and hiding the unnecessary implementation.
- It helps reduce complexity and allows the user to interact with objects at a higher level.

### Benefits of Abstraction:
- **Simplicity**: It makes the code easier to use and understand by hiding complex logic.
- **Flexibility**: Internal changes to a class won't affect code that uses the class, as long as the interface remains consistent.

### Example:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create an object of Rectangle and calculate area
rect = Rectangle(10, 5)
print(f"Area of rectangle: {rect.area()}")
```

---

## 3. Inheritance

- **Inheritance** allows one class (child class) to inherit attributes and methods from another class (parent class).
- This promotes **code reusability** and establishes a relationship between classes.

### Benefits of Inheritance:
- **Reusability**: You can reuse fields and methods of the existing class in a new class.
- **Extensibility**: You can add or modify functionalities in the child class without changing the parent class.

### Example:

```python
class Animal:
    def sound(self):
        print("This animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("The dog barks")

# Inheritance in action
my_dog = Dog()
my_dog.sound()  # Output: The dog barks
```

---

## 4. Polymorphism

- **Polymorphism** allows objects of different classes to be treated as objects of a common superclass.
- It refers to the ability to use a method in different ways for different objects, allowing flexibility in the code.

### Benefits of Polymorphism:
- **Flexibility**: One method can be applied to different types of objects.
- **Extensibility**: You can introduce new classes that implement the same methods in different ways.

### Example:

```python
class Bird:
    def fly(self):
        print("Some birds can fly.")

class Sparrow(Bird):
    def fly(self):
        print("Sparrows fly fast.")

class Ostrich(Bird):
    def fly(self):
        print("Ostriches can't fly.")

# Polymorphism in action
def flying_bird(bird):
    bird.fly()

sparrow = Sparrow()
ostrich = Ostrich()

flying_bird(sparrow)  # Output: Sparrows fly fast.
flying_bird(ostrich)  # Output: Ostriches can't fly.
```

---

## Summary

- **Encapsulation**: Hides data and allows controlled access.
- **Abstraction**: Simplifies code by showing only essential details.
- **Inheritance**: Allows classes to reuse code from other classes.
- **Polymorphism**: Enables methods to work differently based on the object calling them.

These concepts allow us to write efficient, scalable, and reusable code, making it easier to model real-world systems and processes in programming.

---
