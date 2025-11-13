#Sample project to understand static methods in OOPS

#Lets say if we want to give unique identification number or employee id to each employee object 
# created in Chatbook class.


class chatbook:
    #Using Static Variable
    __user_id= 0  # Static  variable to keep track of user IDs
        
    def __init__(self):
    # To define attributes and methods
        #self.user_id =0   #Testing purpose only
        #self.user_id +=1  #incrementing user_id for each object created
            
        self.id = chatbook.__user_id  #Self can not access static variable directly, so we use class name
        chatbook.__user_id += 1
        self.username=""
        self.password=""
        self.loggedin=False
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
            
    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    def set_id(value):
        chatbook.__user_id = value          
            
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
'''
print(user1.user_id)  #Output: 1
user2 = chatbook()  
print(user2.user_id)  #Output: 1

user3 = chatbook()  
print(user3.user_id)  #Output: 1

'''
'''💡 Explanation — Static Variable for Unique ID
user1 = chatbook()
print(user1.id)  # Output: 1
user2 = chatbook()
print(user2.id)  # Output: 2
user3 = chatbook()
print(user3.id)  # Output: 3
'''


user1 = chatbook()
print(user1.id)

#Static method can be accessed using class name without creating object.
chatbook.set_id(10) #Manually setting static variable value to 10

user2 = chatbook()
print(user2.id) #Output: 10
user3 = chatbook()
print(user3.id) #Output: 11 



'''

user_id=0
user_id +=1
print(user1.user_id)
print(user2.user_id)
print(user3.user_id)

It intiated with 0 for each object created and incremented by 1 so output is always 1 for each object.

#To avoid this we can use static method.

#Static Method Explanation

#Static methods are methods that belong to a class rather than any specific instance of that class.
#They can be called on the class itself, without needing to create an instance (object)
#Static methods are defined using the @staticmethod decorator.
#They do not have access to instance-specific data (like self) or class-specific data (like cls).
#They are typically used for utility functions that are related to the class but do not require access  
#to instance or class data.

💡 Example — Static Method for Unique ID 
We can use a static method to generate unique IDs for each employee object created in the Chatbook class.
class chatbook:

class chatbook:
    __user_id= 0  # Static  variable to keep track of user IDs

    def __init__(self):
        self.id = chatbook.__user_id #Self can not access static variable directly, so we use class name
        chatbook.__user_id += 1
        self.username=""
        self.password=""
        self.loggedin=False
        #self.menu() # Call menu method when an object is created
        
        # Now, each time we create a new chatbook object, it will get a unique user_id. 
user1 = chatbook()
print(user1.id)  # Output: 1
user2 = chatbook()
print(user2.id)  # Output: 2
user3 = chatbook()
print(user3.id)  # Output: 3



    user_id = 0  # Class variable to keep track of user IDs

    @staticmethod
    def get_id():
        return chatbook.user_id
    
    def set_id(value):
        chatbook.user_id = value  

    def __init__(self):
        self.user_id = chatbook.generate_user_id()  # Call static method to get unique ID
        self.username=""
        self.password=""
        self.loggedin=False
        #self.menu() # Call menu method when an object is created
        
# Now, each time we create a new chatbook object, it will get a unique user_id. 
user1 = chatbook()
print(user1.user_id)  # Output: 1
user2 = chatbook()
print(user2.user_id)  # Output: 2
user3 = chatbook()
print(user3.user_id)  # Output: 3 

'''
