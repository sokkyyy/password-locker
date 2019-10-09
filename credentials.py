import string
import random
import pyperclip

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

        Args:
            Username: Username to find specific credentials for a single user.

        Returns:
            User_credentials: List of a user's social credentials.
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
        
        Returns:
            password: A randomly generated password.
        '''
        password = ''.join(random.choice(char) for _ in range(passwordLength))
        return password
    
    @classmethod
    def find_by_name(cls, media):
        '''
        Find by social media name method that will return the credential based on its social media name.

        Args:
            Media: The social media account you want to find
        
        Returns:
            dict: A credential dictionary that matches the media argument.
        '''
        for credential in cls.credential_list:
            if credential.social_media == media:
                return credential

    @classmethod
    def copy_password(cls, social_media):
        '''
        Copy password method to copy the desired social media password.
        
        Args:
            Social media: The social media account you want to copy the password for.
        '''
        credential_found = cls.find_by_name(social_media)

        if credential_found:
            pyperclip.copy(credential_found.password)

        