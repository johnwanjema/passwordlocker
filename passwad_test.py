import unittest # Importing the unittest module
from passwad import user # Importing the user class
from passwad import credentials # Importing the credentials class


class Testuser(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

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
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(user.user_list),1)

    def test_save_multiple_users(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_user.save_user()
            test_user = user("john","4321") # new user
            test_user.save_user()
            self.assertEqual(len(user.user_list),2)
       

class Testcredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

 # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials= credentials("twitter","1234")  # create credentila  object

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            credentials.credentials_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.account_name, "twitter")
        self.assertEqual(self.new_credentials.password, "1234")

    def test_save_credentials(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_credentials.save_credentials() # saving the new user
        self.assertEqual(len(credentials.credentials_list),1)

    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_credentials.save_credentials()
            test_credentials = credentials("john","4321") # new credential
            test_credentials.save_credentials()
            self.assertEqual(len(credentials.credentials_list),2)


if __name__ == '__main__':
    unittest.main()