import pyperclip
class user:

    user_list = []

    def __init__(self,first_name,last_name,user_name,password):



        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password

    user_list = []
def delete_user(self):



        user.user_list.append(self)
    def delete_user(self):



    user.user_list.append(self)
@classmethod
def find_by_user_name(cls,user_name):


    for user in cls.user_list:
        if user.user_name == user_name:
            return user_name
@classmethod
def user_exist(cls,user_name):

        for user in cls.user_list:
            if user.user_name == user_name:
                return True

        return False
    @classmethod
    def display_user_name(cls)