
# Password Locker
This project was built by [Python 3.6](https://github.com/python).

## Description
Password Locker is an application that runs on the Terminal of your computer. The application allows users to create accounts that can be used to store their various Social Media credentials.

### User Stories
Users can:
* Create an account with their details and specify their log in username and password.
* Store their existing social media credentials.
* Create new social media credentials and use automatically generated passwords or enter their own password.
* View a list of their credentials if they have saved them.
* Delete the credentials they no longer need.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for testing purposes.

### Prerequisites 
* python3.6
* pip
* git

### Clone
Run this command in your Terminal:
```
$ git clone https://github.com/sokkyyy/password-locker.git
$ cd password-locker
```
### Running the Application
To run the application in the Terminal:
```
$ chmod +x password_locker.py
$ ./password_locker.py
```
### Commands for the System
| Short Code | Meaning                | 
|------------|------------------------|
| ca         |create account          |
| lg         |log in                  |
| ex         |exit the system         |
| cc         |create new credentials  | 
| dc         |display credentials     |
| del        |delete credentials      |
| lo         |log out                 |
| gen        | generetae password     |
| ent        | enter your own password|
## Running Tests
In order to run tests for the system, in your Terminal run:
```
$ python3.6 testClasses.py
```

## Built With
* Python 3.6

## Author
* **Raymond Ndegwa** - [GitHub](https://github.com/sokkyyy).

## Acknowledgement
* Moringa School.
