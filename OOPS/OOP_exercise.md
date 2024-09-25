
# Python Inheritance Exercise: Building a Library System

### Objective:
Understand the concepts of inheritance by creating a simple class hierarchy representing a library system.

---

## Problem Statement:

You need to design a library management system with the following classes:

### 1. `Book`:
This class will represent a book in the library.

**Attributes**:
- `title`: The title of the book.
- `author`: The author of the book.
- `isbn`: A unique number to identify the book.

**Methods**:
- `get_book_info()`: This method returns the book’s title, author, and ISBN.

---

### 2. `EBook` (derived class from `Book`):
This class will represent an electronic book (ebook).

**Attributes**:
- `file_size`: Size of the ebook file in MB.

**Methods**:
- Override `get_book_info()`: Include the file size in the output.

---

### 3. `PrintedBook` (derived class from `Book`):
This class will represent a printed book.

**Attributes**:
- `weight`: Weight of the printed book in grams.
- `num_pages`: Number of pages in the book.

**Methods**:
- Override `get_book_info()`: Include the weight and number of pages in the output.

---

## Tasks:

1. Implement the classes `Book`, `EBook`, and `PrintedBook` using inheritance.
2. Create instances of each class and call `get_book_info()` for each of them.
3. Use the `super()` method to ensure code reusability.
4. **Bonus Task**: Add a method `is_heavy()` to the `PrintedBook` class that returns `True` if the weight of the book is more than 500 grams, and `False` otherwise.

---

## Example Code and Output:

```python
# Create a PrintedBook instance
printed_book = PrintedBook("Python Programming", "John Doe", "123456789", 1200, 500)
print(printed_book.get_book_info())
# Output: Title: Python Programming, Author: John Doe, ISBN: 123456789, Weight: 1200g, Pages: 500
print(printed_book.is_heavy())  # Output: True

# Create an EBook instance
ebook = EBook("Learning Data Science", "Jane Smith", "987654321", 15)
print(ebook.get_book_info())
# Output: Title: Learning Data Science, Author: Jane Smith, ISBN: 987654321, File Size: 15MB
```

---

## Key Concepts:
- Inheritance
- Method overriding
- Reusability with `super()`
