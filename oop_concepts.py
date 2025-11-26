from abc import ABC, abstractmethod

"""
*OOPs Concepts in Python*

1. Class in Python
2. Objects in Python
3. Inheritance in Python
4. Polymorphism in Python
5. Encapsulation in Python
6. Data Abstraction in Python

"""

"""
1. Class in Python
Classes are the blueprint for creating objects.
Defines a set of attributes and methods that the created objects (instances) can have.
"""

class Dog:
    species = "Canine"  # class attribute shared for all instances

    def __init__(self, name, breed, age):
        self.name = name  # instance attribute and Publicj attribute
        self._breed = breed  # Protected attribute
        self.__age = age  # Private attribute

    def display_name(self):
        print(f"Dog's Name: {self.name}")

    def display_info(self):
        print(f"Dog's Name: {self.name}, Breed: {self._breed}, and Age: {self.__age}")

    def sound(self):
        print(f"Dog sound")

    # Getter and Setter for private attribute
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")



"""
2. Objects in Python
An Object is an instance of a Class. It represents a specific implementation of a Class, and holds its own data.
- State: represented by their attributes
- Behavior: represented by their methods
- Identity: unique representation
"""

# Example Usage
family_dog = Dog("Bony", "Yorkshire", 10)
print(family_dog.name)


"""
3. Inheritance in Python
Inheritance allows a class (child class) to acquire properties and methods of another class (parent class).
Reusability is the main benefit.

Inheritance Types
A. Single Inheritance: A child class inherits from a single parent class.
B. Multiple Inheritance: A child class inherits from more than one parent class.
C. Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another class.
D. Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
Hybrid Inheritance: A combination of two or more types of inheritance.
"""

class Labrador(Dog):  # Single Inheritance
    def sound(self):
        print("Labrador woofs") # overriding parent method

class GuideDog(Labrador):  # Multilevel Inheritance
    def guide(self):
        print(f"{self.name}Guides the way!")

class Friendly:
    def greet(self):
        print("Friendly!")

class GoldenRetriever(Dog, Friendly):  # Multiple Inheritance
    def sound(self):
        print("Golden Retriever Barks")

# Example Usage
lab = Labrador("Buddy", "Labrador", 2)
lab.display_name()
lab.sound()

guide_dog = GuideDog("Max", "Special", 3)
guide_dog.display_name()
guide_dog.guide()

retriever = GoldenRetriever("Charlie", "GoldenR", 34)
retriever.display_name()
retriever.greet()
retriever.sound()


"""
4. Polymorphism in Python
Polymorphism allows methods to have the same name but behave differently based on the object's context.
It can be achieved through method overriding.
See how Labrador and GolderRetriever overrides the sound method of their parent class Dog.
"""

"""
5. Encapsulation in Python
Limit what pieces of your code are accesible, make private methods or attributes.

Types of Encapsulation:
A. Public Members: Accessible from anywhere.
B. Protected Members: Accessible within the class and its subclasses. Uses a single _
C. Private Members: Accessible only within the class. Uses double __. Access requieres getter and setter methods.
"""

# Accessing public member
print(family_dog.name)  # Accessible

# Accessing protected member
print(family_dog._breed)  # Accessible but discouraged outside the class

# Accessing private member using getter
print(family_dog.get_age())

# Modifying private member using setter
print("Modifying private member using setter")
family_dog.set_age(5)
family_dog.display_info()


"""
5. Data Abstraction in Python
Abstraction hides the internal implementation details while exposing only the necessary functionality.
It helps focus on "what to do" rather than "how to do it."
If you had to understand every single function in a big codebase, you would never code anything.

Types of Abstraction:
A. Partial Abstraction: Abstract class contains both abstract and concrete methods.
B. Full Abstraction: Abstract class contains only abstract methods (like interfaces).
"""


class Cat(ABC):  # Abstract Class
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):  # Abstract Method
        pass

    def display_name(self):  # Concrete Method
        print(f"Cat's Name: {self.name}")

class Siames(Cat):  # Partial Abstraction
    def sound(self):
        print("Siames Miauuuuu!")

michy = Siames("Mipi")
michy.sound()
