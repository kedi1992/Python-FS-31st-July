
# Python OOP (Object-Oriented Programming) Notes

## 1. What is OOP?
- Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects" containing data (attributes) and code (methods).
- **Four main principles**:
  - **Encapsulation**: Binding data and methods together, restricting access to internal states.
  - **Inheritance**: Creating new classes from existing ones, inheriting attributes and methods.
  - **Polymorphism**: Same interface can be used for different data types.
  - **Abstraction**: Hiding complex implementation details, showing only necessary features.

## 2. Classes and Objects
- **Class**: A blueprint for creating objects.
- **Object**: An instance of a class.

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f'Car: {self.brand} {self.model} ({self.year})')

my_car = Car('Toyota', 'Corolla', 2022)
my_car.display_info()
```

## 3. Constructor (`__init__` method)
- Special method called automatically when an object is instantiated, used to initialize object attributes.

## 4. Inheritance
- One class inherits attributes and methods from another class.

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f'{self.brand} is starting')

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_info(self):
        print(f'{self.brand} {self.model}')
        
my_car = Car('Toyota', 'Camry')
my_car.display_info()
my_car.start()
```

## 5. Polymorphism
- Allows different objects to be accessed through the same interface, using their own implementation.

```python
class Dog:
    def sound(self):
        print("Bark")
        
class Cat:
    def sound(self):
        print("Meow")

for animal in (Dog(), Cat()):
    animal.sound()
```

## 6. Encapsulation
- Hides the internal state and restricts access to it using private attributes.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def check_balance(self):
        return self.__balance
```

## 7. Abstraction
- Hides complex internal logic, providing only necessary interfaces.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

dog = Dog()
dog.sound()
```

---

# Hands-On Exercises

### Exercise 1: Define a Library Class
Create a class `Library` with attributes and methods for borrowing, returning, and displaying books.

```python
class Library:
    def __init__(self, books):
        self.books = books

    def display_books(self):
        for book in self.books:
            print(book)

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print("Book not available")

    def return_book(self, book):
        self.books.append(book)
```

### Exercise 2: Inheritance Example
Create an `Employee` class and a `Manager` class that inherits from it, adding a method to manage a team.

---

# Interview Questions

1. **What is the difference between a class and an object?**
2. **Explain inheritance in Python.**
3. **What is encapsulation in OOP?**
4. **How does Python support polymorphism?**
5. **What is an abstract class?**
6. **What are dunder/magic methods in Python?**
