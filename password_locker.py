#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

def create_user(fName, lName, username, password):
    '''
    Function to create new user.
    '''
    new_user = User(fName, lName, username, password)
    return new_user

def save_users(user):
    '''
    Function to save user.
    '''
    user.save_user()

def authenticate_user(username, password):
    '''
    Function to authenticate user log-in information.
    '''
    user = User.login_authentication(username, password)
    return user

def create_credentials(username, social_media, social_username, password):
    '''
    Function to create new credentials for users
    '''
    new_credential = Credentials(username, social_media, social_username, password)
    return new_credential

def generate_password():
    '''
    Function to generate 7 character alphanumeric passwords for users.
    '''
    return Credentials.generate_password()

def save_credentials(credential):
    '''
    Function to save new credential.
    '''
    credential.save_credentials()

def delete_credentials(credential):
    '''
    Function to delete a credential.
    '''
    credential.delete_credentials()

def display_credentials(username):
    '''
    Function to display a user's credentials
    '''
    return Credentials.display_credentials(username)

def find_by_name(socialMedia):
    '''
    Function to find credential using social media name.
    '''
    return Credentials.find_by_name(socialMedia)

#main function to execute the application
def main():
    print("-"*120)
    print('\n')
    print("HELLO!! Welcome to Password locker, An application to manage your social media passwords")
    print('\n')
    
    while True:
        print("-"*120)
        print('Use these short codes: \n ca --> To create an account \n lg --> To log into your account \n ex --> To exit')
        print("-"*60)
        short_code = input().lower()

        # Exit
        if short_code == 'ex':
            break
        
        # Create Account
        elif short_code == 'ca':
            print('-'*60)
            print('To create a new account:')
            print('-'*60)
            
            print('Enter your First Name:')
            fName = input()

            print('Enter your Last Name:')
            lName = input()

            print('Enter a Username:')
            username = input()

            print('Enter your Password:')
            password = input()

            # Create and save user
            save_users(create_user(fName, lName, username, password))
            print('-'*60)
            print(f"Account for '{username}' has been created and the password is: {password}")
            print('-'*60)
        
        # Log in 
        elif short_code == 'lg':
            print('-'*60)
            print('To log in to your account, Enter your Username and Password:')
            print('-'*60)

            #Verify User
            print('Enter your username:')
            username = input()

            print('Enter you password:')
            password = input()

            user = authenticate_user(username, password)

            if user: 
                print('-'*60)
                print(f'Welcome {user.username}')
                print('-'*60)
                print('Choose the options below to navigate through the application:')
                print('-'*60)
                
                while True:
                    print('Use these short codes:')
                    print(' cc --> create credentials \n dc --> display credentials \n del --> delete credentials \n lo --> log out')
                    print('-'*60)
                    short_code = input().lower()
  
                    if short_code == 'lo':
                        print('-'*60)
                        print(f'Goodbye {user.username}')
                        print('-'*60)
                        break
                    
                    elif short_code == 'cc':
                        print('-'*60)
                        print('Enter the Name of the Social Media:')
                        social_media = input()
                        print('Enter the Username of the Social Media account:')
                        username = input()


                        while True:
                            print('-'*60)
                            print('Use these short codes for the Password:')
                            print(' gen --> automatically generate password \n ent --> enter your own password')
                            print('-'*60)
                            password_option = input().lower()

                            if password_option == 'gen':
                                password = generate_password()
                                break
                            elif password_option == 'ent':
                                print('Enter your password:')
                                password = input()
                                break
                            else:
                                print('Wrong code. Try again')
                        
                        save_credentials(create_credentials(user.username, social_media, username, password))
                        print('-'*60)
                        print('\n')
                        print(f'Credentials for "{social_media}" with username "{username}" and password "{password}" has been created.')
                        print('\n')
                        print('-'*60)
                    
                    elif short_code == 'dc':
                        print('-'*60)
                        if display_credentials(user.username):
                            print('Your social media credentials include:')

                            count = 0
                            for credential in display_credentials(user.username):
                                count += 1
                                print(f' {count}. Social Media: {credential.social_media}, Username: {credential.social_username}, Password: {credential.password}.')
                                print('-'*60)
                        else:
                            print('-'*60)
                            print('You don\'t have any credentials.')
                            print('-'*60)
                    
                    elif short_code == 'del':
                        print('-'*60)
                        print('Enter the Name of the social media you want to delete:')
                        social = input()
                        if find_by_name(social):
                            delete_credentials(find_by_name(social))
                            print('-'*60)
                            print('Credential has been deleted.')
                            print('-'*60)
                        else:
                            print('-'*60)
                            print('You dont a credential of the specified name.')
                    else: 
                        print('-'*60)
                        print('Please use only the short codes that you have been provided')
            else:
                print('-'*60)
                print('The user information you entered doesn\'t exist. Enter correct log-in credentials.')
        else:
            print('-'*60)
            print('Please use only the short codes that you have been provided')



                        




if __name__ == "__main__":
    main()