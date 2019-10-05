import unittest
from user import User
from credentials import Credentials


class TestClasses(unittest.TestCase):
    '''
    Class used to test the User and Credential Classes.
    '''

    def setUp(self):
        '''
        setUp Function that will create a new user and new credential instances and run before any test case.
        '''
        self.new_user = User('Raymond','Ndegwa','sokkyyy','king2020', [])
        self.new_credentials = Credentials('Twitter','sokkyyy','pass2019')
    
    def test_user_init(self):
        '''
        Test method to check if user object is initalizzed properly.
        '''

        self.assertEqual(self.new_user.fName, "Raymond")
        self.assertEqual(self.new_user.lName, "Ndegwa")
        self.assertEqual(self.new_user.username, "sokkyyy")
        self.assertEqual(self.new_user.password, "king2020")
        self.assertEqual(self.new_user.credentials, [])
    
    def test_credential_init(self):
        '''
        Test method to check if user credentials are initialized properly.
        '''
        self.assertEqual(self.new_credentials.social_account, 'Twitter')
        self.assertEqual(self.new_credentials.handle_username, 'sokkyyy')
        self.assertEqual(self.new_credentials.password, 'pass2019')

    def test_save_user(self):
        '''
        Test method to check if user is saved successfully
        '''
        self.new_user.save_user() 

        self.assertEqual(len(User.user_list), 1)
    
    # Continue from HERE
    def test_save_credentials(self):
        '''
        Test method to check if the user credentials are saved to their user information.
        '''
        credentials = self.new_credentials.save_credentials()
        print(credentials)  
        self.assertEqual(len(User.user_list.credentials), 1)
    
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
        correct_user_info = User.login_authentication("sokkyyy","king2020") 
        self.assertTrue(correct_user_info)

    





if __name__ == "__main__":
    unittest.main()