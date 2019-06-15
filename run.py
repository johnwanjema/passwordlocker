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

def del_account(account):
    '''
    Function to delete an account
    '''
    account.delete_account()

def find_account(name):
    '''
    Function that finds an account by name and returns the account
    '''
    return account.find_by_name(name)

def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return account. display_allaccounts()









def main():
    print("Hello Welcome to password  locker .  Whereyou can save your passwoards")
    
    print('\t')
   

    while True:
        print("Use these short codes : \n su to signup for password locker \n log :to login \n new - create a new account \n dc - display accounts \n del to delete an account \n fc -find an account \n ex -exit the app ")
        short_code = input().lower()

        if short_code == 'su':
                print("New User")
                print("-"*10)

                print ("User  name ....")
                user_name = input()

                print("pasword...")
                password = input()                


                save_user(create_user(user_name,password)) # create and save new user.
                
                print(f"New user {user_name}  created")
                print ('\t')

        
            
            

            
    

if __name__ == '__main__':

    main()