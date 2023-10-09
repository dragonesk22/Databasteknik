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
    """
    :param cursor:
    :return: tables currently defined in the database.
    """
    tables = []
    cursor.execute("SHOW TABLES")

    for table in cursor:
        tables.append(table)

    tables = [item[0] for item in tables]

    return tables


def get_attributes(table_name, cursor):
    """
    :param table_name: Table name is given by the user in a session.
    :param cursor: When the user is connected the session needs a cursor as an input parameter.
    :return: Returns a list of attributes in the relation table specified by table_name.
    """

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
    """
    :param bool: When the user session has started, we want to specify that it is True, that the user wants to browse.
    :param data: data is given by the users specified table to be browsed.
    :return: Does not return any values.
    """
    b = bool

    possible_cmds = data.columns.tolist() + ['Show', 'Exit']

    while b is not False:

        cmd = input("\n" * 2 + "What data do you want to see?. Enter 'Show' for possibilities. \n")

        if cmd != 'Show' and cmd != 'Exit':
            print(data[cmd])

        elif cmd == 'Show':
            print(f'The possible commands for this session are: \n{possible_cmds}')

        elif cmd not in possible_cmds:

            print("Command not available try again.")

        elif cmd == 'Exit':

            b = False

        else:
            # To be fixed.
            print("Cannot currently browse other tables than 'Department', try another table.")

    print(f"Session terminated by user at {ctime()}.")


def admin_session(cursor):
    """
    :param cursor:

    """
    tables = Get_Tables(cursor)

    time = ctime()
    print('\n' * 2)
    print(f"User started session in database at {time}", end='\n' * 2)
    print(f"Available tables for inspection are: \n{tables}", end='\n' * 2)

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


def change_capitalism(prod_ID, prod_data, cursor):
    ID = prod_ID
    print(f"ID entered by user is: {ID}")

    for i, ids in enumerate(prod_data['prod_ID']):

        if ID == ids:
            print(f"The current discount for the product ID {ID} is {prod_data['percent_discount'][i]}")

    question = float(input("Set the percent discount? If so enter decimal in the range (0, 1): "))

    print(f"The discount set by the user is: {question}")

    if 0 <= question <= 1:

        query = f"UPDATE Product SET percent_discount = {question} WHERE prod_ID = {ID}"

        cursor.execute(query)

    data_update = get_table_data('Product', cursor)

    updated_data = data_update[['title','percent_discount']]
    print(updated_data)

def capitalism(dep_ID, prod_data):
    # assert dep_ID in prod_data['dep_ID'], 'Department is not leaf'

    """

    :param prod_data:
    :return: ID, title, price, price + discount, discounted price + VAT
    """

    discounts = prod_data['percent_discount']
    real_price = prod_data['prod_price']

    for i, leaf in enumerate(prod_data['dep_ID']):

        if leaf == dep_ID:
            print(f"Product ID: {prod_data['prod_ID'][i]}")
            print(f"Product title: {prod_data['title'][i]} ")
            print(f"Product price: {(real_price[i] * (1 - discounts[i]))}")


def user_session(cursor):
    time = ctime()
    print('\n' * 2)
    print(f"User started session in database at {time}", end='\n' * 2)

    tables = Get_Tables(cursor)

    inp_ = int(input("Enter a Department ID: "))

    data_hierarchy = get_table_data('Parent_Relation', cursor)
    data_deparment = get_table_data('Department', cursor)
    data_product = get_table_data('Product', cursor)

    parents = data_hierarchy['parent_ID'].tolist()
    children = data_hierarchy['child_ID'].tolist()

    if inp_ in parents:

        print(f"Department {inp_} is a parent department. Here are its children: \n")

        for i, parent in enumerate(parents):

            if parent == inp_:
                print(f"Deparment ID {parent}, has child {children[i]}")

                print(f"The title of {children[i]} is {data_deparment['title'][i + 1]}", end='\n' * 2)

    else:

        capitalism(inp_, data_product)

    # print(data_deparment)

    """
    parent_of_inp = [parent for parent in parents if parent == inp_]
    child_of_inp = [child for child in children if child == inp_]

    print(f"The input department is {inp_} and has whatever: ")
    print(parent_of_inp, end='\n'*3)
    print(child_of_inp, end='\n'*3)
    """

    # print(data_deparment)


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


# admin_session(c)

# User_session
def main():
    c, db = Connect()

    """
    During the admin_session() we suggest the following input:
    
    1. Parent_Relation          to see parents and their children. Dont exit on first step.
    2. parent_ID                to see available parents. 
    4. child_ID                 to see children of parents in tuple order
    5. Exit
    
    Parents:        Children: 
    t0    1000      1200
    t1    1200      1201
    t2    1200      1202
    t3    1200      1203
    t4    1000      1300
    t5    1300      1301
    t6    1300      1302
    t7    1300      1303
    
    6. Choose a parent to see their children and their descriptions. 
    7. or choose child to see their products. 
    8. If parent ID entered observe its children. (Example 1000)
    9. Enter 'Department' after input of parent ID 1000
    10. Enter '1200' (also a parent)
    11. Enter 'Department'
    12. Enter '1202' (child department)
    13. Enter '1004' (Thinkpad)
    14. Enter new discount.
    """
    admin_session(c)

    user_session(c)

    exit = False
    while exit is not True:
        prompt = input("Which product would you like to be discounted? If you want to go back to department enter 'Department'.\n"
                       "Otherwise Enter ID for the product you want to discount: ")
        if prompt == 'Department':
            user_session(c)
        elif int(prompt) % 1 != 0:
            print("ID must be integer.")

        else:
            exit = True

    prod_ID_to_change = int(prompt)
    prod_DATA = get_table_data('Product', c)

    change_capitalism(prod_ID_to_change, prod_DATA, c)
    db.commit()

    db.close()


main()
