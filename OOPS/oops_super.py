#Sample example of OOPS Super() function in Python

#Parent Class
class Animal:
    def __init__(self):
        self.name = "Buddy"
        
    def speak(self):
        print(f"{self.name} makes a sound.")

#Child Class inheriting from Animal class
class Dog(Animal):
    def __init__(self,breed): 
        super().__init__()  # Calling the parent class construcor __init() to inherit attributes
        self.breed = breed
        
    def speak(self):
       super().speak()  # Calling the parent class speak() method 
       print(f"{self.name} barks. It is a {self.breed}.") #Animal attribute inherited from Animal class
       
#Create an instance of the child class Dog
dog = Dog("Golden Retriever")
dog.speak()  #Outut: Buddy makes a sound.
             # Output: Buddy barks. It is a Golden Retriever. Dog class uses its own speak method, demonstrating method overriding
     
'''
Why Super() is used?
> To call parent class methods and constructors in the child class.
> It helps in reusing the code of the parent class without explicitly naming it.
> It is especially useful in multiple inheritance scenarios to avoid confusion.

What happens if we don’t use Super()?
> If we don’t use super(), the child class won’t inherit the parent class’s attributes and methods automatically.   
> We would have to manually call the parent class methods and constructors, which can lead to code duplication and errors.
> In the example above, if we didn’t use super().__init__() in the Dog class,
the name attribute from the Animal class wouldn’t be initialized, 
leading to an AttributeError when we try to access it in the speak() method.

Simple Notes:
> Super() is used only in child class.

Scenario 1: Without super() in child class constructor

#Parent Class
class Animal:
    def __init__(self):
        self.name = "Buddy"
        
    def speak(self):
        print(f"{self.name} makes a sound.")

#Child Class inheriting from Animal class
class Dog(Animal):
    def __init__(self,breed): 
        super().__init__() # Not using super() here
        self.breed = breed
        
    def speak(self):
       #super().speak()  # Not calling the parent class speak() method
       print(f"{self.name} barks. It is a {self.breed}.") #Child class does not inherit 
       Animal attribute 'name' from Animal class.
       
#Create an instance of the child class Dog
dog = Dog("Golden Retriever")
dog.super().speak() # We can't use super() outside the child class. we also can't use super() 
                    by using object of child class.

#Optupt: AttributeError: 'Dog' object has no attribute 'super'

Scenario 2:  By making constuctor speak1() in child class

#Parent Class
class Animal:
    def __init__(self):
        self.name = "Buddy"
        
    def speak(self):
        print(f"{self.name} makes a sound.")

#Child Class inheriting from Animal class
class Dog(Animal):
    def __init__(self,breed): 
        super().__init__() # Not using super() here
        self.breed = breed
        
    def speak1(self):
       super().speak() 
       print(f"{self.name} barks. It is a {self.breed}.") #Child class does not inherit 
       Animal attribute 'name' from Animal class.
       
#Create an instance of the child class Dog
dog = Dog("Golden Retriever")
dog.speak()

#Output: Buddy makes a sound.



> Without super() we can't call parent attributes and methods in child class.
 
#Parent Class
class Animal:
    def __init__(self):
        self.name = "Buddy"
        
    def speak(self):
        print(f"{self.name} makes a sound.")

#Child Class inheriting from Animal class
class Dog(Animal):
    def __init__(self,breed): 
        #super().__init__() # Not using super() here
        self.breed = breed
        
    def speak(self):
       super().speak()  # Calling the parent class speak() method 
       print(f"{self.name} barks. It is a {self.breed}.") #Child class does not inherit 
       Animal attribute 'name' from Animal class.
       
#Create an instance of the child class Dog
dog = Dog("Golden Retriever")
dog.speak()  #Output: AttributeError: 'Dog' object has no attribute 'name'
 
'''        