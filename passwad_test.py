import unittest # Importing the unittest module
from passwad import user # Importing the user class
from passwad import credentialss # Importing the credentilas class


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

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name, "James")
        self.assertEqual(self.new_user.password, "1234")
       
       
if __name__ == '__main__':
    unittest.main()