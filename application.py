import MySQLdb

conn = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
cursor = conn.cursor()

cursor.execute('SELECT COUNT(MemberID) as count FROM Members WHERE id = 1')
row = cursor.fetchone()

conn.close()

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!" + row
