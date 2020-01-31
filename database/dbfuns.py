import sqlite3
# pip install pysqlite3
conn = None
c = None
data = None


def connectDB():
    global conn, c
    conn = sqlite3.connect('RaidenLeaderboard.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='leaderboard';")
    res = c.fetchone()
    if res is None:
        createTable()
    c = conn.cursor()


def createTable():
    c.execute('''CREATE TABLE leaderboard
             (playername text, score integer)''')


def saveChanges():
    conn.commit()


def closeConnection():
    conn.close()


def insertValues(playername, score):
    c.execute('INSERT into leaderboard values (?, ?)', (playername, score))


def selectScores():
    global data
    c.execute('SELECT * from leaderboard ORDER BY score desc LIMIT 3')
    data = c.fetchall()


# def printAll():
#     c.execute('SELECT * from leaderboard ORDER BY score desc')
#     for a in c.fetchall():
#         print(a['playername'])
#         print(a['score'])
