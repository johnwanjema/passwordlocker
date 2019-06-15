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
        method that returns the credentials list
        '''
        return cls.account_list

    

