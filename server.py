#!/usr/bin/env python3

from modules.database import DataBase
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