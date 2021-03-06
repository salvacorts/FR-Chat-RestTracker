#!/usr/bin/env python3

from falcon import HTTP_404, HTTP_201, HTTP_409, HTTP_403, HTTP_202
from modules.database import DataBase
from modules.constants import *
import hug


db = DataBase("database/users.db")


@hug.post("/users/add/")
@hug.get("/users/add/{name}&{ip}&{port}&{pubKey}")
def AddUser(name, ip, port, pubKey, response=None):
    if db.KeyExists(name):
        response.status = HTTP_409
        return "User {0} already exists".format(name)

    db.AddUser(name, ip, port, pubKey)

    response.status = HTTP_201
    return "User Added"


@hug.post("/users/update/")
@hug.get("/users/update/{name}&{ip}&{port}&{validationMSG}")
def UpdateUser(name, ip, port, validationMSG, response=None):
    if not db.KeyExists(name):
        response.status = HTTP_404
        return "User {0} doesn't exists".format(name)

    if not db.UpdateUser(name, ip, port, validationMSG):
        response.status = HTTP_403
        return "Invalid credentials"

    response.status = HTTP_202
    return "User info updated"


@hug.get("/users/get/{name}")
def GetUserInfo(name, response=None):
    if not db.KeyExists(name):
        response.status = HTTP_404
        return "User {0} doesn't exists".format(name)

    user = db.GetUser(name)

    return user


@hug.get("/key/")
def GetUserInfo():
    return KEY


@hug.get("/", output=hug.output_format.html)
def Home():
    return HOME_HTML
