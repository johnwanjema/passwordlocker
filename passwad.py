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
        save_contact method saves contact objects into contact_list
        '''

        user.user_list.append(self)

class credentials:
    """
    Class that generates new instances of Credentials.
    """

    credentials_list = [] # Empty credentials list

    def __init__(self,account_name,password):

        self.account_name = account_name
        self.password = password

    def save_credentials(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        credentials.credentials_list.append(self)
       