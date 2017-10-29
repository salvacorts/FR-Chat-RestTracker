from modules.users import User

class UsersDB:
    users = {}

    def AddUser(self, user):
        self.users[user.name] = user

    def GetUser(self, name):
        return self.users[name];

    def KeyExists(self, name):
        return name in self.users
