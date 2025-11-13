# Sample project to understand basic OOPS Encapsulation concept

class chatbook:
    def __init__(self):
    # To define attributes and methods
        self.username=""
        self.password=""
        self.loggedin=False
        self.__name="Default User" #private attribute
        #self.menu() # Call menu method when an object is created
        
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


#Encapsulation
#In Python encapsulation, that restricts direct access to an object's data and methods. 
#It is implemented using access modifiers to define the visibility of class members (attributes and methods). Python uses naming conventions to indicate the intended level of access:

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