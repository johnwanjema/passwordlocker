import random
import string
class user:
    """
    Class that generates new instances of users.
    """

    user_list = [] # Empty user list

    def __init__(self,user_name,password):

        self.user_name = user_name
        self.password = password
    
    def save_user(self):
 
        '''
        save_ user method saves user objects into user_list
        '''

        user.user_list.append(self)


    @classmethod
    def find_by_name(cls,user_name):
        '''
        Method that takes in a name and returns an user that matches that name.

        Args:
            user_name: name to search for
        Returns :
            User that matches the name.
        '''

        for user in cls.user_list:
            if user.user_name == user_name:
                return user

class account:
    """
    Class that generates new instances of account.
    """

    account_list = [] # Empty account list

    def __init__(self,account_name,password):

        self.account_name = account_name
        self.password = password

    def save_account(self):

        '''
        save_account method saves account objects into account_list
        '''

        account.account_list.append(self)

    def delete_account(self):

        '''
        delete_account method deletes a saved account from the account_list
        '''

        account.account_list.remove(self)

    @classmethod
    def display_allaccounts(cls):
        '''
        method that returns the account list
        '''
        return cls.account_list

    @classmethod
    def find_by_name(cls,account_name):
        '''
        Method that takes in a name and returns an account that matches that name.

        Args:
            account_name: account name to search for
        Returns :
            Account that matches the name.
        '''

        for account in cls.account_list:
            if account.account_name == account_name:
                return account

    

