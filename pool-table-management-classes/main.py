from datetime import date
from textwrap import dedent
import view
import json
from logic import Table, PoolHall
import random
import os

running = True

# Initialize pool hall - Run only at first start up

while running:
    # Refactor menu to a function. Where to put?
    print(""" 
        Menu options (1/2/3/4/5/q):
        1. Mark a table as occupied
        2. Mark a table as unoccupied
        3. See all active tables
        4. Total revenue
        5. Revenue per table
        q. Press q to quit""")
    choice = input()
    if choice == '1':
        # Refactor for loop here? Some parts reused in choice 2
        user_table_num = int(input("Choose a table to mark occupied: "))
        for index in range(0, len(view.pool_hall_tables)):
            if view.pool_hall_tables[index].table_number == user_table_num:
                objective_table = Table(index)
                objective_table.mark_table_as_occupied(user_table_num - 1)
                objective_table.time_adder(index)
                break
        # refactor else statement? lol
        else:
            "Please choose a valid table"
    elif choice == '2':
        user_table_num = int(input("Choose a table to mark unoccupied: "))
        for index in range(0, len(view.pool_hall_tables)):
            if view.pool_hall_tables[index].table_number == user_table_num:
                objective_table = Table(index)
                objective_table.mark_table_as_unoccupied(user_table_num - 1)
                objective_table.time_adder(index)
                print(index)
                print(user_table_num)
                view.my_poolhall.reset_table(user_table_num)
                break
        else:
            "Please choose a valid table"
    elif choice == '3':
        view.my_poolhall.view_tables_in_hall()
    elif choice == '4':
        pass
    if choice == 'q':
        break
