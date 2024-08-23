
# Python Loops

Loops in Python allow executing a block of code repeatedly. The two main types of loops are:

1. **For Loop**
2. **While Loop**

## 1. For Loop
The `for` loop in Python is used to iterate over a sequence (list, tuple, dictionary, set, or string).

### Syntax:
```python
for element in sequence:
    # Code to execute
```

### Example:
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### Range in For Loop:
`range()` is used to generate a sequence of numbers.

```python
for i in range(5):  # Prints numbers from 0 to 4
    print(i)
```

## 2. While Loop
The `while` loop executes as long as a condition is true.

### Syntax:
```python
while condition:
    # Code to execute
```

### Example:
```python
count = 1
while count <= 5:
    print("Count:", count)
    count += 1
```

## Control Statements in Loops

1. **break:** Exits the loop when a condition is met.
   ```python
   for i in range(5):
       if i == 3:
           break
       print(i)
   ```

2. **continue:** Skips the current iteration and moves to the next.
   ```python
   for i in range(5):
       if i == 3:
           continue
       print(i)
   ```

3. **else in loops:** An `else` block can be used with loops. The `else` block is executed when the loop completes its iterations.
   ```python
   for i in range(5):
       print(i)
   else:
       print("Loop finished")
   ```

## Nested Loops
You can place one loop inside another. The inner loop completes all iterations for each iteration of the outer loop.

### Example:
```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

---

# Exercises for Students

## Exercise 1: Sum of numbers from 1 to 100
Write a Python program using a `for` loop to calculate the sum of numbers from 1 to 100.

```python
total = 0
for i in range(1, 101):
    total += i
print("Sum:", total)
```

## Exercise 2: Multiplication Table
Write a program that prints the multiplication table of a number input by the user.

```python
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, 'x', i, '=', num * i)
```

## Exercise 3: Count Vowels in a String
Write a Python program to count the number of vowels in a given string.

```python
string = "This is a test string"
vowels = 'aeiouAEIOU'
count = 0
for char in string:
    if char in vowels:
        count += 1
print("Number of vowels:", count)
```

---

# Interview Questions on Loops

## 1. What is the difference between a `for` loop and a `while` loop in Python?
   - A `for` loop is used to iterate over a sequence (like a list, tuple, or string) and executes for a predefined number of iterations.
   - A `while` loop is used when the number of iterations is unknown and depends on a condition. The loop executes as long as the condition is true.

## 2. How does the `break` statement work in a loop?
   - The `break` statement is used to exit a loop when a certain condition is met. Once the `break` statement is executed, the control exits the loop entirely.

## 3. Explain the use of the `else` block with loops in Python.
   - The `else` block in a loop executes after the loop has completed its iterations. However, if the loop is terminated using the `break` statement, the `else` block will not be executed.

## 4. Can a loop have multiple `else` blocks?
   - No, a loop can only have one `else` block. However, it can contain multiple `if-elif-else` statements within the loop body.

## 5. How do you iterate over a dictionary in Python?
   - You can iterate over a dictionary by using the `items()`, `keys()`, or `values()` methods:
   ```python
   dictionary = {'a': 1, 'b': 2, 'c': 3}
   for key, value in dictionary.items():
       print(key, value)
   ```
