#initiate a class

class Employee:
    #special method/magic method/dunder method -constructor
   
    def __init__(self):
        print("Started executing Employee class attibutes or data members")
        self.id = 101
        self.salary = 50000
        self.designation = "Developer"
        print("Completed executing Employee class attibutes or data members")
        
    def travel(self,destination):
        print("This travel funtion is called manually by object")
        print(f"Employee is travelling to {destination}")
    
#create object/instance of the class
john = Employee()
#print(john.id,john.salary,john.designation)

#accessing method using object
john.travel("New York")

print(type(john))
    
''' Notes:
👉Class: A blueprint that defines how objects are created and what data (attributes) and actions (methods) they have.

👉Attribute: Variables inside a class that are called (created) automatically when the object is created.

👉Object: A real instance of a class that automatically runs the constructor (__init__) when created.

👉Method: A function defined inside a class that performs actions using the object’s data and must be called manually (unless it’s a special method).

👉If you want to call john.travel() without arguments, you must give a default value in the method definition, like:

def travel(self, destination="Unknown"):
    print(f"Employee is travelling to {destination}")

Then both work:

john.travel("London")   # uses passed argument
john.travel()           # uses default "Unknown"

👉f-string, meaning any expression inside {} will be evaluated and replaced with its actual value.
'''    
'''
🔹 Constructor — What It Is

A constructor (__init__ method in Python) is a special method that runs automatically when you create an object of a class.

🔹 Real Use / Purpose

Initialize object data (attributes)
It sets up the initial state of the object — gives your object all the variables it needs from the start.

class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary
john = Employee("John", 101, 50000)


➡️ The constructor gives john his data immediately — no need to assign values later.

Automatic setup / avoid repetitive code
Without a constructor, you’d have to manually set attributes every time:

john = Employee()
john.name = "John"
john.id = 101
john.salary = 50000


That’s extra typing and error-prone.
Constructor = cleaner, safer, and automatic setup.

Ensure required data is provided
You can make sure all important info is passed when creating the object.
If someone forgets, Python throws an error — preventing incomplete objects.

Perform setup actions
You can run setup tasks like connecting to a database, opening files, initializing lists, etc.

def __init__(self):
    print("Connecting to server...")

🔹 In short

👉 The constructor’s real use is to automatically prepare and initialize an object’s data or environment the moment it’s created, 
saving you from manual setup and ensuring every object starts in a valid state'''

'''
Why Python is Object-Oriented ?
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

'''
Advantages of Object-Oriented Programming (OOP) in Python:
> You can create custom data types.
> Code reusability through inheritance.
> Debugging is easier with encapsulation.
> Easy to collab. 

'''