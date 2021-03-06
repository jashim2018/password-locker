import unittest
# import pyperclip
from user import User

class TestUser(unittest.TestCase):
    
    def setUp(self):
         
         
          self.new_user = User("Patrick","Buong","Patoh Patrick","pachecoh")
          
          
          
    def test_init(self):
          
        self.assertEqual(self.new_user.first_name,"Patrick")
        self.assertEqual(self.new_user.last_name,"Buong")
        self.assertEqual(self.new_user.user_name,"Patoh Patrick")
        self.assertEqual(self.new_user.password,"pachecoh")
     
               
         
    def test_save_user(self):
       
        self.new_user.save_user() 
        self.assertEqual(len(User.user_list),1)
        
    def test_save_multiple_user(self):
       
        self.new_user.save_user()
        test_user = User("Facebook","Patrick","Patoh Patrick","Pachecoh") 
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
    
    def tearDown(self):
         
         User.user_list = []

    def test_delete_user(self):
        
         self.new_user.save_user()
         test_user = User("Facebook","Patrick","Patoh Patrick","Pachecoh") 
         test_user.save_user()

         self.new_user.delete_user()
         self.assertEqual(len(User.user_list),1)
    #  def test_find_user_by_username(self):
    def test_save_user_by_username(self):    

        self.new_user.save_user()
        test_user = User("Facebook","Patrick")
        test_user.save_user()

        found_user = User.find_by_user_name("Patoh Patrick")

        self.assertEqual(found_user.user_name,test_user.user_name)
    def test_user_exists(self):
         
        self.new_user.save_user()
        test_user = User("Patoh Patrick") 
        test_user.save_user()

        user_exists = User.user_exist("Patoh Patrick")

        self.assertTrue(user_exists)
    def test_display_all_users(self):
       

         self.assertEqual(User.display_user(),User.user_list)
   
    def test_copy_password(self):
         

         self.new_user.save_user()
         User.copy_password("")

         self.assertEqual(self.new_user.password,pyperclip.paste())

if __name__ ==  '__main__':
 unittest.main()