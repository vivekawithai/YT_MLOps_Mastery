#Sample example of OOPS Overloading concept in Python


#Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

#Child Class inheriting from Amimal class
class Dog(Animal):
    
    def __init__(self):
        self.behavior = "Friendly" #Once new attribute is added in child class constructor , parent class constructor is not inherited.
        
    def speak(self):
       print(f"{self.name} barks.It is very {self.behavior}.") #Therefore, Attribute 'name' from Animal class is not inherited here
    #AttributeError: 'Dog' object has no attribute 'name' will be raised if we try to access name attribute from parent class.

#Create an instance of the child class Dog
dog = Dog()  
dog.speak()  # Output: Buddy barks.  #Dog class uses its own speak method, demonstrating method overriding             


'''
> Constructor Overloading , parent class attributes and methods are not inherited by the child class.
We need to call the parent class constructor inside the child class constructor using super() function.

 
'''

