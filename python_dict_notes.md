
# Python `dict` Data Type

A `dict` in Python is an unordered collection of items. Each item in a dictionary is a key-value pair. Dictionaries are mutable, which means they can be changed after creation. The keys in a dictionary must be unique and immutable, while values can be of any data type.

## Creating a Dictionary

```python
# Empty dictionary
my_dict = {}

# Dictionary with integer keys
my_dict = {1: 'apple', 2: 'banana'}

# Dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}
```

## Accessing Dictionary Elements

```python
# Using key to access value
print(my_dict['name'])  # Output: John

# Using get() method
print(my_dict.get(1))  # Output: [2, 4, 3]
```

## Dictionary Methods

1. **`clear()`**: Removes all items from the dictionary.
   ```python
   my_dict.clear()
   ```

2. **`copy()`**: Returns a shallow copy of the dictionary.
   ```python
   new_dict = my_dict.copy()
   ```

3. **`fromkeys(seq, value)`**: Creates a new dictionary with keys from `seq` and values set to `value`.
   ```python
   keys = ('a', 'b', 'c')
   value = 1
   new_dict = dict.fromkeys(keys, value)
   ```

4. **`get(key, default)`**: Returns the value for `key` if `key` is in the dictionary; else `default`.
   ```python
   print(my_dict.get('name', 'Default'))  # Output: John
   ```

5. **`items()`**: Returns a view object containing key-value pairs.
   ```python
   print(my_dict.items())  # Output: dict_items([('name', 'John'), (1, [2, 4, 3])])
   ```

6. **`keys()`**: Returns a view object containing the keys.
   ```python
   print(my_dict.keys())  # Output: dict_keys(['name', 1])
   ```

7. **`pop(key, default)`**: Removes the item with the specified `key` and returns its value.
   ```python
   my_dict.pop('name')  # Removes and returns 'John'
   ```

8. **`popitem()`**: Removes and returns the last inserted key-value pair.
   ```python
   my_dict.popitem()  # Output: ('name', 'John')
   ```

9. **`setdefault(key, default)`**: Inserts `key` with `default` value if the key is not in the dictionary.
   ```python
   my_dict.setdefault('age', 25)
   ```

10. **`update([other_dict])`**: Updates the dictionary with elements from another dictionary or an iterable of key-value pairs.
    ```python
    my_dict.update({'age': 30})
    ```

11. **`values()`**: Returns a view object containing the values.
    ```python
    print(my_dict.values())  # Output: dict_values([30])
    ```

## Dictionary Operations

- **Check if a key exists**:
  ```python
  if 'name' in my_dict:
      print("Name exists")
  ```

- **Iterating over a dictionary**:
  ```python
  for key, value in my_dict.items():
      print(key, value)
  ```

- **Deleting an item**:
  ```python
  del my_dict['name']
  ```

## Examples

### Nested Dictionary

```python
student = {
    'name': 'John',
    'marks': {'math': 90, 'science': 95}
}
print(student['marks']['math'])  # Output: 90
```

### Dictionary Comprehension

```python
squares = {x: x*x for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## Real-Time Use Cases

- **Configuration Settings**: Storing settings in a config file.
- **Counting Frequency**: Use a dictionary to count the occurrences of items in a list.
   ```python
   from collections import Counter
   freq_dict = Counter([1, 2, 2, 3, 3, 3])
   ```

# Hash Algorithm and Hash Collision in Python Dictionaries

## Hash Algorithm in Dictionaries

Python dictionaries use a hash table internally to store data. A **hash function** is used to convert a key into an integer (called the hash value or hash code). This hash value is then used to index the key-value pair into a specific location in the hash table.

- **Hashing Process**: When you insert or retrieve a key-value pair, Python’s hash function (internally `hash()`) computes the hash value of the key. This value determines the index where the key-value pair will be stored in the hash table.

Example:
```python
my_dict = {'name': 'Alice', 'age': 30}
hash_value = hash('name')
print(hash_value)
```

## Hash Collision

A **hash collision** occurs when two distinct keys are hashed to the same index in the hash table. In other words, even though two keys are different, their hash values are the same. Since dictionaries rely on unique hash values for quick lookups, collisions can pose challenges.

To handle hash collisions, Python uses **collision resolution strategies**. The two main techniques are:

1. **Open Addressing (Linear Probing)**: When a collision occurs, Python looks for the next available slot in the hash table.
   
2. **Chaining**: Instead of looking for another slot, Python stores multiple key-value pairs in the same slot using a linked list.

Python uses **chaining** for handling hash collisions.

Example:
```python
# Two keys with different values, but Python handles the collision internally.
my_dict = {'key1': 'value1', 'key2': 'value2'}
print(hash('key1') % 8)  # Simulating hash table with size 8
print(hash('key2') % 8)  # These may result in the same index, causing a collision.
```

## Impact of Hash Collision

- Hash collisions can slow down the performance of a dictionary since multiple keys will be stored in the same index.
- However, Python's efficient implementation of hash tables minimizes this impact by ensuring collisions are rare and handled efficiently.

## Avoiding Hash Collisions

1. **Good Hash Functions**: Python’s built-in hash function is designed to minimize collisions. Using immutable and unique keys (like integers or strings) helps reduce the chances of collisions.
2. **Table Size**: The size of the hash table is automatically resized in Python, helping to reduce the likelihood of collisions.

## Real-World Example of Hash Collision

Imagine two students have different names, but due to some hash function's calculation, their names hash to the same location in a school's dictionary database. Python will handle this using chaining to ensure both students' data is stored correctly.

# Interview Questions

1. **What is a dictionary in Python?**
   A dictionary is an unordered collection of key-value pairs. It is mutable, and keys must be unique and immutable.

2. **How can you iterate over dictionary items in Python?**
   You can iterate using the `.items()` method:
   ```python
   for key, value in my_dict.items():
       print(key, value)
   ```

3. **What is the difference between `get()` and direct access to keys?**
   `get()` returns `None` or a specified default if the key doesn’t exist, while direct access raises a `KeyError`.

4. **How do you remove an item from a dictionary in Python?**
   You can use `pop()` to remove an item by key or `popitem()` to remove the last inserted item.

5. **What is the use of `setdefault()` in dictionaries?**
   `setdefault()` inserts a key with a default value if it doesn’t exist.

6. **What is a dictionary comprehension?**
   A concise way to create dictionaries. Example:
   ```python
   {x: x**2 for x in range(5)}
   ```

# Exercises

1. Write a Python program to sum all the values in a dictionary.
   ```python
   my_dict = {'a': 100, 'b': 200, 'c': 300}
   print(sum(my_dict.values()))  # Output: 600
   ```

2. Create a program to merge two dictionaries.
   ```python
   dict1 = {'a': 1, 'b': 2}
   dict2 = {'c': 3, 'd': 4}
   dict1.update(dict2)
   print(dict1)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
   ```

3. Write a Python program to check if a given key exists in a dictionary.

4. Create a dictionary of squares of numbers from 1 to 10 using dictionary comprehension.
