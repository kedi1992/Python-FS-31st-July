
# Python `map()` and `filter()` Functions

## 1. `map()` Function

The `map()` function applies a given function to all items in an iterable (such as a list, tuple, etc.) and returns a map object (which is an iterator). The result can be converted into a list, tuple, or any other sequence type.

**Syntax:**
```python
map(function, iterable)
```

- **function**: A function that will be applied to each item in the iterable.
- **iterable**: One or more iterable objects (e.g., list, tuple).

### Example 1:
```python
def square(x):
    return x * x

numbers = [1, 2, 3, 4]
result = map(square, numbers)
print(list(result))  # Output: [1, 4, 9, 16]
```

### Example 2:
Using `lambda` with `map()`:
```python
numbers = [1, 2, 3, 4]
result = map(lambda x: x * x, numbers)
print(list(result))  # Output: [1, 4, 9, 16]
```

### Multiple Iterables Example:
```python
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))  # Output: [5, 7, 9]
```

## 2. `filter()` Function

The `filter()` function filters elements from an iterable based on a function that returns either `True` or `False`. Only the items for which the function returns `True` are included in the result.

**Syntax:**
```python
filter(function, iterable)
```

- **function**: A function that evaluates to either `True` or `False`.
- **iterable**: The iterable to be filtered.

### Example 1:
```python
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
result = filter(is_even, numbers)
print(list(result))  # Output: [2, 4, 6]
```

### Example 2:
Using `lambda` with `filter()`:
```python
numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x > 3, numbers)
print(list(result))  # Output: [4, 5, 6]
```

## Key Differences

- `map()` transforms all elements of an iterable based on a function.
- `filter()` selects elements from an iterable that satisfy a condition (i.e., where the function returns `True`).

## Real-Time Use Cases:

1. **`map()` in Data Transformation**:
   - Converting temperature from Celsius to Fahrenheit for a list of temperature readings.
   - Applying a discount to a list of prices.

2. **`filter()` in Data Filtering**:
   - Filtering out students who passed a test (marks greater than a certain threshold).
   - Filtering out odd numbers from a list of integers.

## Interview Questions:

1. What is the difference between `map()` and `filter()`?
2. Can you use `map()` and `filter()` together in Python? Provide an example.
3. How would you use the `filter()` function to remove empty strings from a list?

## Exercises:

1. Write a Python program using `map()` to convert a list of strings into uppercase.
2. Use `filter()` to find all words longer than 3 characters from a list of words.
3. Combine `map()` and `filter()` to first filter even numbers from a list and then square them.
