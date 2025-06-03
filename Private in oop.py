class Account:
    def __init__(self, name, password):
        self.Name = name
        self.__Password = password
        
    def get_password(self):
        return self.__Password
         
User = Account("Motobashi", 124345)
print(User.Name)
print(User.get_password()) 
