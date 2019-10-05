import string
import random


class Credentials():

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
    
    def delete_credentials(self):
        '''
        Delete credentials method that will remove specific credentials from credential list.
        '''
        Credentials.credential_list.remove(self)

    @classmethod
    def display_credentials(cls, username):
        '''
        Display credentials method that will display a specific user's credentials.
        '''
        user_credentials = []
        for credential in cls.credential_list:
            if credential.username == username:
                user_credentials.append(credential)
        return user_credentials
    
    @classmethod
    def generate_password(cls, passwordLength=7, char=string.ascii_letters+string.digits):
        '''
        Generate password method that will generate an alphanumeric password if the user needs one.
        '''
        password = ''.join(random.choice(char) for _ in range(passwordLength))
        return password
        