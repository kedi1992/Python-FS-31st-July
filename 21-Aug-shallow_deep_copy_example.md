
# Python Shallow Copy and Deep Copy Example

Here's a detailed Python example with notes on shallow copy, deep copy, and assignment.

```python
# Initial List
d1 = [10, 20, 30]

# Case 1: Assignment (Not a Copy, Just Reference)
d2 = d1  # Both d1 and d2 point to the same list in memory

print("Case 1: Assignment")
print(f"Before modification:\nd1: {d1}\nd2: {d2}")

d2[0] = 200  # This change affects both d1 and d2 since they refer to the same list
print(f"After modification:\nd1: {d1}\nd2: {d2}\n")
# Both d1 and d2 will be modified.

# Case 2: Shallow Copy using the `copy` method of the list
d1 = [10, 20, 30]  # Reset d1 for a clean slate
d2 = d1.copy()  # Creates a shallow copy

print("Case 2: Shallow Copy using copy()")
print(f"Before modification:\nd1: {d1}\nd2: {d2}")

d2[0] = 200  # Only d2 changes, as it's a new list in memory
print(f"After modification:\nd1: {d1}\nd2: {d2}\n")
# d1 remains unchanged, as it's a shallow copy (but only for non-nested structures).

# Case 3: Shallow Copy using `copy.copy`
import copy
d1 = [10, 20, 30]  # Reset d1 for a clean slate
d2 = copy.copy(d1)  # Shallow copy using copy.copy()

print("Case 3: Shallow Copy using copy.copy()")
print(f"Before modification:\nd1: {d1}\nd2: {d2}")

d2[1] = 200  # Again, only d2 changes because it’s a shallow copy
print(f"After modification:\nd1: {d1}\nd2: {d2}\n")
# Same result as using d1.copy(), but this is more explicit.

# Case 4: Deep Copy (Handles Nested Structures)
d1 = [10, 20, [30, 40]]  # List with nested list
d2 = copy.deepcopy(d1)  # Deep copy

print("Case 4: Deep Copy using copy.deepcopy()")
print(f"Before modification:\nd1: {d1}\nd2: {d2}")

d1[2][0] = 999  # Modifying the nested list in d1
print(f"After modification:\nd1: {d1}\nd2: {d2}")
# In deep copy, d2 remains unchanged even after modifying nested elements in d1.
```

## Notes:

1. **Assignment (`d2 = d1`)**:
   - This doesn't create a new list; instead, `d2` becomes a reference to the same list as `d1`. Any modification to `d2` will reflect in `d1`, and vice versa, because both refer to the same memory location.
   
2. **Shallow Copy (`d2 = d1.copy()` or `copy.copy(d1)`)**:
   - Creates a new list but does not recursively copy objects within the list. If the list contains other objects (like nested lists), the inner objects will still be shared between `d1` and `d2`.
   
3. **Deep Copy (`d2 = copy.deepcopy(d1)`)**:
   - Creates a completely new list, including recursively copying all nested objects. Changes to any part of `d1` won't affect `d2`.

In your nested list example (`d1 = [10, 20, [30, 40]]`), a deep copy ensures that even the nested list `[30, 40]` is duplicated, so modifications to `d1`'s nested list won’t impact `d2`.
