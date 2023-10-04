from mysql.connector import connect
from pandas import DataFrame as DF
from time import ctime


def Connect():
    DB = connect(
        host='fries.it.uu.se',
        user='ht23_1_group_13',
        password='pasSWd_13',
        database='ht23_1_project_group_13'
    )
    return DB.cursor(), DB


def Get_Tables(cursor):
    tables = []
    cursor.execute("SHOW TABLES")

    for table in cursor:
        tables.append(table)

    tables = [item[0] for item in tables]

    return tables


def get_attributes(table_name, cursor):

    query = f"DESCRIBE {table_name}"
    cursor.execute(query)

    attributes = [row[0] for row in cursor.fetchall()]

    return attributes


def get_table_data(input, cursor):
    """
    :param input: Should be a string with an available table name.
    :return: Returns data corresponding to the input table
    """
    table_name = input

    query = f"SELECT * FROM {table_name}"

    cursor.execute(query)

    _relation = {}

    for i, tuple in enumerate(cursor.fetchall()):
        _relation[f't{i}'] = tuple

    data = DF(_relation).T

    data.columns = get_attributes(input, cursor)

    return data


def browse_data(bool, data):
    b = bool

    possible_cmds = data.columns.tolist() + ['Show', 'Exit']

    while b is not False:

        cmd = input("\n" * 2 + "What data do you want to see?. Enter 'Show' for possibilities. \n")

        if cmd != 'Show' and cmd != 'Exit':
            print(data[cmd])

        elif cmd == 'Show':
            print(f'The possible commands for this session are: {possible_cmds}')

        elif cmd not in possible_cmds:

            print("Command not availiable try again.")

        elif cmd == 'Exit':

            b = False


        else:

            print("Cannot currently browse other tables than 'Department', try another table.")

    print(f"Session terminated by user at {ctime()}.")


def user_session(cursor):
    tables = Get_Tables(cursor)

    time = ctime()
    print('\n' * 2)
    print(f"User started session in database at {time}", end='\n' * 2)
    print(f"Available tables for inspection are: {tables}", end='\n' * 2)

    valid = False

    while not valid:

        str = ("Enter 'Show' to see available tables. Enter 'Exit' to quit program. \n"
               "Which table would you like to search? ")

        inp_ = input(str)

        if inp_ in tables:

            valid = True

        elif inp_ == 'Show':

            print(f"Available tables for inspection are: {tables}")

        elif inp_ == 'Exit':

            print(f"Session terminated by user at {ctime()}")

            break

        else:

            print("Table not recognized try again...")

    data = get_table_data(inp_, cursor)

    browse_data(True, data)


"""
main code

Instructions to execute MAIN_SCRIPT.py remotely: 

1. Start terminal 
2. Enter scp MAIN_SCRIPT.py ussr1234@fries.it.uu.se:~/
3. Enter your studium password A.
4. In terminal enter ssh ussr1234@fries.it.uu.se
6. Enter your password A.
7. Execute python MAIN_SCRIPT.py


Problems Order_Progress Empty.


"""

# Cursor and database object.

c, db = Connect()

user_session(c)

db.close()
