import unittest
from user import User
from credentials import Credentials


class TestUser(unittest.TestCase):
    '''
    Class used to test User class.
    '''

    def setUp(self):
        '''
        setUp Function that will create a new user and new credential instances and run before any test case.
        '''
        self.new_user = User('Raymond','Ndegwa','sokkyyy','king2020')
    
    def test_user_init(self):
        '''
        Test method to check if user object is initalizzed properly.
        '''

        self.assertEqual(self.new_user.fName, "Raymond")
        self.assertEqual(self.new_user.lName, "Ndegwa")
        self.assertEqual(self.new_user.username, "sokkyyy")
        self.assertEqual(self.new_user.password, "king2020")
    
    def test_save_user(self):
        '''
        Test method to check if user is saved successfully
        '''
        self.new_user.save_user() 
        user2 = User('Martin', 'Maina', 'marto','king2020')
        user2.save_user()

        self.assertEqual(len(User.user_list), 2)
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run
        '''
        User.user_list = []
    
    def test_login_authentication(self):
        '''
        Test method that will check if the username is correctly authenticated.
        '''
        self.new_user.save_user()
        user2 = User('Martin', 'Maina', 'marto','king2020')
        user2.save_user()

    
        for user in User.user_list:
            if user.password == user2.password and user.username == user2.username:
                current_user = user
                return current_user
        
        self.assertEqual(current_user, User.login_authentication(user2.username, user2.password))


class TestCredentials(unittest.TestCase):
    '''
    Test Class to test the Credentials class.
    '''
    def setUp(self):
        '''
        setUp method to create new instance of a credential object before each test.
        '''
        
        self.new_credentials = Credentials('sokkyyy','Twitter','ndegwaRay','pass2019')
    
    def test_credential_init(self):
        '''
        Test method to check if user credentials are initialized properly.
        '''
        self.assertEqual(self.new_credentials.username, 'sokkyyy')
        self.assertEqual(self.new_credentials.social_media, 'Twitter')
        self.assertEqual(self.new_credentials.social_username, 'ndegwaRay')
        self.assertEqual(self.new_credentials.password, 'pass2019')
    
    def test_save_credentials(self):
        '''
        Test method to check if credentials are saved in the credential list.
        '''
        self.new_credentials.save_credentials()
        instagram = Credentials('sokkyyy','Insta','superman','password')
        instagram.save_credentials()

        self.assertEqual(len(Credentials.credential_list), 2)
    
    def tearDown(self):
        '''
        Tear Down method that cleans up the credential list after each test.
        '''
        Credentials.credential_list = []
    
    def test_display_credentials(self):
        '''
        Test method to check if correct credentials are displayed for specific user.
        '''
        self.new_credentials.save_credentials()
        instagram = Credentials('sokkyyy','Insta','superman','password')
        instagram.save_credentials()

        self.assertEqual(len(Credentials.display_credentials(instagram.username)), 2) 
    
    def test_delete_credentials(self):
        '''
        Test method to check if correct credential is removed from credential list.
        '''
        self.new_credentials.save_credentials()
        instagram = Credentials('sokkyyy','Insta','superman','password')
        instagram.save_credentials()

        instagram.delete_credentials() 
        self.assertEqual(len(Credentials.credential_list), 1)
    
    def test_generate_password(self):
        '''
        Test method that will check if a password is generated for the user if they wish.
        '''
        gmail = Credentials('superman','Gmail', "sups@gmail.com",'')
        gmail.password = Credentials.generate_password() 

        self.assertTrue(gmail.password)




     

    





if __name__ == "__main__":
    unittest.main()