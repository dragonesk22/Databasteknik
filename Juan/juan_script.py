from mysql.connector import connect

db = connect(
    host='fries.it.uu.se',
    user='ht23_1_group_13',
    password='pasSWd_13'
)

cursor = db.cursor()

cursor.execute("SHOW DATABASES")
for x in cursor:
    print(x)
db.close()
