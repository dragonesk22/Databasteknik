from mysql.connector import connect
from pandas import DataFrame as DF
from time import ctime

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

tables = []
cursor.execute("SHOW TABLES")

for table in cursor:
    tables.append(table)

tables = [item[0] for item in tables]


def get_table(input):
    """
    :param input: Should be a string with an avilable table name.
    :return: data: Returns data corresponding to the input table
    """

    # Query 1: Select every tuple from the Department table.

    table_name = input # Input should be in the available tables for inspection

    query = f"SELECT * FROM {table_name}"


    cursor.execute(query)

    # Saves the tuples of the relation Department with attributes dpt_id, title...
    _relation = {}

    for i, tuple in enumerate(cursor.fetchall()):
        _relation[f't{i}'] = tuple

    data = DF(_relation).T

    available = ['Department']

    if input == "Department":
        data.columns = ['dept_ID', 'title', 'description', 'link']

    else:

        print(f"Cannot currently browse other tables than {available}. Try again.")


    return data



"""
Assignment 7. Create a Python program which connects to the database, asks the user for a
department ID (i.e. the primary key) and lists all its products (outputting the ID, the title
and the retail price after the discount) if the given department is a leaf department, otherwise
list all its child department  (outputting the ID and the title).
"""


def _browse_data(bool, data):
    b = bool

    possible_cmds = ['dept_ID', 'title', 'description', 'link', 'Show', 'Exit']

    while b is not False:
        cmd = input("\n"*2 + "What data do you want to see? Enter 'Show' for possibilities: ")

        if cmd != 'Show' and cmd != 'Exit':
            print(data[cmd])

        elif cmd == 'Show':
            print(f'The possible commands for this session are: {possible_cmds}')

        elif cmd not in possible_cmds:

            print("Command not avaliable try again.")

        elif cmd == 'Exit':

            b = False

        else:

            print("Cannot currently browse other tables than 'Department', try annother table.")

    print(f"Session terminated by user at {ctime()}.")

def user_session():

    time = ctime()
    print('\n'*2)
    print(f"User started session in database at {time}", end='\n'*2)
    print(f"Available tables for inspection are: {tables}", end='\n'*2)

    valid = False

    while not valid:

        inp = input("What table would like to search? Enter 'Show' to see available tables. Enter 'Exit' to quit program: ")

        if inp in tables:

            valid = True


        elif inp == 'Show':

            print(f"Available tables for inspection are: {tables}")

        elif inp == 'Exit':

            break
            print(f"Session terminated by user at {ctime()}")

        else:

            print("Table not recognized try again...")

    data = get_table(inp)

    _browse_data(True, data)













user_session()


db.close()




"""

Instructions to execute MAIN_SCRIPT.py remotely: 

1. Start terminal 
2. Enter scp MAIN_SCRIPT.py ussr1234@fries.it.uu.se:~/
3. Enter your studium password A.
4. In terminal enter ssh ussr1234@fries.it.uu.se
6. Enter your password A.
7. Execute python MAIN_SCRIPT.py
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
