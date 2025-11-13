# Sample example of OOPS Inheritance concept

#Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

#Child Class inheriting from Amimal class
class Dog(Animal):
    def speak(self):
       print(f"{self.name} barks.") #Animal attribute inherited from Amimal class

'''
For test purpose, you can uncomment the below Dog class which does not override the speak method 
of Animal class

class Dog(Amimal):
    def speak(self):
        print(f"{self.name} barks.") #Animal attribute inherited from Animal class

'''

#Create an instance of the parent class Animal
animal = Animal("Generic Animal")
animal.speak()  # Output: Generic Animal makes a sound. 

#Create an instance of the child class Dog
dog = Dog("Buddy")  
dog.speak()  # Output: Buddy barks.  #Dog class uses its own speak method, demonstrating method overriding 

'''
dog = Dog("Max")
dog.speak()  # Output: Max makes a sound.  #Dog class inherits speak method from Animal class     
'''              


'''
Why Inheritance is used?

> Code Reuability: Inheritance allows you to reuse existing code. You can create a new class based on an 
existing class, inheriting its attributes and methods, which saves time and effort.

> Parent has no access to Child class attributes and methods.

What gets inherited?
> Attributes and methods of the parent class are inherited by the child class. Also Non private attributes 
and methods i.e., those not prefixed with double underscores (__) are inherited.

#Parent Class
class Animal:
    def __init__(self, name):
        self.__name = name

    def speak(self):
        print(f"{self.__name} makes a sound.")

#Child Class inheriting from Animal class
class Dog(Animal):
    def speak(self):
       print(f"{self.__name} barks.") #Animal attribute inherited from Animal class

animal = Animal("Generic Animal")
animal.speak()  # Output: Generic Animal makes a sound. 

#Create an instance of the child class Dog
dog = Dog("Buddy")  
dog.speak() # Output: Error - 'Animal' object has no attribute '__name'

> Constructors are not inherited by default, but you can call the parent class constructor from the child
class using super().

#Method Overriding

Here in the sample example, Dog class has its own speak() method which overrides the speak() method of
Animal class. This is called method overriding.
 

'''