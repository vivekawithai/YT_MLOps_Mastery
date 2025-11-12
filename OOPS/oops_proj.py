# Sample project to understand basic OOPS concepts

class chatbook:
    def __init__(self):
    # To define attributes and methods
        self.username=""
        self.password=""
        self.loggedin=False
        self.menu() # Call menu method when an object is created
        
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
#user1 = chatbook()                 