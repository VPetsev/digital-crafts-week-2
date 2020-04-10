import logic
import os
import json

pool_hall_tables = []
my_poolhall = logic.PoolHall(pool_hall_tables)

def show_menu():
    print(""" 
            Menu options (1/2/3/4/5/q):
            1. Mark a table as occupied
            2. Mark a table as unoccupied
            3. See all active tables
            4. Total revenue
            5. Revenue per table
            q. Press q to quit""")

try:
    with open('tables.json', 'r') as file:
        saved_tables = json.load(file)
        for i in range(0, len(saved_tables)):
            print(saved_tables[i].items())
            pool_hall_tables.append(saved_tables[i])
            print(pool_hall_tables)
        print("Tables successfully loaded! (Hopefully)")
except FileNotFoundError:
    with open('tables.json', 'w') as file:
        for i in range(1, 13):
            table = logic.Table(i)
            pool_hall_tables.append(table)
        print("Tables successfully loaded!")
except json.decoder.JSONDecodeError:
    with open('tables.json', 'w') as file:
        for i in range(1, 13):
            table = logic.Table(i)
            pool_hall_tables.append(table)
        print("Tables successfully loaded!")
except:
    print("Unknown error occured! Sorry!")

def save_to_json(pool_hall_tables):
    my_saved_array = []
    for i in range(0, len(pool_hall_tables)):
        table = pool_hall_tables[i]
        my_saved_array.append(table.toDict())

    with open('tables.json', 'w') as file:
        json.dump(my_saved_array, file, indent=4)

