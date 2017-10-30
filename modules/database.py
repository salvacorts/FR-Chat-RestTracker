import sqlite3 as sql

class DataBase:
    addUser = """ INSERT INTO users (name, ip, pubKey) VALUES (?, ?, ?); """
    updateUser = """ UPDATE users SET ip=?, pubKey=?, creacion=DATETIME("now") WHERE name=? """
    userInfo = """SELECT name, ip, pubkey FROM users WHERE name=? LIMIT 1"""
    keyExists = """SELECT count(*) FROM users WHERE name=? LIMIT 1"""

    def __init__(self, dbFile):
        self.file = dbFile
        self.db = sql.connect(self.file)
        self.dbCursor = self.db.cursor()

    def AddUser(self, name, ip, pubKey):
        self.dbCursor.execute(DataBase.addUser, (name, ip, pubKey,))
        self.db.commit()

    def UpdateUser(self, name, ip, pubKey):
        self.dbCursor.execute(DataBase.updateUser, (name, ip, pubKey,))
        self.db.commit()

    def GetUser(self, name):
        self.dbCursor.execute(DataBase.userInfo, (name,))

        out = self.dbCursor.fetchone()

        return {
            "name": out[0],
            "ip": out[1],
            "pubKey": out[2]
        }

    def KeyExists(self, name):
        self.dbCursor.execute(DataBase.keyExists, (name,))

        if (int(self.dbCursor.fetchone()[0]) > 0):
            return True
        else:
            return False
