
# Python If-Else Statements

Conditional statements in Python allow you to control the flow of execution depending on certain conditions. The main types of conditional statements are:
1. **if statement**
2. **if-else statement**
3. **elif statement**
4. **Nested if-else statement**

## 1. if Statement
The `if` statement is used to test a condition. If the condition is `True`, the code inside the `if` block is executed.

### Syntax:
```python
if condition:
    # Code to execute if the condition is True
```

### Example:
```python
age = 18
if age >= 18:
    print("You are eligible to vote.")
```

## 2. if-else Statement
The `if-else` statement provides an alternate path of execution when the condition is `False`.

### Syntax:
```python
if condition:
    # Code to execute if the condition is True
else:
    # Code to execute if the condition is False
```

### Example:
```python
age = 16
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

## 3. elif Statement
The `elif` (short for "else if") allows for multiple conditions to be checked in sequence.

### Syntax:
```python
if condition1:
    # Code to execute if condition1 is True
elif condition2:
    # Code to execute if condition2 is True
else:
    # Code to execute if both conditions are False
```

### Example:
```python
marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")
```

## 4. Nested if-else Statement
You can place an `if-else` statement inside another `if` or `else` block, which is known as nesting.

### Syntax:
```python
if condition1:
    if condition2:
        # Code to execute if both condition1 and condition2 are True
    else:
        # Code to execute if condition1 is True but condition2 is False
else:
    # Code to execute if condition1 is False
```

### Example:
```python
num = 10
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Negative number")
```

---

# Exercises for Students

## Exercise 1: Check Even or Odd
Write a Python program that checks whether a given number is even or odd using an `if-else` statement.

```python
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")
```

## Exercise 2: Find the Largest Number
Write a program that takes three numbers as input and finds the largest one using `if-elif-else`.

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print(a, "is the largest")
elif b > a and b > c:
    print(b, "is the largest")
else:
    print(c, "is the largest")
```

## Exercise 3: Check Leap Year
Write a program that checks whether a given year is a leap year or not.

```python
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
```

---

# Interview Questions on If-Else Statements

## 1. What is the difference between an `if` statement and an `if-else` statement?
   - An `if` statement only executes the code when the condition is `True`. An `if-else` statement provides an alternative block of code to execute when the condition is `False`.

## 2. Can you use multiple `if` statements without using `else` or `elif`?
   - Yes, you can use multiple `if` statements without `else` or `elif`. Each `if` statement is evaluated independently. However, using `elif` is more efficient when conditions are related because it stops checking once a condition is `True`.

## 3. What is the purpose of the `elif` keyword in Python?
   - The `elif` keyword allows you to test multiple conditions sequentially. Once a condition evaluates to `True`, the corresponding block of code is executed, and the rest of the conditions are skipped.

## 4. What are nested `if-else` statements?
   - Nested `if-else` statements occur when an `if` or `else` block contains another `if-else` statement. This allows for multiple levels of condition checking.

## 5. Is it possible to have multiple `else` blocks in a single `if` statement?
   - No, an `if` statement can have only one `else` block. However, you can use multiple `if-elif` blocks followed by a single `else`.
