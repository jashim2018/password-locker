class credential:
    """
    Class that generates new instances of users
    """
    credentials_list  = []

    def __init__(self,credential_name,user_name,password,email):
        self.credential_name = credential_name
        self.user_name = user_name
        self.password = password
        self.email = email

    def save_credential(self)



        Credential.credential_list.append(self)
    

    def delete_credential(self)



        Credential.credential_list.remove(self)


    @classmethod
    def find_name_by_name(cls,name):
        