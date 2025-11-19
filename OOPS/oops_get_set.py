# Sample project to understand basic OOPS Getter Setter methods to access private attributes

class chatbook:
    def __init__(self):
    # To define attributes and methods
        self.username=""
        self.password=""
        self.loggedin=False
        self.__name="Default User" #private attribute
        #self.menu() # Call menu method when an object is created
    
    def get_name(self):
        return self.__name #__name is private attribute and can be accessed here like this within class only.
    
    def set_name(self, value):
        self.__name = value   
        
    def menu(self):
        #user_input = input("Welcome to  Chatbook ! How you would like to proceed? \n 1. Press 1 to Login \n 2. Signup \n 3. Press 3 to write a post"")    
        
        user_input =input('''Welcome to  Chatbook ! How you would like to proceed? 
                          1. Press 1 to Signup 
                          2. Press 2 to Signin
                          3. Press 3 to Write a post
                          4. Press 4 to Message a friend
                          5. Press Any other key to Logout   ''')
        if user_input=='1':  #here 1 is taken in string format 
            self.signup()
        elif user_input=='2':
            self.signin() 
        elif user_input=='3':
            self.mypost()
        elif user_input=='4':
            self.sendmessage()
        else:
            print("You have been logged out. Goodbye!")
            exit()
            
    def signup(self):
        email = input("Enter your email : ")
        pwd = input("Setup your password : ")
        self.username = email  
        self.password = pwd 
        print("Signup successful! You can now Signin.") 
        print("\n")
        self.menu()
    
    def signin(self):
        '''if not self.username or not self.password:
            print("No user found. Please signup first.")
            self.menu()
            return '''
            
        if self.username=="" or self.password=="":
            print("No user found. Please signup first by selecting Pressing 1 in the main menu.")
        else:
            uname = input("Enter your email : ") 
            pwd = input("Enter your password : ")
            if self.username==uname and self.password==pwd:
                print("Signin successful! Welcome back.")
                self.loggedin=True 
            else:
                print("Enter correct credentials. Please try again.")    
        print("\n")      
        self.menu()
        
    def mypost(self):
        if self.loggedin == True:
            post_content = input("Write your post here: ")
            print("Your post has been published!")
        else:
            print("Please signin to write a post.")
        print("\n")
        self.menu()   
        
    def sendmessage(self):
        if self.loggedin == True:
            friend = input("Enter your friend's name to send message: ")
            message = input("Type your message: ")
            print(f"Message sent to {friend}!")
        else:
            print("Please signin to send messages.")
        print("\n")
        self.menu()   
            
#create object/instance of the class            
user1 = chatbook()      

#Accessing private attribute using getter method
print("Default name is:", user1.get_name())
print(id(user1))

#Setting new name using setter method
user1.set_name("Agent Smith")

#Accessing updated name using getter method
print("Updated name is:", user1.get_name())
print(id(user1))

'''
Notes on Getter and Setter Methods:

id(user1)

The id() function in Python returns the memory address (identity) of an object.

This address remains the same as long as the object exists in memory.

🧩 In your case

✅ user1 is an object (instance of a class).
✅ When you call set_name("Agent Smith"), you are modifying an attribute of that object, not creating a new object.

So:

Before setter → the object exists at memory address X

After setter → the same object now has a modified internal attribute (still at memory address X)

Conclusion:
The object’s ID (memory address) stays the same,
only its internal data (attributes) changes.

⚙️ Analogy

Think of user1 like a box —
you can change what’s inside the box,
but the box itself stays in the same place in memory.

'''