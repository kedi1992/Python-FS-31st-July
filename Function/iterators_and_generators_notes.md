
# Python Iterators and Generators

## **Iterators**

### What are Iterators?
- An **iterator** is an object that allows you to traverse through all elements of a collection (like a list or a string).
- The main methods involved are:
  - `__iter__()`: Returns the iterator object itself.
  - `__next__()`: Returns the next element from the collection.

### Simplest Example:
```python
# List as an iterable
my_list = [1, 2, 3]

# Getting an iterator object from the list
my_iter = iter(my_list)

# Using next() to access elements one by one
print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
print(next(my_iter))  # Output: 3
```

### Key Points:
- When there are no more elements, `next()` will raise a `StopIteration` error, signaling the end of the iteration.

### Simplified Hands-on Exercise:
```python
# Create a simple iterator for a string
my_string = "hello"

# Get iterator object
my_string_iter = iter(my_string)

# Iterate through characters one by one
print(next(my_string_iter))  # Output: 'h'
print(next(my_string_iter))  # Output: 'e'
```

---

## **Generators**

### What are Generators?
- A generator is a simpler way to create an iterator using a function.
- Generators use the `yield` keyword to produce one value at a time and remember the state between `yield` calls.

### Simplest Example:
```python
def my_generator():
    yield 1
    yield 2
    yield 3

# Create generator object
gen = my_generator()

# Use next() to get the values one by one
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
```

### Key Points:
- Each time `next()` is called, the generator resumes from where it left off, producing the next value.
- Generators are memory efficient because they generate items one at a time instead of storing them all at once.

### Simplified Hands-on Exercise:
```python
# A simple generator to produce squares of numbers
def square_generator(n):
    for i in range(1, n+1):
        yield i * i

# Create generator and print the square of numbers from 1 to 3
gen = square_generator(3)
print(next(gen))  # Output: 1
print(next(gen))  # Output: 4
print(next(gen))  # Output: 9
```

---

## **Interview Questions**

1. **What is an iterator?**
   - An iterator is an object that lets you loop through items in a collection like a list, one by one.

2. **What is a generator?**
   - A generator is a type of iterator you define with a function using the `yield` keyword to generate values on the fly.

3. **What is the difference between `return` and `yield`?**
   - `return` sends back a single value and ends the function, while `yield` produces a value and pauses the function, allowing it to continue from where it left off.
