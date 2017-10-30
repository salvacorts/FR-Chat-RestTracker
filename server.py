#!/usr/bin/env python3

from falcon import HTTP_404, HTTP_201, HTTP_409, HTTP_403
from modules.database import DataBase
import modules.constants
import hug, falcon

db = DataBase("database/users.db")

@hug.post("/users/add/")
@hug.get("/users/add/{name}&{ip}&{pubKey}")
def AddUser(name, ip, pubKey, response=None):
    if db.KeyExists(name):
        response.status = HTTP_409
        return "User {0} already exists".format(name)

    db.AddUser(name, ip, pubKey)

    response.status = falcon.HTTP_201
    return "User Added"

@hug.post("/users/update/")
@hug.get("/users/update/{name}&{ip}&{pubKey}&{validationMSG}")
def UpdateUser(name, ip, pubKey, validationMSG, response=None):
    if not db.KeyExists(name):
        response.status = HTTP_404
        return "User {0} doesn't exists".format(name)

    if not db.UpdateUser(name, ip, pubKey, validationMSG):
        response.status = HTTP_403
        return "Invalid credentials"

    response.status = falcon.HTTP_201
    return "User info updated"

@hug.get("/users/get/{name}")
def GetUserInfo(name, response=None):
    if not db.KeyExists(name):
        response.status = HTTP_404
        return "User {0} doesn't exists".format(name)

    user = db.GetUser(name)

    return user

@hug.get("/key/")
def GetUserInfo(name, response=None):
    return constants.KEY


@hug.get("/", output=hug.output_format.html)
def Home():
    return """
        <html>
            <body>
                <h1>Hi there!</h1>
                <p>Dont break anything ;)</p>
            </body>
        </html>
    """
