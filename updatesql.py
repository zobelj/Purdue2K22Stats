import csv
import mysql.connector as mysql

db = mysql.connect(
    host = '127.0.0.1:3306',
    user = 'root',
    passwd = 'password'

)
print(db)