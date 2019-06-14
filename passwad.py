class user:
    """
    Class that generates new instances of users.
    """

    user_list = [] # Empty contact list

    def __init__(user_name,password):

        self.first_name = user_name
        self.last_name = password

class credentialss:
    """
    Class that generates new instances of Credentials.
    """

    credentials_list = [] # Empty contact list

    def __init__(account_name,password):

        self.first_name = account_name
        self.last_name = password
       