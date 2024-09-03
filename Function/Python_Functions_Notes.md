
# Python Functions: A Detailed Guide

## 1. What is a Function in Python?
A function is a block of reusable code that performs a specific task. Functions help to make the code modular, organized, and easier to manage. Python provides many built-in functions like `print()`, `len()`, etc., but you can also define your own functions.

## 2. Why Use Functions?
- **Code Reusability:** Once a function is defined, it can be used multiple times without rewriting the code.
- **Modularity:** Functions allow you to break down complex problems into smaller, manageable parts.
- **Maintainability:** Code is easier to understand and modify when it’s organized into functions.
- **Testing:** Functions can be tested independently of the rest of the code.

## 3. Defining a Function
In Python, functions are defined using the `def` keyword, followed by the function name, parentheses, and a colon. The code block within every function starts with an indentation.

**Syntax:**
```python
def function_name(parameters):
    """docstring""" 
    # code block 
    return expression
```

- **function_name:** The name of the function.
- **parameters:** (Optional) The inputs to the function. A function can have no parameters or multiple parameters.
- **docstring:** (Optional) A string that describes what the function does.
- **return:** (Optional) Ends the function and optionally returns a value.

## 4. Example of a Simple Function
Here’s a simple example of a function that takes a number and returns its square:

```python
def square(num):
    """Returns the square of a number.""" 
    return num ** 2

# Calling the function
result = square(4)
print(result)  # Output: 16
```

## 5. Function Parameters and Arguments
- **Positional Arguments:** Arguments passed in the correct positional order.
- **Keyword Arguments:** Arguments passed in the form of key-value pairs.
- **Default Parameters:** Parameters that assume a default value if a value is not provided.
- **Variable-Length Arguments:** Using `*args` and `**kwargs`, you can pass a variable number of arguments to a function.

**Example:**
```python
def greet(name, msg="Hello"):
    """Greets a person with a message.""" 
    print(f"{msg}, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet("Bob", "Good Morning")  # Output: Good Morning, Bob!
```

## 6. Return Statement
The `return` statement is used to exit a function and return a value. If no return statement is provided, the function returns `None`.

**Example:**
```python
def add(a, b):
    """Returns the sum of two numbers.""" 
    return a + b

result = add(3, 5)
print(result)  # Output: 8
```

## 7. Scope of Variables
- **Local Scope:** Variables defined inside a function are local to that function.
- **Global Scope:** Variables defined outside any function have a global scope and can be accessed anywhere in the code.

**Example:**
```python
x = 10  # Global variable

def func():
    x = 5  # Local variable
    print(x)  # Output: 5

func()
print(x)  # Output: 10
```

## 8. Lambda Functions
A lambda function is a small anonymous function defined with the `lambda` keyword. It can take any number of arguments but only has one expression.

**Example:**
```python
square = lambda x: x ** 2
print(square(5))  # Output: 25
```

## 9. Exercises

**Exercise 1:** Write a function that checks if a number is prime.
```python
def is_prime(num):
    """Returns True if the number is prime, otherwise False.""" 
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
```

**Exercise 2:** Create a function that returns the factorial of a number.
```python
def factorial(n):
    """Returns the factorial of a number.""" 
    if n == 0:
        return 1
    return n * factorial(n-1)
```

**Exercise 3:** Write a function that finds the greatest common divisor (GCD) of two numbers.
```python
def gcd(a, b):
    """Returns the greatest common divisor of a and b.""" 
    while b:
        a, b = b, a % b
    return a
```

## 10. Important Interview Questions

1. **What is the difference between a function and a method?**
   - **Function:** A block of code that is executed when it is called. It is not bound to an object.
   - **Method:** A function that is associated with an object. It is called on an object and can access and modify the object’s data.

2. **What are decorators in Python?**
   - Decorators are a way to modify the behavior of a function or method. They are usually defined with the `@` symbol and are placed above the function definition.

3. **Explain *args and **kwargs in Python functions.**
   - `*args` is used to pass a variable number of positional arguments to a function.
   - `**kwargs` is used to pass a variable number of keyword arguments to a function.

4. **What is the difference between local and global variables?**
   - **Local variables** are those defined inside a function and are accessible only within that function.
   - **Global variables** are defined outside all functions and are accessible throughout the code.

5. **What is recursion?**
   - Recursion is a process where a function calls itself. It’s often used to solve problems that can be broken down into smaller, repetitive tasks. However, care must be taken to define a base case to prevent infinite recursion.
