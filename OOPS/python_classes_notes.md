
# Python Classes - Detailed Notes for Beginners

## Why Do We Need Classes in Python?

- **Organization**: As programs grow larger, it becomes difficult to manage the code. Classes help to organize code by grouping related data and functions together.
- **Reusability**: Once a class is created, you can create multiple objects (instances) from that class, which allows you to reuse code efficiently.
- **Encapsulation**: Classes allow you to bundle data (properties) and behavior (methods) into one logical unit. This protects data and ensures it is only manipulated in valid ways.

## What is a Class?

- A **class** is a blueprint or template for creating objects.
- It defines **properties** (also known as attributes or fields) and **methods** (functions) that objects created from the class will have.

### Example of a Class

```python
class Car:
    # Properties (Attributes)
    wheels = 4
    color = 'red'

    # Methods (Behavior)
    def start(self):
        print("Car is starting...")
```

Here, the `Car` class has two attributes (`wheels`, `color`) and a method (`start`).

## Internal Structure of a Class

### Properties (Attributes)
- These are variables that belong to a class or an object.
- In the example above, `wheels` and `color` are attributes of the `Car` class.

### Methods (Functions)
- These are functions defined inside a class that represent the behavior of the object.
- The `start()` method in the `Car` class represents the action of starting the car.

### Constructor
- A constructor is a special method called when an object is created.
- In Python, the constructor is the `__init__()` method.
- Example:

```python
class Car:
    def __init__(self, color):
        self.color = color  # Instance attribute

    def start(self):
        print(f"The {self.color} car is starting...")
```

In this example, `__init__()` sets the color of the car when the object is created.

## What is an Object?

- An **object** is an instance of a class. It is the actual entity created using the class template.
- When you create an object, Python allocates memory for the object and runs its `__init__()` method (if defined).

### Example of Creating an Object

```python
# Creating an object from the Car class
my_car = Car("blue")
my_car.start()  # Output: The blue car is starting...
```

Here, `my_car` is an object (or instance) of the `Car` class. It has its own `color` property.

## How to Create Properties in a Class

- **Class Attributes**: These are attributes that are shared across all instances of the class.
- **Instance Attributes**: These are attributes unique to each object.

```python
class Dog:
    species = 'Canine'  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute

# Usage
dog1 = Dog("Buddy")
dog2 = Dog("Charlie")

print(dog1.species)  # Canine (shared)
print(dog1.name)     # Buddy (unique)
```

## Behavior of Class/Object

- **Class Behavior**: Defined by the methods in the class.
- **Object Behavior**: Objects created from a class inherit the class’s behavior, but they can also have their own specific behavior.

### Example

```python
class Animal:
    def sound(self):
        print("This animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("The dog barks")

# Object behavior
my_dog = Dog()
my_dog.sound()  # Output: The dog barks
```

## Real-Time Example of Classes

Consider a **Bank Account**:

### Class Definition

```python
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number  # Instance attribute
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient funds.")

# Creating an object
my_account = BankAccount("123456789", 100)
my_account.deposit(50)    # Deposited 50. New balance is 150.
my_account.withdraw(30)   # Withdrew 30. New balance is 120.
```

### Explanation
- The `BankAccount` class has two attributes (`account_number`, `balance`) and two methods (`deposit()`, `withdraw()`).
- When you create an object (like `my_account`), you can deposit and withdraw money, which changes the state of the account.

## Summary

- **Class**: Blueprint for creating objects.
- **Object**: Instance of a class.
- **Attributes**: Data or properties of a class/object.
- **Methods**: Functions defining behavior of the class/object.
- **Constructor**: Special method (`__init__`) that initializes object properties.
- **Reusability**: Classes allow you to create multiple objects without duplicating code.

By using classes, we can organize our code, make it reusable, and model real-world objects in a simple and effective way.
