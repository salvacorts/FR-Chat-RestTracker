import sqlite3, time

# DOC: https://sqlite.org/lang_datefunc.html

dataFile = "database/users.db"
sql = """DELETE FROM users WHERE creacion<DATETIME("now", "-1 minute")"""

while True:
    db = sqlite3.connect(dataFile)
    dbCursor = db.cursor()

    dbCursor.execute(sql);
    db.commit()
    dbCursor.close()

    time.sleep(24*60*60) # Rest for a day
