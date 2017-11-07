from modules.keyring import *
import sqlite3 as sql


class DataBase:
    addUser = """ INSERT INTO users (name, ip, port, pubKey) VALUES (?, ?, ?, ?); """
    updateUser = """ UPDATE users SET ip=?, port=?, creacion=DATETIME("now") WHERE name=? """
    userInfo = """SELECT name, ip, port, pubkey FROM users WHERE name=? LIMIT 1"""
    keyExists = """SELECT count(*) FROM users WHERE name=? LIMIT 1"""

    def __init__(self, dbFile):
        self.file = dbFile
        self.db = sql.connect(self.file)
        self.dbCursor = self.db.cursor()

    def AddUser(self, name, ip, port, pubKey):
        self.dbCursor.execute(DataBase.addUser, (name, ip, port, pubKey,))
        self.db.commit()

    def UpdateUser(self, name, ip, port, validationMSG):
        currentPubKey = self.GetUser(name)["pubKey"]

        if not ValidCredentials(currentPubKey, validationMSG):
            return False

        self.dbCursor.execute(DataBase.updateUser, (ip, port, name,))
        self.db.commit()
        return True

    def GetUser(self, name):
        self.dbCursor.execute(DataBase.userInfo, (name,))

        out = self.dbCursor.fetchone()

        return {
            "name": out[0],
            "ip": out[1],
            "port": out[2],
            "pubKey": out[3]
        }

    def KeyExists(self, name):
        self.dbCursor.execute(DataBase.keyExists, (name,))

        if (int(self.dbCursor.fetchone()[0]) > 0):
            return True
        else:
            return False
