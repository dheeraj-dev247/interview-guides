# 🐍 Python Interview Guide

## 1. Introduction

### 🎯 Purpose of This Guide

This guide is designed to help you **prepare efficiently for Python technical interviews**.
It focuses on **the most commonly asked topics, coding problems, and conceptual questions** that appear in interviews for software engineering, data, and backend development roles.

Whether you're interviewing for roles such as:

* **Python Developer**
* **Backend Engineer**
* **Automation Engineer**
* **Data Engineer / Analyst**
* **SDET (Software Development Engineer in Test)**
* or any position that requires strong Python fundamentals,

this guide will help you **understand, recall, and apply** Python concepts under real interview conditions.

---

### 🧭 How to Use This Guide

1. **Study by Section:**
   Each section covers a major Python topic, followed by **example questions and code snippets**.

2. **Practice Actively:**
   Don’t just read — run every example and tweak it.
   Understanding comes from *experimentation*.

3. **Focus on Why, Not Just How:**
   Interviewers love to ask *why Python behaves a certain way*.
   This guide includes reasoning behind each example.

4. **Track Your Weak Spots:**
   As you go through the material, note the areas where you get stuck — and revisit them later.

5. **Use as a Revision Tool:**
   Before interviews, skim through summary tables and example problems for a quick refresher.

---

### 💡 Structure of the Guide

| Section | Topic                | Focus                                               |
| ------- | -------------------- | --------------------------------------------------- |
| 2       | Core Python Concepts | Variables, Operators, and Control Flow              |
| 3       | Functions & Scopes   | Function behavior, `*args`, `**kwargs`, and Lambdas |
| 4       | Data Structures      | Lists, Tuples, Sets, Dictionaries                   |
| 5       | OOP                  | Classes, Inheritance, Magic Methods                 |
| 6       | Exception Handling   | Try/Except and Custom Exceptions                    |
| 7       | File Handling        | Reading/Writing and Context Managers                |
| 8       | Modules & Packages   | Imports and Common Libraries                        |
| 9       | Advanced Topics      | Decorators, Generators, and Memory Concepts         |
| 10      | Coding Challenges    | Common Interview Questions                          |
| 11      | Best Practices       | PEP8, Big-O, and Optimization                       |
| 12      | Mock Interview       | Practice Questions and Sample Answers               |

---

### 🧑‍💻 Who Should Use This Guide

This guide is ideal for:

* Candidates preparing for **Python-centric interviews**
* Developers brushing up before a **technical round**
* Students and professionals aiming for roles at **top tech companies (Google, Amazon, etc.)**

---

### 🕒 Estimated Study Time

If you’re preparing intensively:

* **3–5 days:** Fast revision for experienced Python users
* **1–2 weeks:** Full preparation with coding practice
* **4+ weeks:** Deep dive with mock interviews and projects

---



# 2. Core Python Concepts

### 🧱 Overview

Core Python concepts form the foundation of every interview.
Interviewers test whether you understand **how Python handles data, memory, and logic** — not just if you can write code.

This section covers:

* Data Types & Variables
* Operators
* Control Flow (if-else, loops, etc.)
* Common pitfalls and examples

---

## 2.1 Data Types & Variables

### 🧩 Built-in Data Types

Python is dynamically typed, meaning you don’t need to declare variable types explicitly.

| Category | Type                            | Example                                     |
| -------- | ------------------------------- | ------------------------------------------- |
| Numeric  | `int`, `float`, `complex`       | `x = 5`, `y = 3.14`, `z = 2 + 3j`           |
| Sequence | `str`, `list`, `tuple`, `range` | `"hello"`, `[1,2,3]`, `(1,2,3)`, `range(5)` |
| Mapping  | `dict`                          | `{"a": 1, "b": 2}`                          |
| Set      | `set`, `frozenset`              | `{1,2,3}`                                   |
| Boolean  | `bool`                          | `True`, `False`                             |
| None     | `NoneType`                      | `x = None`                                  |

---

### 🧠 Mutable vs Immutable

A **mutable** object can be changed after creation, while an **immutable** one cannot.

| Mutable               | Immutable                              |
| --------------------- | -------------------------------------- |
| `list`, `dict`, `set` | `int`, `float`, `str`, `tuple`, `bool` |

**Example:**

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # Output: [1, 2, 3, 4]  (both a and b refer to same object)
```

---

### ⚠️ Common Interview Questions

**Q1:** What is the difference between `is` and `==`?
**A:**

* `is` → checks *object identity* (same memory reference)
* `==` → checks *value equality*

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True  (values equal)
print(a is b)  # False (different objects)
```

**Q2:** What happens when you modify a mutable default argument in a function?
**A:**
Mutable defaults persist between calls — a common pitfall.

```python
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2]  <-- unexpected!
```

✅ Fix:

```python
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

---

## 2.2 Operators

Python supports several categories of operators.

| Category   | Example                             | Description             |                   |
| ---------- | ----------------------------------- | ----------------------- | ----------------- |
| Arithmetic | `+`, `-`, `*`, `/`, `//`, `%`, `**` | Basic math              |                   |
| Comparison | `==`, `!=`, `<`, `>`, `<=`, `>=`    | Value comparison        |                   |
| Logical    | `and`, `or`, `not`                  | Boolean logic           |                   |
| Identity   | `is`, `is not`                      | Object identity         |                   |
| Membership | `in`, `not in`                      | Membership in iterable  |                   |
| Bitwise    | `&`, `                              | `, `^`, `~`, `<<`, `>>` | Binary operations |
| Assignment | `=`, `+=`, `-=`, `*=`               | Shorthand updates       |                   |

**Example:**

```python
x, y = 5, 2
print(x ** y)   # 25
print(x // y)   # 2 (floor division)
print(x % y)    # 1
```

---

## 2.3 Control Flow

Control flow structures decide **which parts of code execute**.

### 🔹 Conditional Statements

```python
x = 10
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

**Interview Tip:**
Know the difference between `if`, `elif`, and `else`, and how Python evaluates truthy/falsy values:

* `0`, `''`, `[]`, `{}`, `None`, and `False` → all evaluate to False.

---

### 🔹 Loops

**For Loop Example:**

```python
for i in range(5):
    print(i)
```

**While Loop Example:**

```python
n = 3
while n > 0:
    print(n)
    n -= 1
```

**Loop Control Keywords:**

* `break`: exits loop
* `continue`: skips to next iteration
* `pass`: placeholder (does nothing)

**Example:**

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

### 🧩 Common Mini Problems

**Q1:** Print all even numbers from 1 to 10.

```python
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
```

**Q2:** FizzBuzz (very common interview question)

```python
for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

---

### ✅ Quick Recap

* Python has **dynamic typing** and **mutable vs immutable** distinctions.
* `is` checks identity, `==` checks equality.
* Avoid mutable default arguments in functions.
* Master conditionals and loops — they’re often used in coding rounds.

---

# 3. Functions & Scopes

### 🧠 Overview

Functions are a key part of Python interviews.
They test whether you can **organize logic**, **reuse code**, and **understand variable behavior and lifetime**.

Interviewers often ask about:

* Function definitions and arguments
* Default values and scope
* Lambda, recursion, closures, and higher-order functions

---

## 3.1 Defining and Calling Functions

**Basic Syntax:**

```python
def greet(name):
    return f"Hello, {name}!"
```

**Calling the Function:**

```python
print(greet("Alice"))  # Output: Hello, Alice!
```

Python functions are **first-class objects**, meaning they can be:

* Assigned to variables
* Passed as arguments
* Returned from other functions

**Example:**

```python
def shout(text):
    return text.upper()

def speak(func):
    print(func("hello"))

speak(shout)  # Output: HELLO
```

---

## 3.2 Function Arguments

### 🔹 Types of Arguments

| Type                                 | Example            | Description                      |
| ------------------------------------ | ------------------ | -------------------------------- |
| Positional                           | `func(10, 20)`     | Based on order                   |
| Keyword                              | `func(x=10, y=20)` | Based on parameter name          |
| Default                              | `def f(x, y=5)`    | Uses default if not provided     |
| Variable-length (`*args`)            | `def f(*args)`     | Accepts multiple positional args |
| Keyword variable-length (`**kwargs`) | `def f(**kwargs)`  | Accepts multiple keyword args    |

---

### 🧩 Example – `*args` and `**kwargs`

```python
def show_args(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

show_args(1, 2, 3, name="Dheeraj", age=25)
# Output:
# Positional: (1, 2, 3)
# Keyword: {'name': 'Dheeraj', 'age': 25}
```

**Interview Tip:**
Remember — `*args` is a tuple, and `**kwargs` is a dictionary.

---

## 3.3 Default Arguments & Common Pitfall

**Default Example:**

```python
def power(base, exp=2):
    return base ** exp

print(power(3))   # 9
print(power(3, 3))  # 27
```

**Pitfall with Mutable Defaults:**

```python
def add_to_list(item, lst=[]):
    lst.append(item)
    return lst

print(add_to_list(1))  # [1]
print(add_to_list(2))  # [1, 2] <-- shared list!
```

✅ **Fix:**

```python
def add_to_list(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

---

## 3.4 Variable Scope and Lifetime

Python uses the **LEGB Rule** for variable lookup:

* **L** – Local (inside the function)
* **E** – Enclosing (in nested functions)
* **G** – Global (module level)
* **B** – Built-in (Python keywords/functions)

**Example:**

```python
x = 10  # Global

def outer():
    x = 5  # Enclosing
    def inner():
        x = 2  # Local
        print(x)
    inner()

outer()  # Output: 2
```

---

### 🔹 Global and Nonlocal Keywords

**`global`:** Modify a global variable
**`nonlocal`:** Modify a variable in the enclosing (non-global) scope

```python
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # 1
```

```python
def outer():
    x = "outer"
    def inner():
        nonlocal x
        x = "inner"
    inner()
    print(x)

outer()  # Output: inner
```

---

## 3.5 Lambda (Anonymous) Functions

A **lambda function** is a one-line, anonymous function.

**Syntax:**

```python
lambda arguments: expression
```

**Examples:**

```python
square = lambda x: x * x
print(square(5))  # 25

add = lambda a, b: a + b
print(add(2, 3))  # 5
```

**Common Interview Use:**

```python
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
print(squared)  # [1, 4, 9, 16]
```

---

## 3.6 Recursion

Functions calling themselves — a popular interview test.

**Example: Factorial**

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

**Example: Fibonacci**

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(6))  # 8
```

**Interview Tip:**
Always mention **base case** and **stack depth** concerns in recursion questions.

---

## 3.7 Closures

A **closure** is a function that remembers variables from its enclosing scope even after the outer function has finished executing.

**Example:**

```python
def outer(msg):
    def inner():
        print(msg)
    return inner

say_hi = outer("Hello!")
say_hi()  # Output: Hello!
```

Even though `outer()` has finished, `inner()` still remembers `msg`.

---

## 3.8 Higher-Order Functions

A **higher-order function** either:

* Takes another function as input, or
* Returns a function.

**Examples:**

```python
def apply_func(func, value):
    return func(value)

print(apply_func(lambda x: x + 10, 5))  # 15
```

Common built-in higher-order functions:

* `map()`
* `filter()`
* `reduce()` (from `functools`)

**Example with `filter`:**

```python
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4, 6]
```

---

### ✅ Quick Recap

* Functions are **first-class objects**.
* Understand `*args`, `**kwargs`, and default argument behavior.
* Remember **LEGB rule** for scopes.
* Practice **lambda**, **recursion**, and **closures** — frequent interview topics.
---
# 4. Data Structures

### 🧠 Overview

Data structures are at the heart of Python interviews.
Interviewers frequently test your ability to **choose the right structure**, **manipulate data efficiently**, and **understand time complexities**.

We’ll cover:

* Lists
* Tuples
* Sets
* Dictionaries
* Comprehensions
* Common interview questions

---

## 4.1 Lists

A **list** is an ordered, mutable collection.

**Example:**

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])       # apple
fruits.append("date")  # add item
fruits.remove("banana")
print(fruits)          # ['apple', 'cherry', 'date']
```

### 🔹 Common Operations

| Operation | Example                                       | Description      |
| --------- | --------------------------------------------- | ---------------- |
| Add       | `append(x)` / `extend(iter)` / `insert(i, x)` | Insert items     |
| Remove    | `pop()` / `remove(x)` / `clear()`             | Delete items     |
| Access    | `fruits[i]` / `fruits[-1]`                    | Index access     |
| Sort      | `sort()` / `sorted()`                         | In-place vs copy |
| Length    | `len(list)`                                   | Count elements   |

**Example: Sorting**

```python
nums = [4, 2, 9, 1]
nums.sort()
print(nums)  # [1, 2, 4, 9]
```

### 🔹 List Comprehensions

A concise way to create lists.

```python
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

**Conditional Example:**

```python
evens = [x for x in range(10) if x % 2 == 0]
```

**Nested Example:**

```python
matrix = [[1,2,3], [4,5,6]]
flattened = [num for row in matrix for num in row]
print(flattened)  # [1,2,3,4,5,6]
```

---

### 💬 Common List Interview Questions

**Q1: Reverse a list.**

```python
nums = [1, 2, 3, 4]
print(nums[::-1])  # [4,3,2,1]
```

**Q2: Remove duplicates from a list.**

```python
nums = [1, 2, 2, 3, 4, 4]
unique = list(set(nums))
print(unique)  # [1,2,3,4]
```

**Q3: Find the second largest element.**

```python
nums = [10, 5, 8, 20]
nums.sort()
print(nums[-2])  # 10
```

---

## 4.2 Tuples

A **tuple** is an ordered, immutable collection — faster and hashable (can be used as dict keys).

**Example:**

```python
coords = (10, 20)
print(coords[0])  # 10
```

**Tuple Unpacking:**

```python
x, y = coords
print(x, y)  # 10 20
```

**Nested Tuple Example:**

```python
point = (1, (2, 3))
print(point[1][0])  # 2
```

**Common Question:**
Why use a tuple instead of a list?
✅ Faster lookup, immutable (safe), and usable as a key in dictionaries.

---

## 4.3 Sets

A **set** is an unordered collection of unique elements.

**Example:**

```python
nums = {1, 2, 3, 3}
print(nums)  # {1, 2, 3}
```

### 🔹 Common Set Operations

| Operation            | Syntax                     | Example                         |        |                  |
| -------------------- | -------------------------- | ------------------------------- | ------ | ---------------- |
| Add                  | `add(x)`                   | `s.add(5)`                      |        |                  |
| Remove               | `remove(x)` / `discard(x)` | `s.discard(2)`                  |        |                  |
| Union                | `a                         | b`or`a.union(b)`                | `{1,2} | {2,3}`→`{1,2,3}` |
| Intersection         | `a & b`                    | `{1,2,3}&{2,3,4}` → `{2,3}`     |        |                  |
| Difference           | `a - b`                    | `{1,2,3}-{2}` → `{1,3}`         |        |                  |
| Symmetric Difference | `a ^ b`                    | `{1,2,3}^{3,4,5}` → `{1,2,4,5}` |        |                  |

**Example:**

```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)  # {3}
```

**Interview Tip:**
Sets are great for **duplicate removal** and **membership checks (O(1))**.

---

## 4.4 Dictionaries

A **dictionary** maps keys to values — it’s unordered (since Python 3.7+, insertion order is preserved).

**Example:**

```python
person = {"name": "Alice", "age": 25}
print(person["name"])  # Alice
```

### 🔹 Common Dictionary Methods

| Method     | Description        | Example                         |
| ---------- | ------------------ | ------------------------------- |
| `keys()`   | Get all keys       | `person.keys()`                 |
| `values()` | Get all values     | `person.values()`               |
| `items()`  | Key-value pairs    | `person.items()`                |
| `get()`    | Safe key access    | `person.get('age', 0)`          |
| `update()` | Merge dictionaries | `person.update({"city": "NY"})` |

**Dictionary Comprehension Example:**

```python
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

**Iterating Over Dictionaries:**

```python
for key, value in person.items():
    print(key, value)
```

---

### 💬 Common Dictionary Interview Questions

**Q1: Count character frequencies in a string.**

```python
text = "banana"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)  # {'b':1, 'a':3, 'n':2}
```

**Q2: Find the key with the maximum value.**

```python
scores = {"A": 90, "B": 75, "C": 95}
topper = max(scores, key=scores.get)
print(topper)  # C
```

---

## 4.5 Combining Structures

**Example:** Nested dictionary and list manipulation

```python
students = [
    {"name": "Alice", "marks": [80, 85, 90]},
    {"name": "Bob", "marks": [70, 75, 65]},
]

averages = {s["name"]: sum(s["marks"]) / len(s["marks"]) for s in students}
print(averages)  # {'Alice': 85.0, 'Bob': 70.0}
```

---

## 4.6 Quick Comparison Table

| Feature            | List | Tuple | Set | Dictionary       |
| ------------------ | ---- | ----- | --- | ---------------- |
| Ordered            | ✅    | ✅     | ❌   | ✅                |
| Mutable            | ✅    | ❌     | ✅   | ✅                |
| Duplicates Allowed | ✅    | ✅     | ❌   | Keys ❌, Values ✅ |
| Indexable          | ✅    | ✅     | ❌   | ✅ (by key)       |
| Hashable           | ❌    | ✅     | ✅   | ❌                |

---

### ✅ Quick Recap

* Lists → ordered and mutable.
* Tuples → ordered and immutable.
* Sets → unique, unordered, fast membership checks.
* Dictionaries → key-value storage, fast lookups.
* Learn list/dict comprehensions — a *favorite* in Python interviews.
---

# 5. Object-Oriented Programming (OOP)

### 🧠 Overview

Python is an **object-oriented language**, and understanding OOP is essential for writing scalable, modular, and reusable code.

Interviewers often test your grasp of:

* Classes & Objects
* Encapsulation, Inheritance, Polymorphism
* Class vs Static methods
* Magic methods and dunder functions

---

## 5.1 Classes and Objects

A **class** is a blueprint for creating objects (instances), and an **object** is an instance of that class.

**Example:**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

# Creating an object
p1 = Person("Alice", 25)
print(p1.greet())  # Hi, I'm Alice and I'm 25 years old.
```

**Interview Tip:**
The `__init__` method is a **constructor**, automatically called when you create a new instance.

---

## 5.2 The `self` Keyword

`self` represents the instance of the class and allows access to instance attributes and methods.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

dog1 = Dog("Buddy")
dog1.bark()  # Buddy says Woof!
```

**Note:**
`self` is passed automatically when calling instance methods.

---

## 5.3 Class Variables vs Instance Variables

| Type              | Defined           | Shared | Example           |
| ----------------- | ----------------- | ------ | ----------------- |
| Instance Variable | Inside `__init__` | ❌ No   | `self.name`       |
| Class Variable    | At class level    | ✅ Yes  | `species = "Dog"` |

**Example:**

```python
class Dog:
    species = "Canine"  # Class variable
    def __init__(self, name):
        self.name = name  # Instance variable

dog1 = Dog("Max")
dog2 = Dog("Charlie")

print(dog1.species, dog2.species)  # Canine Canine
Dog.species = "Wolf"
print(dog1.species, dog2.species)  # Wolf Wolf
```

---

## 5.4 Encapsulation

Encapsulation means **restricting direct access** to object data.

In Python, prefixing variables with `_` or `__` indicates protected/private access (by convention).

**Example:**

```python
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = Account("Dheeraj", 1000)
acc.deposit(500)
print(acc.get_balance())  # 1500
```

**Note:**
Private variables can still be accessed via name mangling: `_ClassName__var`.

---

## 5.5 Inheritance

Inheritance allows one class to inherit attributes and methods from another.

**Example:**

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog("Buddy")
print(dog.speak())  # Woof!
```

**Interview Tip:**
Use `super()` to call parent class methods.

**Example:**

```python
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
```

---

## 5.6 Polymorphism

Polymorphism means using a **common interface** for different object types.

**Example:**

```python
class Bird:
    def speak(self):
        return "Chirp!"

class Dog:
    def speak(self):
        return "Bark!"

for animal in [Bird(), Dog()]:
    print(animal.speak())
# Chirp!
# Bark!
```

---

## 5.7 Abstraction

Python supports abstraction via **abstract base classes (ABCs)** from the `abc` module.

**Example:**

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started!")

car = Car()
car.start()  # Car started!
```

Attempting to instantiate `Vehicle()` directly will raise a `TypeError`.

---

## 5.8 Class Methods and Static Methods

| Method Type     | Decorator       | Access                                | Purpose                                      |
| --------------- | --------------- | ------------------------------------- | -------------------------------------------- |
| Instance Method | —               | Accesses instance attributes (`self`) | Operates on individual objects               |
| Class Method    | `@classmethod`  | Accesses class (`cls`)                | Affects the class as a whole                 |
| Static Method   | `@staticmethod` | No `self` or `cls`                    | Utility function, logically related to class |

**Example:**

```python
class Employee:
    company = "Google"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    @staticmethod
    def is_valid_email(email):
        return "@" in email

e1 = Employee("Alice")
Employee.change_company("OpenAI")
print(e1.company)  # OpenAI
print(Employee.is_valid_email("test@gmail.com"))  # True
```

---

## 5.9 Magic Methods (Dunder Methods)

Python classes can define special methods (prefixed and suffixed with `__`) to customize behavior.

| Method     | Purpose                           | Example                   |
| ---------- | --------------------------------- | ------------------------- |
| `__init__` | Constructor                       | Called on object creation |
| `__str__`  | String representation             | `print(obj)`              |
| `__repr__` | Developer-friendly representation | For debugging             |
| `__add__`  | Overload `+` operator             | Combine objects           |
| `__len__`  | Support `len()`                   | Return length             |
| `__eq__`   | Compare equality                  | Overload `==`             |

**Example:**

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} ({self.pages} pages)"

    def __add__(self, other):
        return self.pages + other.pages

b1 = Book("Python", 200)
b2 = Book("AI", 150)
print(b1)          # Python (200 pages)
print(b1 + b2)     # 350
```

---

## 5.10 Composition vs Inheritance

**Composition** means using other objects inside a class rather than inheriting from them.

**Example:**

```python
class Engine:
    def start(self):
        print("Engine started!")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition

    def drive(self):
        self.engine.start()
        print("Car is moving!")

c = Car()
c.drive()
```

**Interview Tip:**
Use **composition** for flexibility and **inheritance** for shared structure.

---

### 💬 Common OOP Interview Questions

**Q1:** What’s the difference between `@classmethod` and `@staticmethod`?
**A:**

* `@classmethod` receives the class as the first argument (`cls`)
* `@staticmethod` doesn’t receive instance or class automatically — behaves like a normal function inside a class.

**Q2:** What is the difference between `__str__` and `__repr__`?
**A:**

* `__str__`: for human-readable output (used by `print()`)
* `__repr__`: for developers/debugging (used in interpreter)

**Q3:** Why is encapsulation useful?
**A:**
It hides internal details and protects data integrity.

---

### ✅ Quick Recap

* Classes define **structure**, objects represent **instances**.
* Key principles: **Encapsulation**, **Inheritance**, **Polymorphism**, **Abstraction**.
* Understand the use of `self`, `super()`, and magic methods.
* Practice designing small class hierarchies (Bank, Vehicle, Employee).
---

# 6. Exception Handling

### 🧠 Overview

Exception handling in Python ensures that your program can handle **unexpected errors** gracefully without crashing.
Interviewers often test how well you understand:

* `try`, `except`, `else`, `finally`
* Raising and creating custom exceptions
* Common built-in exceptions
* Best practices for robust code

---

## 6.1 What is an Exception?

An **exception** is an event that interrupts the normal flow of a program.
If not handled, it causes the program to terminate with an error message.

**Example:**

```python
print(10 / 0)  # ZeroDivisionError
```

Common built-in exceptions:

| Exception           | Raised When              |
| ------------------- | ------------------------ |
| `ValueError`        | Invalid value            |
| `TypeError`         | Wrong data type          |
| `ZeroDivisionError` | Division by zero         |
| `IndexError`        | Index out of range       |
| `KeyError`          | Missing dictionary key   |
| `FileNotFoundError` | File not found           |
| `ImportError`       | Import fails             |
| `AttributeError`    | Invalid attribute access |

---

## 6.2 Basic `try`–`except` Block

**Syntax:**

```python
try:
    # code that might raise an exception
except ExceptionType:
    # handle exception
```

**Example:**

```python
try:
    x = int("abc")
except ValueError:
    print("Invalid input!")
```

**Output:**

```
Invalid input!
```

---

## 6.3 Handling Multiple Exceptions

You can handle different exceptions separately or together.

**Example 1: Multiple except blocks**

```python
try:
    x = int(input("Enter number: "))
    print(10 / x)
except ValueError:
    print("Invalid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

**Example 2: Tuple of exceptions**

```python
try:
    result = 10 / 0
except (ZeroDivisionError, ValueError) as e:
    print("Error occurred:", e)
```

---

## 6.4 Using `else` and `finally`

* `else`: executes **only if no exception occurs**
* `finally`: **always executes**, used for cleanup

**Example:**

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division successful.")
finally:
    print("End of program.")
```

**Output (if input = 2):**

```
5.0
Division successful.
End of program.
```

---

## 6.5 Raising Exceptions Manually

You can **raise exceptions** using the `raise` keyword.

**Example:**

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance!")
    balance -= amount
    return balance

try:
    print(withdraw(1000, 1500))
except ValueError as e:
    print(e)
```

**Output:**

```
Insufficient balance!
```

---

## 6.6 Creating Custom Exceptions

For better readability and context, define your own exception classes by inheriting from `Exception`.

**Example:**

```python
class InsufficientFundsError(Exception):
    pass

def transfer(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Not enough funds for transfer.")
    return balance - amount

try:
    transfer(500, 1000)
except InsufficientFundsError as e:
    print("Transaction failed:", e)
```

**Output:**

```
Transaction failed: Not enough funds for transfer.
```

---

## 6.7 The `try...except...finally` Pattern (Real-world Example)

**Example: File Handling**

```python
try:
    file = open("data.txt", "r")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()
    print("File closed.")
```

**Best Practice:**
Use context managers (`with` statement) instead — they handle cleanup automatically.

```python
with open("data.txt", "r") as file:
    data = file.read()
```

---

## 6.8 Nested Exception Handling

You can nest `try-except` blocks when different sections of code may fail independently.

**Example:**

```python
try:
    x = int(input("Enter number: "))
    try:
        print(10 / x)
    except ZeroDivisionError:
        print("Cannot divide by zero!")
except ValueError:
    print("Invalid input!")
```

---

## 6.9 Suppressing Exceptions

Python provides the `contextlib.suppress()` utility to ignore specific exceptions gracefully.

**Example:**

```python
from contextlib import suppress

with suppress(FileNotFoundError):
    open("missing.txt")
```

No error will be raised even if the file doesn’t exist.

---

## 6.10 Logging Exceptions

For production-level code, you should **log exceptions** instead of just printing them.

**Example:**

```python
import logging

logging.basicConfig(level=logging.ERROR)

try:
    result = 10 / 0
except Exception as e:
    logging.error("Error occurred", exc_info=True)
```

---

### 💬 Common Interview Questions

**Q1:** What is the difference between `raise` and `assert`?
**A:**

* `raise` → explicitly triggers an exception.
* `assert` → used for debugging; raises `AssertionError` if the condition is False.

**Q2:** What happens if both `except` and `finally` blocks have `return` statements?
**A:**
The `return` in `finally` overrides the one in `except`.

**Q3:** Why is `finally` block useful?
**A:**
It’s used for cleanup actions (e.g., closing files, releasing resources), ensuring code runs regardless of success or failure.

---

### ✅ Quick Recap

* Use `try-except-else-finally` effectively for robust error handling.
* Avoid bare `except:` — always specify exception types.
* Create custom exceptions for meaningful error reporting.
* Use context managers (`with`) for automatic resource management.
* Use logging instead of `print()` in production code.
---
# 7. File Handling

### 🧠 Overview

File handling in Python is essential for working with external data — reading, writing, and manipulating files.
Interviewers often test:

* Reading/Writing text and CSV files
* Using context managers (`with`)
* Exception handling with files
* Working with JSON and file paths

---

## 7.1 Opening and Closing Files

In Python, you can open files using the built-in `open()` function.

**Syntax:**

```python
file = open(filename, mode)
```

**Common Modes:**

| Mode  | Meaning | Description                       |
| ----- | ------- | --------------------------------- |
| `'r'` | Read    | Default mode                      |
| `'w'` | Write   | Overwrites file                   |
| `'a'` | Append  | Adds content at end               |
| `'x'` | Create  | Creates new file, fails if exists |
| `'b'` | Binary  | Read/write binary data            |
| `'t'` | Text    | Default text mode                 |

**Example:**

```python
file = open("example.txt", "w")
file.write("Hello, Python!")
file.close()
```

**⚠️ Always close the file!**
Unclosed files may cause data loss or memory leaks.

---

## 7.2 Using Context Managers (`with` Statement)

Instead of manually closing files, use `with open()` — it automatically closes files even if an error occurs.

**Example:**

```python
with open("example.txt", "w") as f:
    f.write("Hello, Dheeraj!")
# File is automatically closed here
```

**Reading the file:**

```python
with open("example.txt", "r") as f:
    content = f.read()
    print(content)
```

---

## 7.3 Reading Files

**Methods for Reading:**

| Method        | Description                 |
| ------------- | --------------------------- |
| `read()`      | Reads entire file           |
| `readline()`  | Reads one line              |
| `readlines()` | Reads all lines into a list |

**Example:**

```python
with open("data.txt", "r") as f:
    print(f.readline())       # Reads first line
    print(f.readlines())      # Reads remaining lines as list
```

---

## 7.4 Writing and Appending Files

**Write Mode (`'w'`) – Overwrites file**

```python
with open("output.txt", "w") as f:
    f.write("New content\n")
```

**Append Mode (`'a'`) – Adds new data**

```python
with open("output.txt", "a") as f:
    f.write("Appended line\n")
```

---

## 7.5 Working with File Paths

Use the **`os`** and **`pathlib`** modules for file path management.

**Example (os.path):**

```python
import os
print(os.getcwd())                   # Current directory
print(os.path.exists("data.txt"))    # Check if file exists
print(os.path.join("folder", "file.txt"))  # Combine paths
```

**Example (pathlib – recommended):**

```python
from pathlib import Path
file_path = Path("data.txt")
if file_path.exists():
    print(file_path.read_text())
```

---

## 7.6 Reading and Writing CSV Files

Python’s built-in `csv` module is common in interview tasks.

**Example: Writing to CSV**

```python
import csv

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Role"])
    writer.writerow(["Dheeraj", "Security Engineer"])
```

**Example: Reading CSV**

```python
import csv

with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

---

## 7.7 Working with JSON Files

JSON (JavaScript Object Notation) is commonly used for APIs and configurations.

**Example: Writing JSON**

```python
import json

data = {"name": "Dheeraj", "role": "Cybersecurity Engineer"}

with open("data.json", "w") as f:
    json.dump(data, f)
```

**Example: Reading JSON**

```python
with open("data.json", "r") as f:
    content = json.load(f)
    print(content["role"])
```

---

## 7.8 File Iteration and Line Counting

**Example:**

```python
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())
```

**Counting lines:**

```python
with open("data.txt", "r") as f:
    count = sum(1 for _ in f)
print("Total lines:", count)
```

---

## 7.9 Exception Handling in File Operations

Always handle file-related exceptions like `FileNotFoundError`, `IOError`.

**Example:**

```python
try:
    with open("missing.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File does not exist!")
```

---

## 7.10 Deleting and Renaming Files

**Example:**

```python
import os

# Rename file
os.rename("old.txt", "new.txt")

# Delete file
os.remove("unwanted.txt")
```

**Check before deleting:**

```python
if os.path.exists("temp.txt"):
    os.remove("temp.txt")
else:
    print("File not found!")
```

---

### 💬 Common Interview Questions

**Q1:** Difference between `read()`, `readline()`, and `readlines()`?
**A:**

* `read()` → reads entire file as string
* `readline()` → reads one line
* `readlines()` → returns list of all lines

**Q2:** Why use `with open()` instead of `open()`?
**A:**
Because it automatically handles resource cleanup (closing files safely).

**Q3:** How do you handle a missing file gracefully?
**A:**
Use `try-except` around `open()` or `pathlib.Path.exists()` before reading.

---

### ✅ Quick Recap

* Use `with open()` for safe file handling.
* Understand read/write modes and context managers.
* Use `csv` and `json` for structured data.
* Always handle file exceptions properly.
* Learn `os` and `pathlib` for cross-platform file operations.
  
---

# 8. Iterators, Generators, and Comprehensions

### 🧠 Overview

These are **core Python features** that help you process sequences efficiently.
Interviewers love to test how well you understand:

* How iteration works internally (`__iter__`, `__next__`)
* Differences between lists, generators, and iterators
* How comprehensions simplify loops
* Real-world use cases for generators (e.g., streaming data, large files)

---

## 8.1 Iterables and Iterators

**Iterable:** An object capable of returning its elements one at a time (e.g., `list`, `tuple`, `str`, `dict`).
**Iterator:** An object that produces data on demand using `__next__()`.

**Example:**

```python
nums = [1, 2, 3]
it = iter(nums)  # Get iterator object

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
```

If there are no more elements:

```python
next(it)  # Raises StopIteration
```

---

## 8.2 Custom Iterator

You can make your own iterator class by defining `__iter__()` and `__next__()`.

**Example:**

```python
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration

for num in Counter(1, 5):
    print(num)
```

**Output:**

```
1
2
3
4
5
```

---

## 8.3 Generators

A **generator** is a simpler way to create iterators using the `yield` keyword.
Generators produce items **lazily** — they don’t store all values in memory.

**Example:**

```python
def squares(n):
    for i in range(n):
        yield i * i

for val in squares(5):
    print(val)
```

**Output:**

```
0
1
4
9
16
```

---

## 8.4 Generator Expressions

Similar to list comprehensions but use `()` instead of `[]`.
They are **memory efficient** — generate items on the fly.

**Example:**

```python
gen = (x**2 for x in range(5))
print(next(gen))  # 0
print(next(gen))  # 1
```

**Compare Memory Usage:**

```python
import sys
print(sys.getsizeof([x for x in range(1000)]))  # Large
print(sys.getsizeof((x for x in range(1000))))  # Small
```

---

## 8.5 The `yield` Keyword

When a function contains `yield`, it becomes a **generator function**.

**Key Difference from `return`:**

| `return`                      | `yield`                 |
| ----------------------------- | ----------------------- |
| Exits the function completely | Pauses execution        |
| Returns one value             | Returns a generator     |
| Can’t resume later            | Resumes from last state |

**Example:**

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for val in countdown(3):
    print(val)
```

**Output:**

```
3
2
1
```

---

## 8.6 The `next()` and `send()` Methods

Generators can also receive data via `send()`.

**Example:**

```python
def echo():
    while True:
        val = yield
        print("You sent:", val)

gen = echo()
next(gen)  # Prime generator
gen.send("Hello")  # You sent: Hello
```

---

## 8.7 List Comprehensions

**List comprehension** offers a concise syntax for creating lists.

**Syntax:**

```python
[expression for item in iterable if condition]
```

**Example:**

```python
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

**With condition:**

```python
even = [x for x in range(10) if x % 2 == 0]
print(even)  # [0, 2, 4, 6, 8]
```

---

## 8.8 Dictionary and Set Comprehensions

**Dictionary Comprehension:**

```python
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

**Set Comprehension:**

```python
unique = {x % 3 for x in range(10)}
print(unique)  # {0, 1, 2}
```

---

## 8.9 Nested Comprehensions

**Example:**

```python
matrix = [[1, 2, 3], [4, 5, 6]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6]
```

---

## 8.10 Real-World Use Case

**Processing large log file efficiently:**

```python
def read_large_file(file_name):
    with open(file_name, "r") as f:
        for line in f:
            yield line.strip()

for line in read_large_file("access.log"):
    if "ERROR" in line:
        print(line)
```

This avoids loading the entire file into memory — perfect for interview scenarios about scalability.

---

### 💬 Common Interview Questions

**Q1:** What’s the difference between an iterator and a generator?
**A:**

* Iterators: Use `__iter__()` and `__next__()` manually
* Generators: Created automatically using `yield`

**Q2:** Why are generators memory-efficient?
**A:** They produce one value at a time instead of storing the entire sequence.

**Q3:** Can you have multiple `yield` statements?
**A:** Yes — each one pauses execution and returns a value.

**Q4:** What’s the difference between a list comprehension and a generator expression?
**A:**   
* List comprehension: builds a full list in memory.
* Generator expression: creates a lazy generator (faster for large datasets).


---

### ✅ Quick Recap

* **Iterator** = Object that produces items with `next()`
* **Generator** = Function that yields items lazily
* **Comprehensions** = Concise syntax for lists, dicts, sets
* Use **generators** for large or infinite sequences
* Master **comprehensions** — they’re asked in nearly every Python interview

---

# 9. Modules, Packages, and Imports

### 🧠 Overview

As Python projects grow, code is split into multiple files (modules) and folders (packages).
This section helps you master how **imports, namespaces, and packages** work — a favorite interview topic for assessing clean code organization and dependency handling.

---

## 9.1 What is a Module?

A **module** is simply a Python file (`.py`) that contains functions, classes, or variables that can be imported elsewhere.

**Example:**

📁 `math_utils.py`

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

📁 `main.py`

```python
import math_utils

print(math_utils.add(3, 5))
print(math_utils.multiply(2, 4))
```

**Output:**

```
8
8
```

---

## 9.2 Different Import Styles

| Style                        | Syntax                        | Use Case                            |
| ---------------------------- | ----------------------------- | ----------------------------------- |
| Import module                | `import module_name`          | When you want full module reference |
| Import specific function     | `from module import func`     | When using specific functions       |
| Import with alias            | `import module_name as alias` | For convenience                     |
| Import all (not recommended) | `from module import *`        | Quick tests, not for production     |

**Examples:**

```python
import math
print(math.sqrt(16))

from math import sqrt
print(sqrt(16))

import math as m
print(m.pi)

from math import *  # Not recommended
print(sin(pi/2))
```

---

## 9.3 The `__name__ == "__main__"` Idiom

When a file is run directly, its `__name__` variable is set to `"__main__"`.
This helps separate **executable** code from **importable** modules.

**Example:**

```python
# file: mymodule.py
def greet():
    print("Hello from module!")

if __name__ == "__main__":
    print("Running directly")
else:
    print("Imported as module")
```

Running `python mymodule.py` → `"Running directly"`
Importing it → `"Imported as module"`

---

## 9.4 Packages

A **package** is a collection of Python modules organized in directories.

**Example: Directory Structure**

```
project/
│
├── app/
│   ├── __init__.py
│   ├── utils.py
│   └── core.py
└── main.py
```

**Inside `app/utils.py`:**

```python
def say_hello():
    print("Hello from utils!")
```

**Inside `main.py`:**

```python
from app import utils
utils.say_hello()
```

---

## 9.5 The `__init__.py` File

The `__init__.py` file marks a directory as a Python package.
It can be **empty**, or it can initialize package-level variables or imports.

**Example:**

```python
# app/__init__.py
from .utils import say_hello
```

Now you can do:

```python
from app import say_hello
say_hello()
```

---

## 9.6 Importing from Subpackages

**Example:**

```
mypackage/
│
├── __init__.py
├── data/
│   ├── __init__.py
│   └── reader.py
└── utils/
    ├── __init__.py
    └── formatter.py
```

**reader.py**

```python
def read_data():
    print("Reading data...")
```

**main.py**

```python
from mypackage.data.reader import read_data
read_data()
```

---

## 9.7 The `sys.path` and Module Resolution

Python searches for modules using the directories in `sys.path`.

**Example:**

```python
import sys
print(sys.path)
```

The output is a list of paths where Python looks for modules.
You can append custom paths dynamically:

```python
sys.path.append("/path/to/custom_modules")
```

**Interview Tip:**
Understanding `sys.path` helps debug “ModuleNotFoundError” issues.

---

## 9.8 Built-in and Third-Party Modules

* **Built-in:** Already available (e.g., `os`, `sys`, `math`, `datetime`, `json`)
* **Third-party:** Installed using `pip install`

**Example:**

```bash
pip install requests
```

**Usage:**

```python
import requests
response = requests.get("https://api.github.com")
print(response.status_code)
```

---

## 9.9 Relative vs Absolute Imports

**Absolute Import:**

```python
from app.utils import say_hello
```

**Relative Import (within package):**

```python
from .utils import say_hello
```

Relative imports use a leading `.` to indicate the current or parent package.

**Example:**

* `from . import module` → current package
* `from .. import module` → parent package

---

## 9.10 Organizing Code with Packages (Best Practices)

✅ Follow these guidelines for interview-ready modular code:

1. **Keep modules focused** – each file should handle a single concern.
2. **Avoid circular imports** (when two modules import each other).
3. **Use `__init__.py`** to simplify imports.
4. **Use absolute imports** in large projects for clarity.
5. **Group dependencies** logically (e.g., `utils`, `models`, `api`).

---

### 💬 Common Interview Questions

**Q1:** What’s the difference between a module and a package?
**A:**

* **Module:** Single `.py` file
* **Package:** Directory with an `__init__.py` file that contains modules

**Q2:** Why use `__name__ == "__main__"`?
**A:**
It prevents certain code from running when a module is imported.

**Q3:** How does Python find modules?
**A:**
Python checks built-in modules, current directory, and then paths in `sys.path`.

**Q4:** What are circular imports and how to avoid them?
**A:**
They occur when two modules import each other. Fix by refactoring or using local imports.

---

### ✅ Quick Recap

* **Modules** = `.py` files containing reusable code
* **Packages** = folders containing multiple modules
* `__init__.py` turns a folder into a package
* Use **absolute imports** for clarity, **relative imports** for internal linking
* Understand `sys.path` and `__name__ == "__main__"` for debugging imports

---

# 10. Decorators and Context Managers

### 🧠 Overview

Decorators and context managers are **advanced Python features** that improve readability, reusability, and control over function or resource behavior.
They’re frequently asked in interviews to test deep understanding of:

* Higher-order functions
* Function wrapping and `@decorator` syntax
* Context managers and the `with` statement

---

## 10.1 First-Class and Higher-Order Functions

**First-class functions** → Functions can be treated like any other object.
They can be passed as arguments, returned from other functions, or stored in data structures.

**Example:**

```python
def greet(name):
    return f"Hello, {name}"

def call_func(func, name):
    return func(name)

print(call_func(greet, "Dheeraj"))  # Hello, Dheeraj
```

A **higher-order function** either:

* Takes another function as input, or
* Returns a new function

---

## 10.2 Closures

A **closure** is a function that remembers variables from its enclosing scope even after that scope has finished executing.

**Example:**

```python
def outer(msg):
    def inner():
        print(f"Message: {msg}")
    return inner

say_hi = outer("Hi there!")
say_hi()  # Message: Hi there!
```

**Interview Tip:**
Closures are the foundation of **decorators** in Python.

---

## 10.3 What is a Decorator?

A **decorator** is a function that takes another function and extends or modifies its behavior **without permanently changing it**.

**Basic Syntax:**

```python
@decorator_name
def function_name():
    pass
```

Equivalent to:

```python
function_name = decorator_name(function_name)
```

---

## 10.4 Writing a Simple Decorator

**Example:**

```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def greet():
    print("Hello, Python!")

greet()
```

**Output:**

```
Before function call
Hello, Python!
After function call
```

---

## 10.5 Decorators with Arguments

**Example:**

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
```

**Output:**

```
Hello!
Hello!
Hello!
```

---

## 10.6 Preserving Function Metadata

When you use decorators, the original function’s metadata (like its name or docstring) gets replaced by the wrapper’s.
To fix this, use `functools.wraps`.

**Example:**

```python
from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@debug
def add(a, b):
    """Adds two numbers."""
    return a + b

print(add(2, 3))
print(add.__name__)  # add
print(add.__doc__)   # Adds two numbers.
```

---

## 10.7 Chaining Multiple Decorators

You can apply multiple decorators to a single function.

**Example:**

```python
def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper

def greet_decorator(func):
    def wrapper():
        return f"*** {func()} ***"
    return wrapper

@uppercase
@greet_decorator
def greet():
    return "hello"

print(greet())  # *** HELLO ***
```

---

## 10.8 Built-in Decorators

Python provides built-in decorators such as:

* `@staticmethod`
* `@classmethod`
* `@property`

**Example:**

```python
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Invalid salary")
        self._salary = value

e = Employee("Alice", 50000)
e.salary = 60000
print(e.salary)  # 60000
```

---

## 10.9 Real-World Decorator Example: Logging Execution Time

**Example:**

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)

slow_function()
```

---

## 10.10 Context Managers

A **context manager** handles resource setup and cleanup automatically.
It’s most often used with the `with` statement (e.g., opening files).

**Example (Using `with`):**

```python
with open("test.txt", "w") as file:
    file.write("Hello World!")
```

This automatically closes the file, even if an exception occurs.

---

## 10.11 Creating Custom Context Managers

### Using a Class

```python
class MyContext:
    def __enter__(self):
        print("Entering context...")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context...")

with MyContext():
    print("Inside block")
```

**Output:**

```
Entering context...
Inside block
Exiting context...
```

---

### Using a Generator (`contextlib.contextmanager`)

**Example:**

```python
from contextlib import contextmanager

@contextmanager
def managed_resource(name):
    print(f"Opening {name}")
    yield
    print(f"Closing {name}")

with managed_resource("file.txt"):
    print("Using resource")
```

---

## 10.12 Real-World Example: Database Connection

```python
from contextlib import contextmanager

@contextmanager
def db_connection():
    print("Connecting to database...")
    yield
    print("Closing connection...")

with db_connection():
    print("Performing query...")
```

---

### 💬 Common Interview Questions

**Q1:** What’s the difference between a decorator and a closure?
**A:**

* A closure remembers its outer variables.
* A decorator is a closure used to modify another function.

**Q2:** How does `@property` differ from a normal method?
**A:**
`@property` allows method access like an attribute, improving encapsulation.

**Q3:** How is a context manager different from `try-finally`?
**A:**
A context manager is cleaner, reusable, and automatically ensures resource cleanup.

**Q4:** What does `functools.wraps` do?
**A:**
It preserves the original function’s metadata (name, docstring).

---

### ✅ Quick Recap

* **Decorators** modify behavior of functions or classes.
* **Closures** enable decorators by remembering enclosing scope.
* Use `@wraps` to preserve metadata.
* **Context Managers** simplify resource management.
* Use `with` or `@contextmanager` for safe, reusable cleanup code.
  
---

# 11. Multithreading and Multiprocessing

### 🧠 Overview

Python supports **concurrency** (doing many things at once) through:

* **Multithreading:** Multiple threads within a process (shared memory)
* **Multiprocessing:** Multiple processes (separate memory spaces)

Understanding when and why to use each is a common Python interview test — especially for roles involving performance optimization, APIs, or distributed systems.

---

## 11.1 Concurrency vs Parallelism

| Concept         | Description                                                | Example                             |
| --------------- | ---------------------------------------------------------- | ----------------------------------- |
| **Concurrency** | Managing multiple tasks *at once* (interleaving execution) | Switching between I/O tasks         |
| **Parallelism** | Executing multiple tasks *simultaneously*                  | Running tasks on multiple CPU cores |

---

## 11.2 The Global Interpreter Lock (GIL)

The **GIL** is a mutex that allows only one thread to execute Python bytecode at a time, even on multi-core CPUs.
It’s why **Python threads are not true parallel threads** for CPU-bound tasks.

**Implication:**

* **Threads** → Best for I/O-bound tasks (like API calls, file I/O)
* **Processes** → Best for CPU-bound tasks (like calculations, ML workloads)

---

## 11.3 Multithreading with `threading` Module

**Example:**

```python
import threading
import time

def worker(name):
    print(f"Thread {name} starting")
    time.sleep(2)
    print(f"Thread {name} finished")

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("All threads complete")
```

**Output (order may vary):**

```
Thread 0 starting
Thread 1 starting
Thread 2 starting
Thread 0 finished
Thread 1 finished
Thread 2 finished
All threads complete
```

---

## 11.4 Thread Synchronization with Locks

Since threads share memory, you must protect shared resources using **locks**.

**Example:**

```python
import threading

lock = threading.Lock()
counter = 0

def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("Final counter:", counter)
```

Without a lock, you’ll get inconsistent results due to race conditions.

---

## 11.5 Using `concurrent.futures.ThreadPoolExecutor`

A higher-level and preferred way to manage threads.

**Example:**

```python
from concurrent.futures import ThreadPoolExecutor
import time

def fetch_data(n):
    print(f"Fetching {n}")
    time.sleep(1)
    return f"Data {n}"

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(fetch_data, [1, 2, 3, 4, 5])

for r in results:
    print(r)
```

---

## 11.6 Multiprocessing in Python

To overcome the GIL and achieve **true parallelism**, use the `multiprocessing` module.
Each process runs its own Python interpreter and memory space.

**Example:**

```python
from multiprocessing import Process
import os
import time

def task(name):
    print(f"Running {name} in process ID: {os.getpid()}")
    time.sleep(2)
    print(f"Finished {name}")

if __name__ == "__main__":
    processes = [Process(target=task, args=(f"Task {i}",)) for i in range(3)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print("All processes complete")
```

**Output:**

```
Running Task 0 in process ID: 1010
Running Task 1 in process ID: 1011
Running Task 2 in process ID: 1012
Finished Task 0
Finished Task 1
Finished Task 2
All processes complete
```

---

## 11.7 Using `concurrent.futures.ProcessPoolExecutor`

A cleaner way to manage multiple processes.

**Example:**

```python
from concurrent.futures import ProcessPoolExecutor
import time

def square(n):
    time.sleep(1)
    return n * n

with ProcessPoolExecutor() as executor:
    results = executor.map(square, [1, 2, 3, 4, 5])

print(list(results))
```

---

## 11.8 Sharing Data Between Processes

Each process has its own memory — use **multiprocessing.Queue** or **Manager** to share data.

**Example:**

```python
from multiprocessing import Process, Queue

def worker(q):
    q.put("Hello from process")

if __name__ == "__main__":
    q = Queue()
    p = Process(target=worker, args=(q,))
    p.start()
    print(q.get())  # Hello from process
    p.join()
```

---

## 11.9 Comparing Threads vs Processes

| Feature   | Threads      | Processes         |
| --------- | ------------ | ----------------- |
| Memory    | Shared       | Separate          |
| GIL       | Affected     | Not affected      |
| Overhead  | Low          | High              |
| Ideal for | I/O-bound    | CPU-bound         |
| Example   | Web requests | Heavy computation |

---

## 11.10 Async Programming (Brief Overview)

Modern Python also supports **asynchronous programming** using `asyncio` for concurrent I/O.

**Example:**

```python
import asyncio

async def say_hello():
    print("Hello...")
    await asyncio.sleep(1)
    print("...World!")

asyncio.run(say_hello())
```

---

### 💬 Common Interview Questions

**Q1:** What is the GIL, and how does it affect multithreading?
**A:**
The GIL allows only one thread to execute at a time, limiting parallelism for CPU-bound tasks.

**Q2:** When would you prefer multiprocessing over multithreading?
**A:**
Use multiprocessing for **CPU-bound** tasks and multithreading for **I/O-bound** tasks.

**Q3:** How do you share data safely between threads?
**A:**
Use `threading.Lock` or thread-safe data structures like `Queue`.

**Q4:** How do you communicate between processes?
**A:**
Use `multiprocessing.Queue`, `Pipe`, or `Manager`.

**Q5:** How can Python achieve concurrency despite the GIL?
**A:**
Through **I/O-bound threading**, **asyncio**, or **multiprocessing** for parallel CPU work.

---

### ✅ Quick Recap

* **Threads** → Lightweight, shared memory, I/O-bound tasks
* **Processes** → True parallelism, separate memory, CPU-bound tasks
* **GIL** → Restricts simultaneous bytecode execution
* Use **`concurrent.futures`** for cleaner thread/process management
* **`asyncio`** → Great for scalable async I/O tasks

---

# 12. File Handling and Serialization

### 🧠 Overview

File handling allows you to **store, retrieve, and manipulate data** on disk.
Serialization helps **convert Python objects into a storable or transferable format** (like JSON or Pickle).

Interviewers often test this to check how you handle:

* File I/O safely
* Resource management
* Data persistence

---

## 12.1 Opening and Closing Files

Use Python’s built-in `open()` function.

**Syntax:**

```python
open(file, mode)
```

| Mode   | Description                 |
| ------ | --------------------------- |
| `'r'`  | Read (default)              |
| `'w'`  | Write (overwrites)          |
| `'a'`  | Append                      |
| `'b'`  | Binary mode                 |
| `'r+'` | Read and write              |
| `'x'`  | Create file, fail if exists |

**Example:**

```python
file = open("example.txt", "w")
file.write("Hello, Python!\n")
file.close()
```

---

## 12.2 Using `with` Statement (Best Practice)

Using `with` ensures the file is closed automatically.

**Example:**

```python
with open("example.txt", "r") as file:
    data = file.read()
    print(data)
```

This is **equivalent to**:

```python
file = open("example.txt", "r")
try:
    data = file.read()
finally:
    file.close()
```

---

## 12.3 Reading Files

**Example:**

```python
with open("data.txt", "r") as f:
    print(f.read())        # Read entire file
    # f.readline() → reads one line
    # f.readlines() → reads all lines as list
```

---

## 12.4 Writing Files

**Example:**

```python
with open("data.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
```

To **append**:

```python
with open("data.txt", "a") as f:
    f.write("New line added\n")
```

---

## 12.5 Working with Binary Files

**Example:**

```python
with open("image.png", "rb") as f:
    content = f.read()
    print(len(content))  # Number of bytes
```

To write binary data:

```python
with open("copy.png", "wb") as f:
    f.write(content)
```

---

## 12.6 Handling File Paths with `os` and `pathlib`

**Example (using `os`):**

```python
import os

print(os.getcwd())           # Current directory
print(os.path.exists("data.txt"))
os.rename("data.txt", "new_data.txt")
```

**Example (using `pathlib`):**

```python
from pathlib import Path

p = Path("data.txt")
print(p.exists())
print(p.parent)
print(p.suffix)
```

`pathlib` is **modern and object-oriented**, preferred in interviews.

---

## 12.7 JSON Serialization

The `json` module is used for working with JSON data.

**Example:**

```python
import json

data = {"name": "Dheeraj", "age": 25, "skills": ["Python", "Cybersecurity"]}

# Serialize
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# Deserialize
with open("data.json", "r") as f:
    result = json.load(f)

print(result)
```

---

## 12.8 Converting JSON Strings

**Example:**

```python
import json

person = {"name": "Alice", "age": 30}
json_str = json.dumps(person)
print(json_str)  # '{"name": "Alice", "age": 30}'

data = json.loads(json_str)
print(data["name"])  # Alice
```

---

## 12.9 CSV File Handling

Python provides the `csv` module for handling comma-separated data.

**Writing CSV:**

```python
import csv

rows = [
    ["Name", "Age", "City"],
    ["Alice", 30, "London"],
    ["Bob", 25, "Paris"]
]

with open("people.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
```

**Reading CSV:**

```python
import csv

with open("people.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

---

## 12.10 Pickle Serialization (Binary)

`pickle` is used to **serialize Python objects** into bytes.
Unlike JSON, it supports **custom classes and complex objects**.

**Example:**

```python
import pickle

data = {"a": 1, "b": 2, "c": 3}

# Serialize
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

# Deserialize
with open("data.pkl", "rb") as f:
    result = pickle.load(f)

print(result)
```

⚠️ **Security Note:**
Never `pickle.load()` data from untrusted sources — it can execute arbitrary code.

---

## 12.11 Exception Handling in File I/O

**Example:**

```python
try:
    with open("nofile.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File does not exist!")
```

---

## 12.12 Real-World Example: Merging Text Files

**Example:**

```python
files = ["part1.txt", "part2.txt", "part3.txt"]

with open("merged.txt", "w") as outfile:
    for fname in files:
        with open(fname, "r") as infile:
            outfile.write(infile.read() + "\n")
```

---

### 💬 Common Interview Questions

**Q1:** What’s the difference between JSON and Pickle?
**A:**

* JSON → Human-readable, portable
* Pickle → Python-specific, supports complex objects

**Q2:** How do you ensure a file is closed automatically?
**A:**
Use the `with` statement.

**Q3:** What’s the difference between text and binary mode?
**A:**

* Text mode handles strings (`str`)
* Binary mode handles bytes (`bytes`)

**Q4:** What happens if you open a file in write mode (`'w'`)?
**A:**
It truncates (overwrites) the file if it exists.

**Q5:** How can you read large files efficiently?
**A:**
Use iteration:

```python
with open("bigfile.txt") as f:
    for line in f:
        process(line)
```

---

### ✅ Quick Recap

* Use **`with open()`** for safe file handling
* Use **`json`** for text serialization
* Use **`pickle`** for complex Python objects
* Use **`csv`** for tabular data
* Always handle **FileNotFoundError** and **IOError**

---

# 13. Best Practices, Optimization, and Mock Interview Questions


## 13.1 🧩 PEP 8 – Python Coding Standards

PEP 8 is the **official style guide for Python code**.
Interviewers expect you to write **clean, readable, and consistent** code.

**Key Guidelines:**

| Category        | Rule                                   | Example                                                 |
| --------------- | -------------------------------------- | ------------------------------------------------------- |
| **Indentation** | 4 spaces per level                     | ✅ Good: `for i in range(5):`<br>❌ Bad: Use of tabs      |
| **Naming**      | snake_case for variables and functions | `total_count = 0`                                       |
| **Constants**   | UPPERCASE_WITH_UNDERSCORES             | `MAX_RETRIES = 3`                                       |
| **Class names** | PascalCase                             | `class DataParser:`                                     |
| **Line length** | ≤ 79 characters                        | Split long lines with `\`                               |
| **Imports**     | Standard → Third-party → Local         | `import os`, `import requests`, `from app import utils` |
| **Whitespace**  | Avoid extra spaces                     | ✅ `x = a + b`, ❌ `x = a+b`                              |

---

### ✅ Example (PEP 8 Compliant)

```python
import os

def calculate_sum(numbers):
    """Return the sum of a list of numbers."""
    total = 0
    for num in numbers:
        total += num
    return total

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print(calculate_sum(data))
```

---

## 13.2 🧠 Common Optimization Techniques

### 1. Use List Comprehensions

```python
squares = [x**2 for x in range(10)]
```

Instead of:

```python
squares = []
for x in range(10):
    squares.append(x**2)
```

---

### 2. Use Generators for Large Data

```python
def gen_numbers():
    for i in range(10**6):
        yield i
```

Generators **save memory** by yielding one item at a time.

---

### 3. Use Built-in Functions

Leverage Python’s **optimized C-based built-ins**:

```python
sum(data), max(data), sorted(data)
```

---

### 4. Use `set()` for Membership Tests

```python
if item in myset:  # O(1)
```

is faster than list membership `in list` (O(n)).

---

### 5. Use Caching with `functools.lru_cache`

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(35))
```

Dramatically improves recursive function performance.

---

### 6. Profile Your Code

Use `timeit` for micro-benchmarks:

```python
import timeit
print(timeit.timeit("sum(range(1000))", number=1000))
```

Or use `cProfile` for function-level profiling:

```bash
python -m cProfile script.py
```

---

## 13.3 ⚙️ Memory and Performance Best Practices

| Scenario             | Best Practice                     |
| -------------------- | --------------------------------- |
| Large data           | Use generators, not lists         |
| Repeated computation | Cache results (`lru_cache`)       |
| Reused constants     | Use tuples (immutable)            |
| String concatenation | Use `join()` instead of `+`       |
| Big loops            | Use `map()` or list comprehension |
| File handling        | Use `with` to auto-close          |
| Imports              | Import only what’s needed         |

---

## 13.4 🧰 Debugging and Testing

### Debugging

Use the built-in debugger:

```python
import pdb
pdb.set_trace()
```

Or Python 3.7+ shortcut:

```python
breakpoint()
```

### Unit Testing

```python
import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
```

Run tests:

```bash
python -m unittest test_script.py
```

---

## 13.5 🔒 Secure Coding Practices (Important for Cybersecurity Roles)

* Never use `eval()` or `exec()` with untrusted input
* Use parameterized queries (for SQL injection prevention)
* Sanitize input data before processing
* Use the `secrets` module for cryptographic-safe random values
* Validate file paths to avoid directory traversal

---

## 13.6 🎯 Mock Interview Questions

### Q1: Reverse a String Without Using `[::-1]`

```python
def reverse_string(s):
    result = ""
    for char in s:
        result = char + result
    return result

print(reverse_string("python"))  # nohtyp
```

---

### Q2: Find the First Non-Repeated Character

```python
def first_unique_char(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None

print(first_unique_char("aabbcddee"))  # c
```

---

### Q3: Count Frequency of Words in a Sentence

```python
from collections import Counter

def word_count(sentence):
    words = sentence.split()
    return Counter(words)

print(word_count("this is a test this is"))
```

---

### Q4: Fibonacci Sequence (Iterative + Recursive)

```python
def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fib_rec(n):
    if n < 2:
        return n
    return fib_rec(n-1) + fib_rec(n-2)
```

---

### Q5: Check for Palindrome

```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("Never Odd or Even"))  # True
```

---

### Q6: Flatten a Nested List

```python
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([1, [2, [3, 4]], 5]))  # [1, 2, 3, 4, 5]
```

---

### Q7: Find Duplicates in a List

```python
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)

print(find_duplicates([1, 2, 3, 2, 4, 3]))  # [2, 3]
```

---

### Q8: Sort Dictionary by Value

```python
data = {"a": 3, "b": 1, "c": 2}
sorted_data = dict(sorted(data.items(), key=lambda x: x[1]))
print(sorted_data)  # {'b': 1, 'c': 2, 'a': 3}
```

---

## 13.7 🧩 Final Interview Tips

✅ **Before the Interview**

* Brush up on basic syntax and data types
* Practice common coding challenges on LeetCode/HackerRank
* Revise built-in libraries (`collections`, `itertools`, `functools`)

✅ **During the Interview**

* Think aloud — explain your approach before coding
* Write readable code, follow PEP 8
* Optimize *after* your solution works
* Test with small inputs and edge cases

✅ **After the Interview**

* Ask for feedback
* Reflect on tricky questions
* Keep improving weak areas

---









