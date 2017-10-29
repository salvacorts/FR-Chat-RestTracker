#!/usr/bin/env python3

from modules.database import DataBase
from modules.users import User
import hug, falcon

db = DataBase("database/users.db")

@hug.post("/users/add/")
@hug.get("/users/add/{name}&{ip}&{pubKey}")
def AddUser(name, ip, pubKey, response=None):
    if db.KeyExists(name):
        response.status = falcon.HTTP_418
        return "User {0} already exists".format(name)

    db.AddUser(name, ip, pubKey)

    response.status = falcon.HTTP_201
    return "User Added"

@hug.get("/users/get/{name}")
def GetUserInfo(name, response=None):
    if not db.KeyExists(name):
        response.status = falcon.HTTP_404
        return "No user named: {0}".format(name)

    user = db.GetUser(name)

    return user


# AddUser("Salva", "127.0.0.1", "lmaooo")
# GetUserInfo("Salva")
