from mysql.connector import connect

db = connect(
    host='fries.it.uu.se',
    user='ht23_1_group_13',
    password='pasSWd_13',
    database='ht23_1_project_group_13'
)


cursor = db.cursor()
#cursor.execute("SHOW DATABASES")

#for x in cursor:
#    print(x)


table_name = "Customer"
query = f"SELECT * FROM {table_name}"

cursor.execute(query)
for row in cursor.fetchall():
    print(row)

db.close()
