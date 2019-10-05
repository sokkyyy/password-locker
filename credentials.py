from user import User

class Credentials(User):

    credential_list = []

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
    
    def save_credentials(self):
        '''
        Save credentials method that will save credentials to the credential list.
        '''
        Credentials.credential_list.append(self)