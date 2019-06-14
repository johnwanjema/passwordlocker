class user:
    """
    Class that generates new instances of users.
    """

    user_list = [] # Empty user list

    def __init__(self,user_name,password):

        self.user_name = user_name
        self.password = password

class credentials:
    """
    Class that generates new instances of Credentials.
    """

    credentials_list = [] # Empty credentials list

    def __init__(self,account_name,password):

        self.account_name = account_name
        self.password = password
       