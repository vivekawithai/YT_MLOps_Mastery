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
                          1. Press 1 to Login 
                          2. Press 2 to Signin
                          3. Press 3 to Write a post
                          4. Press 4 to Message a friend
                          5. Press Any other key to Logout''')
        if user_input=='1':  #string format 
            pass
        elif user_input=='2':
            pass 
        elif user_input=='3':
            pass
        elif user_input=='4':
            pass
        else:
            print("You have been logged out. Goodbye!")
            exit()

#create object/instance of the class            
obj = chatbook()                 