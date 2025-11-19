'''lst = [1,2,3,4,5]
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
#a ='x'
#b ='y'
#print(a+b)  # concatenation of strings -- Output: xy

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

#Module: OOPS/oops_proj.py
from oops_proj import chatbook
#user1 = chatbook()

#Function vs Method
#Function
lst = [1,2,3]  #lst is object of list class
#function to get length of list
a1=len(lst)  #a1 is variable to store length of list
print(a1)

#Method
#A method is simply a function that is defined inside a class and is called using an object of that class.
#user1 = chatbook()
#user1.sendmessage()

'''
Concept	        Example	        Belongs To	            Called As	                Description
Function	    len(lst)	    Built-in / Global	    len(obj)	                Works independently, takes objects as input
Method	    user1.sendmessage()	Inside a Class	        object.method()	            Works on the object’s data
Object	    lst, user1	        Instance of Class	    Created using ClassName()	Real-world entity holding data & methods
'''

'''
Function vs Method (in short)
Term	    Defined Where	        Called Using	        Example
Function	Outside any class	    Just the name	        len(lst)
Method	    Inside a class	        Object + dot notation	user1.sendmessage()

'''

#Magic Methods or Dunder Methods

#Self

#You can create attributes outside the Class as well using object.


#Encapsulation
#In Python encapsulation, that restricts direct access to an object's data and methods. 
#It is implemented using access modifiers to define the visibility of class members (attributes and methods). Python uses naming conventions to indicate the intended level of access:

user1= chatbook()

#print(user1.name)
#print(user1.__name)  #This will raise an AttributeError
print(user1._chatbook__name)  #Accessing private attribute using name mangling

'''Access Modifiers in Python
 In Python, there are three levels of access control for class members:
 
 1. Public Members:
    - No underscore prefix (e.g., name, age).
    - Accessible from anywhere, both inside and outside the class.
    2. Protected Members:
    - Single underscore prefix (e.g., _name, _age).
    - Intended for internal use within the class and its subclasses.
    - Can be accessed from outside, but it's a convention to indicate "use with caution."
    3. Private Members:
    - Double underscore prefix (e.g., __name, __age).
    - Name-mangled to prevent direct access from outside the class.
    - Intended for use only within the class itself.'''
    
#Usually attributes are stored in memory as object.attribute
#Eg:emp(id) --> Accessed as object_name.attribute 

#But in case of Hidden/ Private attribute, it is stored in memory with _classname__attributename. 
# Therefore, to access private attribute, we need to use name mangling.

#Eg:emp(__name) --> Accessed as  object_name._class_name__private_attribute



#Getter and Setter Methods - to access private or hidden attributes
user1 = chatbook()
#Accessing private attribute using getter method
print("Default name is:", user1.get_name())

#Setting new name using setter method
user1.set_name("Agent Smith")

#Accessing updated name using getter method
print("Updated name is:", user1.get_name())


#Static Methods
user1 = chatbook()
print(user1.id)

#Static method can be accessed using class name without creating object.
chatbook.set_id(10) #Manually setting static variable value to 10

user2 = chatbook()
print(user2.id) #Output: 10
user3 = chatbook()
print(user3.id) #Output: 11 

#Inheritance


