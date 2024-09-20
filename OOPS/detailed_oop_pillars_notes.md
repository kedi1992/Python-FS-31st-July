
# OOP Pillars: Detailed Notes

---

## 1. Encapsulation

### What is Encapsulation?
Encapsulation is the technique of wrapping the data (variables) and the code acting on the data (methods) together as a single unit, usually in a class. It restricts access to some of an object’s components, which is a means of preventing unintended interference and misuse.

### Types of Encapsulation:
1. **Private Members**: Members are not accessible outside the class.
2. **Protected Members**: Members are accessible within the class and subclasses.
3. **Public Members**: Members are accessible from anywhere.

### Real-time Example:
In a **Banking System**, sensitive data such as account balance should not be directly accessed. Instead, methods such as `deposit()` and `withdraw()` provide controlled access to the balance.

```python
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.__balance
```

### Interview Questions on Encapsulation:
1. What is encapsulation and how is it implemented in Python?
2. Why do we use private and protected attributes in Python?
3. Can you provide a real-world example where encapsulation is necessary?

---

## 2. Abstraction

### What is Abstraction?
Abstraction means hiding the complexity and showing only the essential details to the user. In Python, abstraction can be achieved using abstract classes and interfaces.

### Types of Abstraction:
1. **Abstract Classes**: Classes that cannot be instantiated directly and require subclasses to implement the abstract methods.
2. **Interfaces**: Similar to abstract classes but focus purely on defining methods without implementation.

### Real-time Example:
In a **Payment System**, users only need to know about the `pay()` method without worrying about how different payment modes like credit card or PayPal are processed internally.

```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paying {amount} using credit card.")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paying {amount} using PayPal.")

payment = CreditCardPayment()
payment.pay(100)
```

### Interview Questions on Abstraction:
1. What is abstraction, and how is it different from encapsulation?
2. How does Python implement abstraction?
3. Give an example of abstraction in real-world software.

---

## 3. Inheritance

### What is Inheritance?
Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class). It promotes reusability and can be of different types.

### Types of Inheritance:
1. **Single Inheritance**: A child class inherits from a single parent class.
2. **Multiple Inheritance**: A child class can inherit from multiple parent classes.
3. **Multilevel Inheritance**: A class inherits from a parent class, which in turn inherits from another class.
4. **Hierarchical Inheritance**: Multiple child classes inherit from a single parent class.
5. **Hybrid Inheritance**: A combination of two or more types of inheritance.

### Real-time Example:
In an **Employee Management System**, all employees share common properties like `name` and `salary`, but managers may have additional responsibilities.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is working.")

class Manager(Employee):
    def work(self):
        print(f"{self.name} is managing the team.")

emp = Employee("John", 5000)
mgr = Manager("Sara", 10000)

emp.work()  # Output: John is working.
mgr.work()  # Output: Sara is managing the team.
```

### Interview Questions on Inheritance:
1. What are the different types of inheritance in Python?
2. Can you explain the difference between single and multiple inheritance?
3. How does Python handle method resolution in multiple inheritance?

---

## 4. Polymorphism

### What is Polymorphism?
Polymorphism allows different classes to be treated as instances of the same class through a common interface. It means "many forms" and refers to the ability to process objects differently depending on their class.

### Types of Polymorphism:
1. **Compile-Time (Overloading)**: Achieved through method overloading, which is not directly supported in Python but can be mimicked.
2. **Run-Time (Overriding)**: Achieved through method overriding, where a subclass overrides the method of its parent class.

### Real-time Example:
In a **Drawing Application**, different shapes such as circles and rectangles can have their own implementations of the `draw()` method, but they can all be used polymorphically.

```python
class Shape:
    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

def draw_shape(shape):
    shape.draw()

shapes = [Circle(), Rectangle()]
for shape in shapes:
    draw_shape(shape)
```

### Interview Questions on Polymorphism:
1. What is polymorphism and how is it implemented in Python?
2. What is the difference between method overloading and method overriding?
3. Give a real-world example of where polymorphism is useful.

---

## Summary
The four pillars of OOP — **Encapsulation**, **Abstraction**, **Inheritance**, and **Polymorphism** — are essential for writing modular, reusable, and efficient code. Understanding these concepts will help you model real-world entities in a more structured and logical manner.

- **Encapsulation** protects data from outside interference.
- **Abstraction** hides unnecessary details and simplifies the interface.
- **Inheritance** promotes code reuse by sharing common logic between classes.
- **Polymorphism** enables one interface to be used for different data types.

---
