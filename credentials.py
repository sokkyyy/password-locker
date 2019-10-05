from user import User

class Credentials(User):
    '''
    Class to instantiate social media credential for users.
    '''
    def __init__(self, username, social_media, social_username, password):
        '''
        __init__ method that will allow us to create properties for user social media credential.
        '''
        self.username = username 
        self.social_media = social_media
        self.social_username = social_username
        self.password = password