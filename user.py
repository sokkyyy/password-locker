class User:
    '''
    Class to instatiate new users for Password Locker application
    '''
    user_list = [] # Store for the applications users.

    def __init__(self, fName, lName, username, password):
        '''
        __init__ method that will allow us to create properties for users.

        Args:
            fName: New user first name.
            lName: New user last name.
            username: New user username.
            password: New user password.
        '''

        self.fName = fName
        self.lName = lName
        self.username = username
        self.password = password
    
    def save_user(self):
        '''
        save_user method to save user information for the application.
        '''
        User.user_list.append(self)
    
    
    @classmethod
    def login_authentication(cls, name, password):
        '''
        Method that takes in username and returns a Boolean based on whether it found a user(True) or not(False).
        Args:
            name: Username to authenticate if user exists in application
            password: User password to authenticate if its same user's password
        Returns:
            True if user is found and False if not found.
        '''
        for user in cls.user_list:
            if user.username == name and user.password == password:
                return user
        
    


