import sqlite3

#InfoArrays

t = [[1,"Auday"], [2,"Leo"], [3,"Vaclav"]]
p = [[1, 1, "Super"], [1, 2, "Giga"], [1, 3, "Mega"], [2, 51, "Super-fast-one"], [3, 50, "Scary-one"]]

conn = sqlite3.connect('pokedex.db')
cursor = conn.cursor()
print("Opened database successfully")

#--------------------------------------------------------------------------
#Creation of the tables

conn.execute('''CREATE TABLE IF NOT EXISTS Trainers(
           trainer_id                   INT                     PRIMARY KEY,
           trainer_name                 TEXT                    NOT NULL

         )''')
print("Table1 created successfully")


conn.execute('''CREATE TABLE IF NOT EXISTS Pairs(
            trainer_id                  INT                     NOT NULL,
            pokemon_id                  INT                     NOT NULL,
            pokemon_name                TEXT                    NOT NULL,
            FOREIGN KEY(trainer_id)     REFERENCES Trainers(trainer_id),
            FOREIGN KEY(pokemon_id)     REFERENCES pokedex(pokedex_number)

                )''')
print("Table2 created successfully")


#End of table creation
#--------------------------------------------------------------------------
#Inject new tables with data from lists

for element in t:
    conn.execute("INSERT INTO Trainers (trainer_id,trainer_name) VALUES (?,?)", (element[0], element[1]))


for element in p:
    conn.execute("INSERT INTO Pairs(trainer_id, pokemon_id, pokemon_name) VALUES (?,?,?)", (element[0], element[1], element[2]))

#End of injection
#--------------------------------------------------------------------------



pairs = conn.execute(
                 ' SELECT '                                                                     #Query
                 ' Pairs.pokemon_name,'                                                         #First pick
                 ' pokedex.name,'                                                               #Second pick
                 ' Trainers.trainer_name FROM Pairs'                                            #Third pick
                 ' INNER JOIN Trainers ON Pairs.trainer_id = Trainers.trainer_id'               #Inner Join Trainers, Pairs
                 ' INNER JOIN pokedex ON Pairs.pokemon_id = pokedex.pokedex_number')            #Inner Join pokedex, Pairs

for element in pairs:
    print('Name of the pokemon:', element[0], 'type:', element[1], 'its trainer:', element[2])


