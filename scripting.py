from mysql.connector import connect

db = connect(
    host='fries.it.uu.se',
    user='ht23_1_group_50',
    password='pasSWd_50'
)

cursor = db.cursor()

cursor.execute("SHOW DATABASES")

for x in cursor:
    print(x)

cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)

db.close()