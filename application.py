import pyodbc

from flask import Flask
app = Flask(__name__)


server = 'wichmann.database.windows.net'
database = 'TestDatabase'
username = 'wichmann'
password = 'HuluHulu1'
driver= '{ODBC Driver 13 for SQL Server}'

cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM Course")
row = cursor.fetchone()
    while row:
    print (str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()

@app.route("/")
def hello():
    return "Hello World! str(row[0])"
