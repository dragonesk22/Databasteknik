from mysql.connector import connect
from pandas import DataFrame as DF

db = connect(
    host='fries.it.uu.se',
    user='ht23_1_group_13',
    password='pasSWd_13',
    database='ht23_1_project_group_13'
)

cursor = db.cursor()
# cursor.execute("SHOW DATABASES")

# for x in cursor:
#    print(x)


# Query 1: Select every tuple from the Department table.
table_name = "Department"
query = f"SELECT * FROM {table_name}"


cursor.execute(query)

# Saves the tuples of the relation Department with attributes dpt_id, title...
dpt_relation = {}

for i, tuple in enumerate(cursor.fetchall()):
    dpt_relation[f't{i}'] = tuple

data = DF(dpt_relation).T

data.columns = ['dept_ID', 'title', 'description', 'link']

"""
Assignment 7. Create a Python program which connects to the database, asks the user for a
department ID (i.e. the primary key) and lists all its products (outputting the ID, the title
and the retail price after the discount) if the given department is a leaf department, otherwise
list all its child department  (outputting the ID and the title).
"""


def user_session():
    valid = False

    while not valid:
        dept_ID = int(input("Enter Department ID: "))

        assert isinstance(dept_ID, int), 'Wrong input-type try again...'

        valid = True

    def _browse_data(bool=False):
        b = bool

        possible_cmds = ['dept_ID', 'title', 'description', 'link', 'Show', 'Exit']

        while b is not False:
            cmd = input("What data do you want to see? Enter 'Show' for possibilities: ")

            assert cmd in possible_cmds

            if cmd != 'Show' and cmd != 'Exit':
                print(data[cmd])

            elif cmd == 'Show':
                print(f'The possible commands for this session are: {possible_cmds}')

            elif cmd == 'Exit':

                b = False

            else:

                raise NotImplementedError("Command is not implemented. ")

        print("Session terminated by user.")
    _browse_data(True)



user_session()


db.close()




"""

Instructions to execute MAIN_SCRIPT.py remotely: 

1. Start terminal 
2. Enter scp MAIN_SCRIPT.py ussr1234@fries.it.uu.se:~/
3. Enter your studium password A.
4. In terminal enter ssh ussr1234@fries.it.uu.se
5. Execute python MAIN_SCRIPT.py
"""






"""


for keys, vals in dpts_.items():
    print(f'Keys : {keys} Vals: {vals}')
                dep_ID  title                   descr                link
Keys : t0 Vals: (1000, 'Welcome to AltOnline', 'altonline.com/Home', 'Home')
Keys : t1 Vals: (1200, 'Electronics and more here', 'altonline.com/Home/Electronics/', 'Electronics')
Keys : t2 Vals: (1201, 'Buy good phones', 'altonline.com/Home/Electronics/Phones', 'Phones')
Keys : t3 Vals: (1202, 'Buy good computers', 'altonline.com/Home/Electronics/Computers', 'Computers')
Keys : t4 Vals: (1203, 'Buy large TVs', 'altonline.com/Home/Electronics/TVs', 'TVs')
Keys : t5 Vals: (1300, 'Food', 'altonline.com/Home/Food', 'Food')
Keys : t6 Vals: (1301, 'Buy tasty bread', 'altonline.com/Home/Food/Bread', 'Bread')
Keys : t7 Vals: (1302, 'Buy fresh fruit', 'altonline.com/Home/Food/Fruit', 'Fruit')

"""
