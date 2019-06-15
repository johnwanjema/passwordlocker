import unittest # Importing the unittest module
from passwad import user # Importing the user class
from passwad import account # Importing the account class
import random
import string


class Testuser(unittest.TestCase):

    '''
    Test class that defines test cases for the account class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

 # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user= user("James","1234")  # create user  object

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            user.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name, "James")
        self.assertEqual(self.new_user.password, "1234")


    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(user.user_list),1)

    def test_save_multiple_users(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = user("john","4321") # new user
            test_user.save_user()
            self.assertEqual(len(user.user_list),2)

    def test_find_user_by_name(self):
        '''
        test to check if we can find an user by name
        '''

        self.new_user.save_user()
        test_user = user("james","3425") # new user
        test_user.save_user()

        found_user = user.find_by_name("james")

        self.assertEqual(found_user.user_name,test_user.user_name)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = user("Test","3344",) # new user
        test_user.save_user()

        user_exists = user.user_exist("Test","3344")

        self.assertTrue(user_exists)
       

class Testaccount(unittest.TestCase):

    '''
    Test class that defines test cases for the account class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

 # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account= account("twitter","1234")  # create credentila  object

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            account.account_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.account_name, "twitter")
        self.assertEqual(self.new_account.password, "1234")

    def test_save_account(self):
        '''
        test_save_account test case to test if the user object is saved into
         the user list
        '''
        self.new_account.save_account() # saving the new user
        self.assertEqual(len(account.account_list),1)

    def test_save_multiple_account(self):
            '''
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
            self.new_account.save_account()
            test_account = account("instagram","4321") # new credential
            test_account.save_account()
            self.assertEqual(len(account.account_list),2)
   
    def test_delete_account(self):
            '''
            test_delete_account to test if we can remove a account from our accountlist
            '''
            self.new_account.save_account()
            test_account = account("facebook","4321") # new account
            test_account.save_account()
            self.new_account.delete_account()# Deleting a account object
            self.assertEqual(len(account.account_list),1)

    def test_display_allaccounts(self):
        '''
        test for method that returns 
        all accounts saved
        '''
        self.assertEqual(account.display_allaccounts(),account.account_list)

    def test_find_account_by_name(self):
        '''
        test to check if we can find an account by name
        '''

        self.new_account.save_account()
        test_account = account("snapchat","paswa") # new account
        test_account.save_account()

        found_account = account.find_by_name("snapchat")

        self.assertEqual(found_account.account_name,test_account.account_name)
    
    def test_account_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account.
        '''

        self.new_account.save_account()
        test_account = account("Test","3344",) # new account
        test_account.save_account()

        account_exists = account.account_exist("Test")

        self.assertTrue(account_exists)

    def test_account_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account.
        '''

        self.new_account.save_account()
        test_account = account("Test","3344",) # new account
        test_account.save_account()

        account_exists = account.account_exist("Test")

        self.assertTrue(account_exists)

    
        
    



if __name__ == '__main__':
    unittest.main()