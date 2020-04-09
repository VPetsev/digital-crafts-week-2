from textwrap import dedent
import json
import logic
import random
import os

running = True

while running:
    print("Menu options (1/2/3/q): ")
    print("1. Mark a table as occupied")
    print("2. Mark a table as unoccupied")
    print("3. See all active tables")
    print("4. Total revenue")
    print("q. Press q to quit")

    choice = input()
    if choice == '1':
        table_num = int(input("Which table to mark as occupied? "))
        print(logic.mark_as_occupied(table_num))
        logic.time_adder()
    elif choice == '2':
        table_num = int(input("Which table to mark as unoccupied? "))
        print(logic.mark_as_unoccupied(table_num))
        logic.time_adder()
    elif choice == '3':
        # see only active tables
        # see only inactive tables
       logic.view_tables(0)

    if choice == 'q':
        break

with open('tables.json', 'w') as file:
    json.dump(logic.table_list, file, indent=4)
