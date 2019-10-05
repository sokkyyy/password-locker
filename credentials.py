from user import User

class Credentials(User):
    '''
    Class to instantiate social media credential for users.
    '''
    def __init__(self, social_media, username, password):
        '''
        __init__ method that will allow us to create properties for user social media credential.
        ''' 
        self.social_account = social_media
        self.handle_username = username
        self.password = password