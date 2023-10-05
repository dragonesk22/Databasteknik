from mysql.connector import connect

db = connect(
    host='fries.it.uu.se',
    user='ht23_1_group_13',
    password='pasSWd_13',
    database='ht23_1_project_group_13'
)

cursor = db.cursor()
prod_id = input("Enter productID: ")

attribute_name = "percent_discount"
table_name = "Product"
query = f"SELECT {attribute_name} FROM {table_name} WHERE prod_ID = {prod_id};"

cursor.execute(query)
attr_val = cursor.fetchone()[0]
print("Current % Discount: " + str(attr_val))

action = input("Enter new percentage discount (or leave empty to not change): ")
if action:
    query =f"UPDATE {table_name} SET {attribute_name} = {action} WHERE prod_ID = {prod_id};"
    cursor.execute(query)
    db.commit()
    print("Value updated.")
else:
    print("Value not updated.")

cursor.close()
db.close()
