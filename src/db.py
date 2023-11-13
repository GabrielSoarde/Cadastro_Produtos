import pymysql

# Do not forget to change the password and the database, in db.py, accordingly. (I used XAMPP for SQL integration.)


mysql = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '',
    database = '',
)