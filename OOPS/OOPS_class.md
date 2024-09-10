
# Python Class Example: Animal

## 1. Introduction to the Animal Class
This example demonstrates the concept of **classes** in Python by creating an `Animal` class. The class includes multiple methods to represent different behaviors like making a sound, eating, sleeping, and moving.

## 2. Why Use a Class?
Classes allow us to group related data (attributes) and behaviors (methods) into a single structure, making code more modular and easier to maintain. In this case, the `Animal` class represents an animal with specific attributes and behaviors.

## 3. Class Structure

```python
class Animal:
    # Class variable (shared by all instances)
    species = "Mammal"
    
    # Constructor to initialize instance variables
    def __init__(self, name, sound, food):
        self.name = name        # Instance variable
        self.sound = sound      # Instance variable
        self.food = food        # Instance variable
    
    # Method to represent the sound behavior
    def make_sound(self):
        return f"{self.name} makes a {self.sound} sound."
    
    # Method to represent eating behavior
    def eat(self):
        return f"{self.name} is eating {self.food}."
    
    # Method to represent sleeping behavior
    def sleep(self):
        return f"{self.name} is sleeping."
    
    # Method to represent movement behavior
    def move(self):
        return f"{self.name} is moving around."
```

## 4. Instance and Class Variables
- **Instance Variables**: `name`, `sound`, and `food` are unique to each instance (object) of the class.
- **Class Variable**: `species` is shared by all instances of the `Animal` class.

## 5. Behaviors Represented by Methods
- **make_sound()**: Describes the sound the animal makes.
- **eat()**: Describes what the animal eats.
- **sleep()**: Describes the animal's sleeping action.
- **move()**: Describes the movement of the animal.

## 6. Creating Objects and Accessing Methods

```python
# Creating instances (objects) of the Animal class
dog = Animal("Dog", "bark", "bones")
cat = Animal("Cat", "meow", "fish")

# Using methods to show different behaviors
print(dog.make_sound())   # Output: Dog makes a bark sound.
print(dog.eat())          # Output: Dog is eating bones.
print(dog.sleep())        # Output: Dog is sleeping.
print(dog.move())         # Output: Dog is moving around.

print(cat.make_sound())   # Output: Cat makes a meow sound.
print(cat.eat())          # Output: Cat is eating fish.
print(cat.sleep())        # Output: Cat is sleeping.
print(cat.move())         # Output: Cat is moving around.
```

## 7. Summary
The `Animal` class illustrates how classes can be used to bundle related data and functionality. Each object (dog and cat) has its own attributes (`name`, `sound`, `food`) and behaviors (`make_sound()`, `eat()`, `sleep()`, `move()`). This makes the code more organized and reusable.
