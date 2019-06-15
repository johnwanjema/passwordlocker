#!/usr/bin/env python3.6
from passwad import user # Importing the user class
from passwad import account # Importing the account class

#user functions
def create_user(user_name,password):
    '''
    Function to create a new user
    '''
    new_user = user(user_name,password)
    return new_user

def save_user(user):
    '''
    Function to save users
    '''
    user.save_user()


#account functios
def create_account(account_name,password):
    '''
    Function to create a new account
    '''
    new_account = user(account_name,password)
    return new_account


def save_account(account):
    '''
    Function to save accounts
    '''
    account.save_account()









def main():
    print("Hello Welcome to password  locker .  Whereyou can save your passwoards")
    
    print('\n')

    while True:
            print("Use these short codes : su to signup for password locker,log :to login ,new - create a new account credentials, dc - display accounts,del to delete an account, fc -find an account,  ex -exit the app ")

            short_code = input().lower()

            
    

if __name__ == '__main__':

    main()