
# Understanding Lambda Functions in Python

## What is a Lambda Function?

A **lambda function** in Python is a small, anonymous function that is defined using the `lambda` keyword. Unlike regular functions defined using `def`, lambda functions are typically used for short, simple operations. They can have any number of arguments but only one expression, which is evaluated and returned.

**Syntax:**
```python
lambda arguments: expression
```

## Simple Example

Let’s say you want to create a function that adds 10 to a number.

### Using a regular function:
```python
def add_ten(x):
    return x + 10

print(add_ten(5))  # Output: 15
```

### Using a lambda function:
```python
add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15
```

Both examples do the same thing, but the lambda function is more concise.

## Why Use Lambda Functions?

- **Conciseness:** Lambda functions are a quick way to write small, throwaway functions that are used in a short context.
- **Inline Usage:** They are often used as arguments to higher-order functions, such as `map()`, `filter()`, and `sorted()`, where defining a full function would be overkill.
- **Anonymous Functions:** When you don't need to reuse a function, defining it as a lambda can save time and space.

## Real-Time Example

Suppose you have a list of tuples representing products and their prices, and you want to sort this list by price.

**Example:**
```python
products = [("apple", 100), ("banana", 50), ("cherry", 75)]

# Sort by price using lambda
sorted_products = sorted(products, key=lambda x: x[1])

print(sorted_products)
```

**Output:**
```
[('banana', 50), ('cherry', 75), ('apple', 100)]
```

Here, the lambda function `lambda x: x[1]` is used to specify that the sorting should be based on the second item in each tuple (the price).

## Common Use Cases for Lambda Functions

1. **Sorting:** Sorting lists based on custom keys.
2. **Filtering:** Filtering data using conditions.
3. **Mapping:** Applying a function to each item in a list.
4. **In Functional Programming:** Used in conjunction with functions like `map()`, `filter()`, and `reduce()`.

### Example with `filter()`:
```python
numbers = [1, 2, 3, 4, 5, 6]

# Filter out even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)
```

**Output:**
```
[2, 4, 6]
```

## Interview Question

**Q:** What are lambda functions in Python, and how do they differ from regular functions?

**A:** Lambda functions in Python are anonymous functions defined with the `lambda` keyword. They can have multiple arguments but only one expression. Lambda functions are often used for short, simple operations where defining a full function would be unnecessary. Unlike regular functions defined with `def`, lambda functions are not given a name (hence "anonymous") and are typically used in a functional programming context, such as with `map()`, `filter()`, or `sorted()`.

## Exercise Questions

1. **Basic Lambda Function:**
   - Write a lambda function that multiplies a number by 2.
   - Example: `f(3)` should return `6`.

2. **Sorting with Lambda:**
   - Given a list of strings `["apple", "banana", "cherry"]`, write a lambda function to sort the list by the length of each string.

3. **Filtering with Lambda:**
   - Use a lambda function to filter out all the odd numbers from the list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`.

4. **Map with Lambda:**
   - Given a list `[1, 2, 3, 4, 5]`, write a lambda function using `map()` to square each number.

By practicing these exercises, you'll get more comfortable using lambda functions in various scenarios.
