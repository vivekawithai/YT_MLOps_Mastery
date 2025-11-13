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
       print(f"{self.name} barks. It is a {self.breed}.") #Child class does not inherit Animal attribute 'name' from Animal class.
       
#Create an instance of the child class Dog
dog = Dog("Golden Retriever")
dog.super().speak() # We can't use super() outside the child class. we also can't use super() 
                    #by using object of child class.