
# Understanding `break` and `continue` in Python

## `break` Statement

**Definition:**  
The `break` statement is used to immediately exit a loop (like `for` or `while`) when a certain condition is met, even if the loop hasn't finished all its iterations.

**Example:**

```python
# Simple loop that counts from 1 to 5
for i in range(1, 6):
    if i == 3:  # When i is 3, break the loop
        break
    print(i)
```

**Output:**
```
1
2
```

**Explanation:**  
In this example, the loop is supposed to print numbers from 1 to 5. However, when `i` becomes `3`, the `break` statement stops the loop immediately, so it only prints `1` and `2`.

---

## `continue` Statement

**Definition:**  
The `continue` statement skips the rest of the code inside the loop for the current iteration and jumps to the next iteration of the loop.

**Example:**

```python
# Simple loop that counts from 1 to 5
for i in range(1, 6):
    if i == 3:  # When i is 3, skip the rest of the loop for this iteration
        continue
    print(i)
```

**Output:**
```
1
2
4
5
```

**Explanation:**  
In this example, the loop prints numbers from 1 to 5. But when `i` is `3`, the `continue` statement skips the print statement and moves to the next iteration. So, `3` is not printed.

---

## Summary
- **`break`:** Stops the loop completely.
- **`continue`:** Skips the rest of the current loop iteration and continues with the next one.

These statements are handy when you need to control the flow of loops based on specific conditions.
