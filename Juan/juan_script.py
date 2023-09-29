from mysql.connector import connect

db = connect(
    host='fries.it.uu.se',
    user='ht23_1_group_13',
    password='pasSWd_13'
)

cursor = db.cursor()

table_name = "Customer"
query = f"SELECT * FROM {table_name}"
cursor.execute(query)
for row in cursor.fetchall():
    print(row)
db.close()
