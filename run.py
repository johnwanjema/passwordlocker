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

def login(password):
    """
    function to login
    """
    return  user.find_by_name(password)

def check_existing_user(user_name):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return user.user_exist(user_name)

def find_user(user_name):
    '''
    Function that finds an account by name and returns the account
    '''
    return account.find_by_name(user_name)



#account functios
def create_account(account_name,password):
    '''
    Function to create a new account
    '''
    new_account = account(account_name,password)
    return new_account


def save_account(account):
    '''
    Function to save accounts
    '''
    account.save_account()

def delete_account(account):
    '''
    Function to delete an account
    '''
    account.delete_account()

def find_account(account_name):
    '''
    Function that finds an account by name and returns the account
    '''
    return account.find_by_name(account_name)

def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return account. display_allaccounts()

def check_existing_accounts(account_name):
    '''
    Function that check if a account exists with that number and return a Boolean
    '''
    return account.account_exist(account_name)

def find_account(account_name):
    '''
    Function that finds an account by name and returns the account
    '''
    return account.find_by_name(account_name)









def main():
    print("Hello Welcome to password  locker .  Whereyou can save your passwoards")
    
    print('\t')
   

    while True:
        print("Use these short codes : \n su to signup for password locker \n log :to login  \n ex -exit the app ")
        print("\t")
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

        elif short_code == 'log':
                print("input username and password to login")
                print("-"*100)
                print("input username")
                user_name = input()
               
                
                print("pasword...")
                password = input()
                if check_existing_user(user_name):
                        search_user = find_user(user_name)                        
                        print('-' * 20)
                        while True:
                                print("Use these short codes\n new - create a new account \n dc - display accounts \n del to delete an account \n fc -find an account")
                                short_code1 = input().lower()                              
                                

                                if short_code1 == 'new':
                                        
                                        print ("Account name ....")
                                        account_name = input()

                                        print("pasword...")
                                        password = input()

                                        save_account(create_account(account_name,password))
                                        print(f"New user {user_name}  created") 

                                elif short_code1 == "dc":
                                        if display_accounts():
                                                print("Here is a list of all your contacts")
                                                print('\n')

                                                for account in display_accounts():
                                                        print(f"{account.account_name} {account.password} ")

                                                print('no accounts yet')
                                
                                elif short_code1 == "del":
                                       
                                                print("Enter the number you want to delete")
                                                search_number = input()
                                                if check_existing_accounts(account_name):
                                                        search_account = find_account(account_name)
                                                        delete_account(search_account)
                                                        print("account deleted")
                                                else:
                                                        print('account does not exsit')  
                                else:
                                        print('\n')
                                        print("You dont any account  yet")
                                        print('\n')
                                
                                

                        else:
                                print("That user does not exist or you have input a wrong password or username")
                                print('\n')
        else:
                print("wrong short code try again")
                
        


        
            
            

            
    

if __name__ == '__main__':
  main()