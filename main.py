#!/usr/bin/env python3

from modules.database import UsersDB
from modules.users import User
import hug, falcon

db = UsersDB()

@hug.post("/post/")
def testPost(uno, otro):
    return uno + "\t" + otro

@hug.post("/users/add/")
def AddUser(name, ip, pubKey, response=None):
    if db.KeyExists(name):
        response.status = falcon.HTTP_418
        return "User {0} already exists".format(name)

    db.AddUser(User(name, ip, pubKey))

    response.status = falcon.HTTP_201
    return "User Added"

@hug.get("/users/get/{name}")
def GetUserInfo(name, response=None):
    if not db.KeyExists(name):
        response.status = falcon.HTTP_404
        return "No user named: {0}".format(name)

    user = db.GetUser(name)

    return {
        "name": user.name,
        "ip": user.ip,
        "pubKey": user.pubKey
    }
