lst = [1,2,3,4,5]
print(lst)
print(type(lst))

my_str = "hello, world!"
print(type(my_str))

my_str1=my_str.capitalize() # Capitalizes the first letter of the string
print(my_str1)

my_int = 42
print(type(my_int))

lst.append(6)
print(lst)

'''
Notes:  Why Python is Object-Oriented ?

Everything in Python is an Object
In Python, everything is an object, including:
- Data types (like lists, strings, integers) 
- Functions
- Classes
- Data structures 
- Modules
- Even code itself
This means they all have attributes and methods you can use.
For example, lst is a list object with methods like append() to add items.

'''

a ='x'
b ='y'
print(a+b)  # concatenation of strings -- Output: xy

'''
how Python treats variables like a = 'x', b = 'y' as strings, not as algebraic symbols (like in math).

Let’s clarify that properly 👇

🧩 Your Example
a = 'x'
b = 'y'
print(a + b)


Output:

xy


✅ Here, + performs string concatenation, not algebraic addition — because 'x' and 'y' are strings (text), not algebraic symbols.

💡 Explanation

In Python, variables like 'x' or 'y' have no mathematical meaning unless you explicitly define how they should behave.
That’s why we say:

Python does not have algebraic data types (like symbolic variables) by default.

But — we can create our own data types or use libraries that give that behavior.

🧠 Example — Creating Your Own Algebraic Type

You can use a class to make Python understand algebraic-like symbols:

class Symbol:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return f"{self.name} + {other.name}"

a = Symbol('x')
b = Symbol('y')
print(a + b)


Output:

x + y


Now, a + b behaves algebraically — not like string concatenation.

✅ In simple words:

In Python, 'x' and 'y' are just strings — so a + b joins them as text.
Python doesn’t have algebraic types built in, but we can create our own custom data types (like Symbol) to behave algebraically.

'''
