import sqlite3 as sql

class SqlCalls:
    addUser = """ INSERT INTO users (name, ip, pubKey) VALUES ("{0}", "{1}", "{2}"); """
    updateUser = """ UPDATE users SET ip="{1}", pubKey="{2}" WHERE name="{0}" """
    userInfo = """SELECT * FROM users WHERE name="{0}" LIMIT 1"""
    keyExists = """SELECT count(*) FROM users WHERE name="{0}" """

    @staticmethod
    def AddUserSql(name, ip, pubKey):
        return SqlCalls.addUser.format(name, ip, pubKey)

    @staticmethod
    def UpdateUserSql(name, ip, pubKey):
        return SqlCalls.updateUser.format(name, ip, pubKey)

    @staticmethod
    def GetUserInfoSql(name):
        return SqlCalls.userInfo.format(name)

    @staticmethod
    def KeyExistsSql(name):
        return SqlCalls.keyExists.format(name)


class DataBase:
    def __init__(self, dbFile):
        self.file = dbFile
        self.db = sql.connect(self.file)
        self.dbCursor = self.db.cursor()

    def AddUser(self, name, ip, pubKey):
        sql = SqlCalls.AddUserSql(name, ip, pubKey)
        self.dbCursor.execute(sql)

    def UpdateUser(self, name, ip, pubKey):
        sql = SqlCalls.UpdateUserSql(name, ip, pubKey)
        self.dbCursor.execute(sql)

    def GetUser(self, name):
        sql = SqlCalls.GetUserInfoSql(name)
        self.dbCursor.execute(sql)

        out = self.dbCursor.fetchone()

        return {
            "name": out[0],
            "ip": out[1],
            "pubKey": out[2]
        }

    def KeyExists(self, name):
        sql = SqlCalls.KeyExistsSql(name)
        self.dbCursor.execute(sql)

        if (int(self.dbCursor.fetchone()[0]) > 0):
            return True
        else:
            return False
